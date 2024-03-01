"""
Snirk API for connecting to and interacting with SNI device filesystems.
"""

from pathlib import Path

import grpc._channel

from snirk.api import Snirk
from snirk.sni import sni_pb2 as pb
from snirk.sni import sni_pb2_grpc as sni

__all__ = ["SnirkFilesystem"]


class SnirkFilesystem(Snirk):
    """
    Container and API for connecting to and interacting with SNI devices with access to device filesystem.

    Each operation assures that the SNI device has necessary capabilities before attempting to access
    the device filesystem, raising a SnirkIncapableError exception when the capabilities are missing.

    :param max_message_length: max bytes to transfer in get/put operations
    :type max_message_length: int
    """

    max_message_length: int = 1024**3

    async def get_file(self, device_file: str, timeout: int = 30) -> pb.GetFileResponse:
        """Get device file from SNI device filesystem.

        :param device_file: path to device file to read
        :param timeout: seconds until timeout reading file from device
        :raises SnirkIncapableError: when device does not have GetFile capability
        """
        device = await self.find_device()
        await self.ensure_capability(pb.DeviceCapability.GetFile)

        options = [
            ("grpc.max_message_length", self.max_message_length),
            ("grpc.max_receive_message_length", self.max_message_length),
        ]
        async with self.grpc_channel(options=options, timeout=timeout) as ch:
            stub = sni.DeviceFilesystemStub(ch)
            retry_get = await self.retry_grpc(stub.GetFile, max_retries=3, sleep=0.5)
            return await retry_get(pb.GetFileRequest(uri=device.uri, path=device_file))

    async def make_directory(self, device_path: str, parents: bool = False, timeout: int = 10):
        """Create missing directories on SNI device filesystem.

        If parents is not true, then an exception will propagate from gRPC if device_path
        cannot be created because it's parent (sub-)directories do not exist. When parents is
        true, all missing (sub-)directories will be created in the correct order.

        :param device_path: path to create on SNI device
        :param parents: when True, create any missing parent (sub-)directories for device_path
        :param timeout: seconds to try creating directories until timeout
        :raises SnirkIncapableError: when device does not have MakeDirectory capability
        """
        directories: list[str] = [device_path]
        if parents:
            parts = Path(device_path).parts
            directories = [str(Path(*parts[0:x])) for x in range(2, len(parts) + 1)]

        device = await self.find_device()
        await self.ensure_capability(pb.DeviceCapability.MakeDirectory)

        # find and create missing directories
        async with self.grpc_channel(timeout=timeout) as ch:
            stub = sni.DeviceFilesystemStub(ch)
            for directory in directories:
                try:
                    stub.ReadDirectory(pb.ReadDirectoryRequest(uri=device.uri, path=directory))
                except grpc._channel._InactiveRpcError:
                    retry_mkdir = await self.retry_grpc(stub.MakeDirectory)
                    await retry_mkdir(pb.MakeDirectoryRequest(uri=device.uri, path=directory))

    async def put_file(self, data: bytes, device_path: str, timeout: int = 30) -> pb.PutFileResponse:
        """Put file bytes at path on SNI device filesystem.

        :param data: bytes to write to device path
        :param device_path: path on device to write local_file bytes
        :param timeout: seconds until timeout writing file to device
        :raises SnirkIncapableError: when device does not have PutFile capability
        """
        device = await self.find_device()
        await self.ensure_capability(pb.DeviceCapability.PutFile)

        options = [
            ("grpc.max_message_length", self.max_message_length),
            ("grpc.max_send_message_length", self.max_message_length),
        ]
        async with self.grpc_channel(options=options, timeout=timeout) as ch:
            stub = sni.DeviceFilesystemStub(ch)
            retry_put = await self.retry_grpc(stub.PutFile, max_retries=3, sleep=0.5)
            response = await retry_put(pb.PutFileRequest(uri=device.uri, path=device_path, data=data))

        # note: appears that PutFileResponse.size is missing
        # might be SNI bug or could be gRPC proto error (it specifies size)
        return response

    async def read_directory(self, path: str, timeout: int = 2) -> pb.ReadDirectoryResponse:
        """Read directory from SNI device filesystem.

        :param path: directory path to read from device
        :param timeout: seconds until timeout reading directory from device
        :raises SnirkIncapableError: when device does not have ReadDirectory capability
        """
        device = await self.find_device()
        await self.ensure_capability(pb.DeviceCapability.ReadDirectory)

        async with self.grpc_channel() as ch:
            stub = sni.DeviceFilesystemStub(ch)
            retry = await self.retry_grpc(stub.ReadDirectory, timeout=timeout)
            try:
                response = await retry(pb.ReadDirectoryRequest(uri=device.uri, path=path))
            except grpc._channel._InactiveRpcError as ex:
                if "failed to list" not in str(ex):
                    raise
                # otherwise, could be because path is a single file, or because doesn't exist
                # if doesn't exist, let exception propagate up
                parent = str(Path(path).parent)
                response = await retry(pb.ReadDirectoryRequest(uri=device.uri, path=parent))
        return response

    async def remove_file(self, device_file: str, timeout: int = 5) -> pb.RemoveFileResponse:
        """Remove device file from SNI device filesystem.

        :param device_file: path to device file to remove
        :param timeout: seconds until timeout removing file from device
        :raises SnirkIncapableError: when device does not have RemoveFile capability
        """
        device = await self.find_device()
        await self.ensure_capability(pb.DeviceCapability.RemoveFile)

        async with self.grpc_channel(timeout=timeout) as ch:
            stub = sni.DeviceFilesystemStub(ch)
            retry_get = await self.retry_grpc(stub.RemoveFile, max_retries=3, sleep=0.5)
            return await retry_get(pb.RemoveFileRequest(uri=device.uri, path=device_file))
