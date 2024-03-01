"""
Snirk API for connecting to and interacting with SNI devices.
"""

import asyncio

from contextlib import asynccontextmanager
from dataclasses import dataclass
from functools import wraps
from typing import Any, AsyncGenerator, Callable, Optional

import grpc
import grpc._channel

from snirk.sni import sni_pb2 as pb
from snirk.sni import sni_pb2_grpc as sni
from snirk.constants import SnirkConstants
from snirk.types import AddressEnum

__all__ = ["Snirk"]


class SnirkError(BaseException):
    pass


class SnirkIncapableError(BaseException):
    """Exception raised when SNI device does not have needed capability."""


@dataclass
class Snirk:
    """
    Container and API for connecting to and interacting with SNI device.

    :param channel: target host/port running SNI server
    """

    channel: str = "localhost:8191"

    _device: Optional[pb.DevicesResponse.Device] = None
    _rom_mapping: Optional[pb.MemoryMapping] = None

    @property
    def device(self) -> pb.DevicesResponse.Device:
        if self._device is None:
            self._device = asyncio.run(self.find_device())
        return self._device

    @device.setter
    def device(self, uri: str):
        self._device = asyncio.run(self.find_device(uri=uri))

    async def detect_rom_mapping(self, force: bool = False, timeout: int = 3) -> pb.MemoryMapping:
        """Cached detection of memory mapping from ROM.

        Use lookup from cache unless forced to detect again.

        :param force: when True, force detecting ROM memory mapping, even if cached
        :param timeout: seconds to attempt detecting ROM memory mapping before timing out
        :raises SnirkError: cannot detect memory mapping from ROM
        :return: memory mapping of ROM
        """
        # unless forced, used cached memory mapping when cached
        if not force and self._rom_mapping is not None:
            return self._rom_mapping

        device = await self.find_device()

        async with self.grpc_channel(timeout=timeout) as ch:
            stub = sni.DeviceMemoryStub(ch)
            response = stub.MappingDetect(pb.DetectMemoryMappingRequest(uri=device.uri))

        if not response or not (mm := response.memoryMapping):
            raise SnirkError("Could not detect memory mapping from ROM!")

        self._rom_mapping = mm
        return mm

    async def ensure_capability(self, capability: pb.DeviceCapability) -> bool:
        """Ensure device has specified capability or raise exception.

        :raises SnirkIncapableError: when device does not have specified capability
        :returns: True when device has capability
        """
        device = await self.find_device()

        if capability not in device.capabilities:
            cap_name = SnirkConstants.CAPABILITY_LOOKUP[capability]
            raise SnirkIncapableError(f"Device does not have {cap_name} capability: {device.uri}")
        return True

    async def find_device(
        self, kind: Optional[str] = None, force: bool = False, timeout: int = 10, uri: Optional[str] = None
    ) -> pb.DevicesResponse.Device:
        """Cached lookup of finding SNI device.

        Use lookup from cache unless forced to detect again.
        When multiple SNI devices are found, if uri parameter is specified, uses that one. Otherwise uses
        first device.

        :param kind: limit devices to specified kind (e.g. "fxpakpro")
        :param force: when True, force finding SNI device, even if cached
        :param timeout: seconds to attempt detecting SNI device before timing out
        :param uri: select device specified by URI
        :raises SnirkError: cannot find any SNI devices or specified URI
        :return: SNI device URI string
        """
        # unless forced, used cached device when cached
        if not force and self._device is not None:
            # force if current cached device does not match kind or uri
            if (not kind or self._device.kind == kind) and (not uri or self._device.uri == uri):
                return self._device

        devices: list[pb.DevicesResponse.Device] = []

        try:
            devices = await self.list_devices(kind=kind, timeout=timeout)
        except asyncio.TimeoutError:
            pass

        if not devices:
            if kind:
                raise SnirkError(f"Could not find any SNI devices of kind: {kind}")
            raise SnirkError("Could not find any SNI devices!")

        if uri:
            try:
                device = next(device for device in devices if device.uri == uri)
            except StopIteration:
                raise SnirkError(f"Could not find device specified by URI: {uri}")
        else:
            device = devices[0]

        # cache results for future lookups
        self._device = device
        return self._device

    async def list_devices(self, kind: Optional[str] = None, timeout: int = 10) -> list[pb.DevicesResponse.Device]:
        """Get list of all SNI devices or time out.

        :param kind: limit devices to specified kind (e.g. "fxpakpro")
        :param timeout: seconds to detect SNI devices before timing out
        :raises SnirkError: connection refused to gRPC device at target channel
        :return: list of detected SNI devices
        """
        devices: list[pb.DevicesResponse.Device] = []

        async with asyncio.timeout(timeout):
            while True:
                try:
                    with grpc.insecure_channel(self.channel) as ch:
                        stub = sni.DevicesStub(ch)
                        response = stub.ListDevices(pb.DevicesRequest(kinds=[]))
                except grpc._channel._InactiveRpcError as exc:
                    if "connection refused" in str(exc).lower():
                        raise SnirkError(f"Connection refused: {self.channel}")
                    raise

                if response:
                    # filter devices based on kind, if specified
                    if kind:
                        devices = [device for device in response.devices if device.kind == kind]
                    else:
                        devices = [device for device in response.devices]
                    if devices:
                        break

                timeout = max(0, timeout - 1)
                await asyncio.sleep(1)
        return devices

    async def multi_read(self, *addresses: AddressEnum, timeout: int = 3) -> pb.MultiReadMemoryResponse:
        """Read multiple addresses in single request.

        :param addresses: address/size pairs to read
        :param timeout: timeout for response
        """
        device = await self.find_device()
        mm = await self.detect_rom_mapping()
        requests = [
            pb.ReadMemoryRequest(requestAddress=address.address, requestMemoryMapping=mm, size=address.size)
            for address in addresses
        ]

        async with self.grpc_channel(timeout=timeout) as ch:
            stub = sni.DeviceMemoryStub(ch)
            return stub.MultiRead(pb.MultiReadMemoryRequest(uri=device.uri, requests=requests))

    async def single_read(self, address: AddressEnum, timeout: int = 3) -> pb.SingleReadMemoryResponse:
        """Read single address.

        :param address: address/size pair to read
        :param timeout: timeout for response
        """
        device = await self.find_device()
        mm = await self.detect_rom_mapping()
        request = pb.ReadMemoryRequest(requestAddress=address.address, requestMemoryMapping=mm, size=address.size)

        async with self.grpc_channel(timeout=timeout) as ch:
            stub = sni.DeviceMemoryStub(ch)
            return stub.SingleRead(pb.SingleReadMemoryRequest(uri=device.uri, request=request))

    @asynccontextmanager
    async def grpc_channel(
        self, options: Optional[list[tuple[str, Any]]] = None, timeout: int = 10
    ) -> AsyncGenerator[grpc.Channel, None]:
        """Async context manager for gRPC channel with timeout.

        :param options: options to pass to creating gRPC channel
        :param timeout: seconds until timeout
        :yields: grpc channel
        """
        async with asyncio.timeout(timeout):
            with grpc.insecure_channel(self.channel, options=options) as channel:
                yield channel

    @classmethod
    @asynccontextmanager
    async def session(cls, kind: Optional[str] = None, uri: Optional[str] = None) -> AsyncGenerator["Snirk", None]:
        """Async context manager for SNI session.

        :param kind: limit devices to specified kind (e.g. "fxpakpro")
        :param uri: select device specified by URI
        """
        snirk = cls()
        await snirk.find_device(kind=kind, uri=uri)
        yield snirk

    @staticmethod
    async def retry_grpc(
        fn: Callable[..., Any],
        backoff: bool = True,
        max_retries: Optional[int] = None,
        sleep: float = 0.1,
        timeout: int = 10,
    ):
        """Decorator for gRPC function with base-2 exponential backoff, max retries, and timeout.

        :param backoff: when True, double sleep between each retry
        :param max_retries: maximum amount of retries to try (default: -1, unlimited retries until timeout)
        :param sleep: seconds between retries (initial when backoff is used)
        :param timeout: seconds until timeout
        """

        @wraps(fn)
        async def wrapper(*args, **kwargs):
            retries = 0
            sleep_time = sleep
            async with asyncio.timeout(timeout):
                while max_retries is None or retries < max_retries:
                    try:
                        return fn(*args, **kwargs)
                    except grpc._channel._InactiveRpcError as exc:
                        if "does not contain USBA header" not in str(exc):
                            raise
                    await asyncio.sleep(sleep_time)
                    if backoff:
                        sleep_time *= 2
                    retries += 1

        return wrapper
