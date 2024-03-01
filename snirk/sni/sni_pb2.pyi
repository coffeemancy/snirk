from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class AddressSpace(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FxPakPro: _ClassVar[AddressSpace]
    SnesABus: _ClassVar[AddressSpace]
    Raw: _ClassVar[AddressSpace]

class MemoryMapping(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Unknown: _ClassVar[MemoryMapping]
    HiROM: _ClassVar[MemoryMapping]
    LoROM: _ClassVar[MemoryMapping]
    ExHiROM: _ClassVar[MemoryMapping]
    SA1: _ClassVar[MemoryMapping]

class DeviceCapability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ReadMemory: _ClassVar[DeviceCapability]
    WriteMemory: _ClassVar[DeviceCapability]
    ExecuteASM: _ClassVar[DeviceCapability]
    ResetSystem: _ClassVar[DeviceCapability]
    PauseUnpauseEmulation: _ClassVar[DeviceCapability]
    PauseToggleEmulation: _ClassVar[DeviceCapability]
    ResetToMenu: _ClassVar[DeviceCapability]
    FetchFields: _ClassVar[DeviceCapability]
    ReadDirectory: _ClassVar[DeviceCapability]
    MakeDirectory: _ClassVar[DeviceCapability]
    RemoveFile: _ClassVar[DeviceCapability]
    RenameFile: _ClassVar[DeviceCapability]
    PutFile: _ClassVar[DeviceCapability]
    GetFile: _ClassVar[DeviceCapability]
    BootFile: _ClassVar[DeviceCapability]
    NWACommand: _ClassVar[DeviceCapability]

class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DeviceName: _ClassVar[Field]
    DeviceVersion: _ClassVar[Field]
    DeviceStatus: _ClassVar[Field]
    CoreName: _ClassVar[Field]
    CoreVersion: _ClassVar[Field]
    CorePlatform: _ClassVar[Field]
    RomFileName: _ClassVar[Field]
    RomHashType: _ClassVar[Field]
    RomHashValue: _ClassVar[Field]

class DirEntryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Directory: _ClassVar[DirEntryType]
    File: _ClassVar[DirEntryType]

FxPakPro: AddressSpace
SnesABus: AddressSpace
Raw: AddressSpace
Unknown: MemoryMapping
HiROM: MemoryMapping
LoROM: MemoryMapping
ExHiROM: MemoryMapping
SA1: MemoryMapping
ReadMemory: DeviceCapability
WriteMemory: DeviceCapability
ExecuteASM: DeviceCapability
ResetSystem: DeviceCapability
PauseUnpauseEmulation: DeviceCapability
PauseToggleEmulation: DeviceCapability
ResetToMenu: DeviceCapability
FetchFields: DeviceCapability
ReadDirectory: DeviceCapability
MakeDirectory: DeviceCapability
RemoveFile: DeviceCapability
RenameFile: DeviceCapability
PutFile: DeviceCapability
GetFile: DeviceCapability
BootFile: DeviceCapability
NWACommand: DeviceCapability
DeviceName: Field
DeviceVersion: Field
DeviceStatus: Field
CoreName: Field
CoreVersion: Field
CorePlatform: Field
RomFileName: Field
RomHashType: Field
RomHashValue: Field
Directory: DirEntryType
File: DirEntryType

class DevicesRequest(_message.Message):
    __slots__ = ("kinds",)
    KINDS_FIELD_NUMBER: _ClassVar[int]
    kinds: _containers.RepeatedScalarFieldContainer[str]

class DevicesResponse(_message.Message):
    __slots__ = ("devices",)

    class Device(_message.Message):
        __slots__ = ("uri", "displayName", "kind", "capabilities", "defaultAddressSpace", "system")
        URI_FIELD_NUMBER: _ClassVar[int]
        DISPLAYNAME_FIELD_NUMBER: _ClassVar[int]
        KIND_FIELD_NUMBER: _ClassVar[int]
        CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
        DEFAULTADDRESSSPACE_FIELD_NUMBER: _ClassVar[int]
        SYSTEM_FIELD_NUMBER: _ClassVar[int]
        uri: str
        displayName: str
        kind: str
        capabilities: _containers.RepeatedScalarFieldContainer[DeviceCapability]
        defaultAddressSpace: AddressSpace
        system: str

    DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[DevicesResponse.Device]

class ResetSystemRequest(_message.Message):
    __slots__ = ("uri",)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str

class ResetSystemResponse(_message.Message):
    __slots__ = ("uri",)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str

class ResetToMenuRequest(_message.Message):
    __slots__ = ("uri",)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str

class ResetToMenuResponse(_message.Message):
    __slots__ = ("uri",)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str

class PauseEmulationRequest(_message.Message):
    __slots__ = ("uri", "paused")
    URI_FIELD_NUMBER: _ClassVar[int]
    PAUSED_FIELD_NUMBER: _ClassVar[int]
    uri: str
    paused: bool

class PauseEmulationResponse(_message.Message):
    __slots__ = ("uri", "paused")
    URI_FIELD_NUMBER: _ClassVar[int]
    PAUSED_FIELD_NUMBER: _ClassVar[int]
    uri: str
    paused: bool

class PauseToggleEmulationRequest(_message.Message):
    __slots__ = ("uri",)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str

class PauseToggleEmulationResponse(_message.Message):
    __slots__ = ("uri",)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str

class DetectMemoryMappingRequest(_message.Message):
    __slots__ = ("uri", "fallbackMemoryMapping", "romHeader00FFB0")
    URI_FIELD_NUMBER: _ClassVar[int]
    FALLBACKMEMORYMAPPING_FIELD_NUMBER: _ClassVar[int]
    ROMHEADER00FFB0_FIELD_NUMBER: _ClassVar[int]
    uri: str
    fallbackMemoryMapping: MemoryMapping
    romHeader00FFB0: bytes

class DetectMemoryMappingResponse(_message.Message):
    __slots__ = ("uri", "memoryMapping", "confidence", "romHeader00FFB0")
    URI_FIELD_NUMBER: _ClassVar[int]
    MEMORYMAPPING_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    ROMHEADER00FFB0_FIELD_NUMBER: _ClassVar[int]
    uri: str
    memoryMapping: MemoryMapping
    confidence: bool
    romHeader00FFB0: bytes

class ReadMemoryRequest(_message.Message):
    __slots__ = ("requestAddress", "requestAddressSpace", "requestMemoryMapping", "size")
    REQUESTADDRESS_FIELD_NUMBER: _ClassVar[int]
    REQUESTADDRESSSPACE_FIELD_NUMBER: _ClassVar[int]
    REQUESTMEMORYMAPPING_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    requestAddress: int
    requestAddressSpace: AddressSpace
    requestMemoryMapping: MemoryMapping
    size: int

class ReadMemoryResponse(_message.Message):
    __slots__ = (
        "requestAddress",
        "requestAddressSpace",
        "requestMemoryMapping",
        "deviceAddress",
        "deviceAddressSpace",
        "data",
    )
    REQUESTADDRESS_FIELD_NUMBER: _ClassVar[int]
    REQUESTADDRESSSPACE_FIELD_NUMBER: _ClassVar[int]
    REQUESTMEMORYMAPPING_FIELD_NUMBER: _ClassVar[int]
    DEVICEADDRESS_FIELD_NUMBER: _ClassVar[int]
    DEVICEADDRESSSPACE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    requestAddress: int
    requestAddressSpace: AddressSpace
    requestMemoryMapping: MemoryMapping
    deviceAddress: int
    deviceAddressSpace: AddressSpace
    data: bytes

class WriteMemoryRequest(_message.Message):
    __slots__ = ("requestAddress", "requestAddressSpace", "requestMemoryMapping", "data")
    REQUESTADDRESS_FIELD_NUMBER: _ClassVar[int]
    REQUESTADDRESSSPACE_FIELD_NUMBER: _ClassVar[int]
    REQUESTMEMORYMAPPING_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    requestAddress: int
    requestAddressSpace: AddressSpace
    requestMemoryMapping: MemoryMapping
    data: bytes

class WriteMemoryResponse(_message.Message):
    __slots__ = (
        "requestAddress",
        "requestAddressSpace",
        "requestMemoryMapping",
        "deviceAddress",
        "deviceAddressSpace",
        "size",
    )
    REQUESTADDRESS_FIELD_NUMBER: _ClassVar[int]
    REQUESTADDRESSSPACE_FIELD_NUMBER: _ClassVar[int]
    REQUESTMEMORYMAPPING_FIELD_NUMBER: _ClassVar[int]
    DEVICEADDRESS_FIELD_NUMBER: _ClassVar[int]
    DEVICEADDRESSSPACE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    requestAddress: int
    requestAddressSpace: AddressSpace
    requestMemoryMapping: MemoryMapping
    deviceAddress: int
    deviceAddressSpace: AddressSpace
    size: int

class SingleReadMemoryRequest(_message.Message):
    __slots__ = ("uri", "request")
    URI_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    uri: str
    request: ReadMemoryRequest

class SingleReadMemoryResponse(_message.Message):
    __slots__ = ("uri", "response")
    URI_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    uri: str
    response: ReadMemoryResponse

class SingleWriteMemoryRequest(_message.Message):
    __slots__ = ("uri", "request")
    URI_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    uri: str
    request: WriteMemoryRequest

class SingleWriteMemoryResponse(_message.Message):
    __slots__ = ("uri", "response")
    URI_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    uri: str
    response: WriteMemoryResponse

class MultiReadMemoryRequest(_message.Message):
    __slots__ = ("uri", "requests")
    URI_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    uri: str
    requests: _containers.RepeatedCompositeFieldContainer[ReadMemoryRequest]

class MultiReadMemoryResponse(_message.Message):
    __slots__ = ("uri", "responses")
    URI_FIELD_NUMBER: _ClassVar[int]
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    uri: str
    responses: _containers.RepeatedCompositeFieldContainer[ReadMemoryResponse]

class MultiWriteMemoryRequest(_message.Message):
    __slots__ = ("uri", "requests")
    URI_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    uri: str
    requests: _containers.RepeatedCompositeFieldContainer[WriteMemoryRequest]

class MultiWriteMemoryResponse(_message.Message):
    __slots__ = ("uri", "responses")
    URI_FIELD_NUMBER: _ClassVar[int]
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    uri: str
    responses: _containers.RepeatedCompositeFieldContainer[WriteMemoryResponse]

class ReadDirectoryRequest(_message.Message):
    __slots__ = ("uri", "path")
    URI_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    uri: str
    path: str

class DirEntry(_message.Message):
    __slots__ = ("name", "type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: DirEntryType

class ReadDirectoryResponse(_message.Message):
    __slots__ = ("uri", "path", "entries")
    URI_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    uri: str
    path: str
    entries: _containers.RepeatedCompositeFieldContainer[DirEntry]

class MakeDirectoryRequest(_message.Message):
    __slots__ = ("uri", "path")
    URI_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    uri: str
    path: str

class MakeDirectoryResponse(_message.Message):
    __slots__ = ("uri", "path")
    URI_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    uri: str
    path: str

class RemoveFileRequest(_message.Message):
    __slots__ = ("uri", "path")
    URI_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    uri: str
    path: str

class RemoveFileResponse(_message.Message):
    __slots__ = ("uri", "path")
    URI_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    uri: str
    path: str

class RenameFileRequest(_message.Message):
    __slots__ = ("uri", "path", "newFilename")
    URI_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    NEWFILENAME_FIELD_NUMBER: _ClassVar[int]
    uri: str
    path: str
    newFilename: str

class RenameFileResponse(_message.Message):
    __slots__ = ("uri", "path", "newFilename")
    URI_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    NEWFILENAME_FIELD_NUMBER: _ClassVar[int]
    uri: str
    path: str
    newFilename: str

class PutFileRequest(_message.Message):
    __slots__ = ("uri", "path", "data")
    URI_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    uri: str
    path: str
    data: bytes

class PutFileResponse(_message.Message):
    __slots__ = ("uri", "path", "size")
    URI_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    uri: str
    path: str
    size: int

class GetFileRequest(_message.Message):
    __slots__ = ("uri", "path")
    URI_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    uri: str
    path: str

class GetFileResponse(_message.Message):
    __slots__ = ("uri", "path", "size", "data")
    URI_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    uri: str
    path: str
    size: int
    data: bytes

class BootFileRequest(_message.Message):
    __slots__ = ("uri", "path")
    URI_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    uri: str
    path: str

class BootFileResponse(_message.Message):
    __slots__ = ("uri", "path")
    URI_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    uri: str
    path: str

class FieldsRequest(_message.Message):
    __slots__ = ("uri", "fields")
    URI_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    uri: str
    fields: _containers.RepeatedScalarFieldContainer[Field]

class FieldsResponse(_message.Message):
    __slots__ = ("uri", "fields", "values")
    URI_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    uri: str
    fields: _containers.RepeatedScalarFieldContainer[Field]
    values: _containers.RepeatedScalarFieldContainer[str]

class NWACommandRequest(_message.Message):
    __slots__ = ("uri", "command", "args", "binaryArg")
    URI_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    BINARYARG_FIELD_NUMBER: _ClassVar[int]
    uri: str
    command: str
    args: str
    binaryArg: bytes

class NWACommandResponse(_message.Message):
    __slots__ = ("uri", "asciiReply", "binaryReplay")

    class NWAASCIIItem(_message.Message):
        __slots__ = ("item",)

        class ItemEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

        ITEM_FIELD_NUMBER: _ClassVar[int]
        item: _containers.ScalarMap[str, str]

    URI_FIELD_NUMBER: _ClassVar[int]
    ASCIIREPLY_FIELD_NUMBER: _ClassVar[int]
    BINARYREPLAY_FIELD_NUMBER: _ClassVar[int]
    uri: str
    asciiReply: _containers.RepeatedCompositeFieldContainer[NWACommandResponse.NWAASCIIItem]
    binaryReplay: bytes
