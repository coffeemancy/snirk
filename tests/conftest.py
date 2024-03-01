from contextlib import contextmanager
from typing import Generator
from unittest.mock import patch

import pytest

import snirk.sni.sni_pb2 as pb


class Helpers:
    """Common helper functions for tests."""

    @staticmethod
    @contextmanager
    def patch_devices(*devices: pb.DevicesResponse.Device) -> Generator[pb.DevicesResponse, None, None]:
        """Patch calls to ListDevices to return mocked devices."""
        response = pb.DevicesResponse()
        response.devices.extend(devices)

        with patch("grpc.insecure_channel"):
            with patch("snirk.api.sni.DevicesStub") as stub:
                with patch.object(stub.return_value, "ListDevices", return_value=response):
                    yield response


@pytest.fixture(scope="session")
def helpers():
    """Common helper functions for tests."""
    return Helpers


@pytest.fixture(scope="session")
def fxpakpro() -> pb.DevicesResponse.Device:
    """Fixture mocking SNI-connected FxPak Pro device."""
    device = pb.DevicesResponse.Device()
    device.uri = "fxpakpro://./dev/ttyACM1"
    device.displayName = "/dev/ttyACM1 (1209:5a22)"
    device.kind = "fxpakpro"
    device.capabilities.extend(
        [
            pb.DeviceCapability.BootFile,
            pb.DeviceCapability.ExecuteASM,
            pb.DeviceCapability.FetchFields,
            pb.DeviceCapability.GetFile,
            pb.DeviceCapability.MakeDirectory,
            pb.DeviceCapability.PutFile,
            pb.DeviceCapability.ReadDirectory,
            pb.DeviceCapability.ReadMemory,
            pb.DeviceCapability.RemoveFile,
            pb.DeviceCapability.RenameFile,
            pb.DeviceCapability.ResetSystem,
            pb.DeviceCapability.ResetToMenu,
            pb.DeviceCapability.WriteMemory,
        ]
    )
    return device


@pytest.fixture(scope="session")
def retroarch() -> pb.DevicesResponse.Device:
    """Fixture mocking SNI-connected Retroarch device."""
    device = pb.DevicesResponse.Device()
    device.uri = "ra://127.0.0.1:55355"
    device.displayName = "RetroArch v1.16.0 (127.0.0.1:55355)"
    device.kind = "retroarch"
    device.capabilities.extend(
        [
            pb.DeviceCapability.FetchFields,
            pb.DeviceCapability.PauseToggleEmulation,
            pb.DeviceCapability.ReadMemory,
            pb.DeviceCapability.ResetSystem,
            pb.DeviceCapability.WriteMemory,
        ]
    )
    device.defaultAddressSpace = pb.AddressSpace.SnesABus
    return device


@pytest.fixture(scope="session")
def sni_devices(helpers, fxpakpro, retroarch) -> Generator[pb.DevicesResponse, None, None]:
    """Fixture mocking SNI-connected devices."""
    devices = [fxpakpro, retroarch]
    with helpers.patch_devices(*devices) as response:
        yield response
