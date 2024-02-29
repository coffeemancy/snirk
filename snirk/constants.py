from typing import Final

from snirk.sni import sni_pb2 as pb


class SnirkConstants:
    """Container for useful constants."""

    # mapping of device capability ints to string representations
    CAPABILITY_LOOKUP: Final[dict[pb.DeviceCapability, str]] = {
        pb.DeviceCapability.ReadMemory: "ReadMemory",
        pb.DeviceCapability.WriteMemory: "WriteMemory",
        pb.DeviceCapability.ExecuteASM: "ExecuteASM",
        pb.DeviceCapability.ResetSystem: "ResetSystem",
        pb.DeviceCapability.PauseUnpauseEmulation: "PauseUnpauseEmulation",
        pb.DeviceCapability.PauseToggleEmulation: "PauseToggleEmulation",
        pb.DeviceCapability.ResetToMenu: "ResetToMenu",
        pb.DeviceCapability.FetchFields: "FetchFields",
        pb.DeviceCapability.ReadDirectory: "ReadDirectory",
        pb.DeviceCapability.MakeDirectory: "MakeDirectory",
        pb.DeviceCapability.RemoveFile: "RemoveFile",
        pb.DeviceCapability.RenameFile: "RenameFile",
        pb.DeviceCapability.PutFile: "PutFile",
        pb.DeviceCapability.GetFile: "GetFile",
        pb.DeviceCapability.BootFile: "BootFile",
        pb.DeviceCapability.NWACommand: "NWACommand",
    }
