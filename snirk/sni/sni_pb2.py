# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sni/sni.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\rsni/sni.proto"\x1f\n\x0e\x44\x65vicesRequest\x12\r\n\x05kinds\x18\x01'
    b' \x03(\t"\xdf\x01\n\x0f\x44\x65vicesResponse\x12(\n\x07\x64\x65vices\x18\x01'
    b" \x03(\x0b\x32\x17.DevicesResponse.Device\x1a\xa1\x01\n\x06\x44\x65vice\x12\x0b\n\x03uri\x18\x01"
    b" \x01(\t\x12\x13\n\x0b\x64isplayName\x18\x02 \x01(\t\x12\x0c\n\x04kind\x18\x03"
    b" \x01(\t\x12'\n\x0c\x63\x61pabilities\x18\x04"
    b" \x03(\x0e\x32\x11.DeviceCapability\x12*\n\x13\x64\x65\x66\x61ultAddressSpace\x18\x05"
    b" \x01(\x0e\x32\r.AddressSpace\x12\x12\n\x06system\x18\x06"
    b' \x01(\tB\x02\x18\x01"!\n\x12ResetSystemRequest\x12\x0b\n\x03uri\x18\x01'
    b' \x01(\t""\n\x13ResetSystemResponse\x12\x0b\n\x03uri\x18\x01'
    b' \x01(\t"!\n\x12ResetToMenuRequest\x12\x0b\n\x03uri\x18\x01'
    b' \x01(\t""\n\x13ResetToMenuResponse\x12\x0b\n\x03uri\x18\x01'
    b' \x01(\t"4\n\x15PauseEmulationRequest\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0e\n\x06paused\x18\x02'
    b' \x01(\x08"5\n\x16PauseEmulationResponse\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0e\n\x06paused\x18\x02'
    b' \x01(\x08"*\n\x1bPauseToggleEmulationRequest\x12\x0b\n\x03uri\x18\x01'
    b' \x01(\t"+\n\x1cPauseToggleEmulationResponse\x12\x0b\n\x03uri\x18\x01'
    b' \x01(\t"\xa9\x01\n\x1a\x44\x65tectMemoryMappingRequest\x12\x0b\n\x03uri\x18\x01'
    b" \x01(\t\x12\x32\n\x15\x66\x61llbackMemoryMapping\x18\x02"
    b" \x01(\x0e\x32\x0e.MemoryMappingH\x00\x88\x01\x01\x12\x1c\n\x0fromHeader00FFB0\x18\x03"
    b' \x01(\x0cH\x01\x88\x01\x01\x42\x18\n\x16_fallbackMemoryMappingB\x12\n\x10_romHeader00FFB0"~\n\x1b\x44\x65tectMemoryMappingResponse\x12\x0b\n\x03uri\x18\x01'
    b" \x01(\t\x12%\n\rmemoryMapping\x18\x02 \x01(\x0e\x32\x0e.MemoryMapping\x12\x12\n\nconfidence\x18\x03"
    b" \x01(\x08\x12\x17\n\x0fromHeader00FFB0\x18\x04"
    b' \x01(\x0c"\x93\x01\n\x11ReadMemoryRequest\x12\x16\n\x0erequestAddress\x18\x01'
    b" \x01(\r\x12*\n\x13requestAddressSpace\x18\x02"
    b" \x01(\x0e\x32\r.AddressSpace\x12,\n\x14requestMemoryMapping\x18\x04"
    b" \x01(\x0e\x32\x0e.MemoryMapping\x12\x0c\n\x04size\x18\x03"
    b' \x01(\r"\xd6\x01\n\x12ReadMemoryResponse\x12\x16\n\x0erequestAddress\x18\x01'
    b" \x01(\r\x12*\n\x13requestAddressSpace\x18\x02"
    b" \x01(\x0e\x32\r.AddressSpace\x12,\n\x14requestMemoryMapping\x18\x06"
    b" \x01(\x0e\x32\x0e.MemoryMapping\x12\x15\n\rdeviceAddress\x18\x03"
    b" \x01(\r\x12)\n\x12\x64\x65viceAddressSpace\x18\x04 \x01(\x0e\x32\r.AddressSpace\x12\x0c\n\x04\x64\x61ta\x18\x05"
    b' \x01(\x0c"\x94\x01\n\x12WriteMemoryRequest\x12\x16\n\x0erequestAddress\x18\x01'
    b" \x01(\r\x12*\n\x13requestAddressSpace\x18\x02"
    b" \x01(\x0e\x32\r.AddressSpace\x12,\n\x14requestMemoryMapping\x18\x04"
    b" \x01(\x0e\x32\x0e.MemoryMapping\x12\x0c\n\x04\x64\x61ta\x18\x03"
    b' \x01(\x0c"\xd7\x01\n\x13WriteMemoryResponse\x12\x16\n\x0erequestAddress\x18\x01'
    b" \x01(\r\x12*\n\x13requestAddressSpace\x18\x02"
    b" \x01(\x0e\x32\r.AddressSpace\x12,\n\x14requestMemoryMapping\x18\x06"
    b" \x01(\x0e\x32\x0e.MemoryMapping\x12\x15\n\rdeviceAddress\x18\x03"
    b" \x01(\r\x12)\n\x12\x64\x65viceAddressSpace\x18\x04 \x01(\x0e\x32\r.AddressSpace\x12\x0c\n\x04size\x18\x05"
    b' \x01(\r"K\n\x17SingleReadMemoryRequest\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12#\n\x07request\x18\x02'
    b' \x01(\x0b\x32\x12.ReadMemoryRequest"N\n\x18SingleReadMemoryResponse\x12\x0b\n\x03uri\x18\x01'
    b" \x01(\t\x12%\n\x08response\x18\x02"
    b' \x01(\x0b\x32\x13.ReadMemoryResponse"M\n\x18SingleWriteMemoryRequest\x12\x0b\n\x03uri\x18\x01'
    b" \x01(\t\x12$\n\x07request\x18\x02"
    b' \x01(\x0b\x32\x13.WriteMemoryRequest"P\n\x19SingleWriteMemoryResponse\x12\x0b\n\x03uri\x18\x01'
    b" \x01(\t\x12&\n\x08response\x18\x02"
    b' \x01(\x0b\x32\x14.WriteMemoryResponse"K\n\x16MultiReadMemoryRequest\x12\x0b\n\x03uri\x18\x01'
    b" \x01(\t\x12$\n\x08requests\x18\x02"
    b' \x03(\x0b\x32\x12.ReadMemoryRequest"N\n\x17MultiReadMemoryResponse\x12\x0b\n\x03uri\x18\x01'
    b" \x01(\t\x12&\n\tresponses\x18\x02"
    b' \x03(\x0b\x32\x13.ReadMemoryResponse"M\n\x17MultiWriteMemoryRequest\x12\x0b\n\x03uri\x18\x01'
    b" \x01(\t\x12%\n\x08requests\x18\x02"
    b' \x03(\x0b\x32\x13.WriteMemoryRequest"P\n\x18MultiWriteMemoryResponse\x12\x0b\n\x03uri\x18\x01'
    b" \x01(\t\x12'\n\tresponses\x18\x02"
    b' \x03(\x0b\x32\x14.WriteMemoryResponse"1\n\x14ReadDirectoryRequest\x12\x0b\n\x03uri\x18\x01'
    b' \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t"5\n\x08\x44irEntry\x12\x0c\n\x04name\x18\x01'
    b" \x01(\t\x12\x1b\n\x04type\x18\x02"
    b' \x01(\x0e\x32\r.DirEntryType"N\n\x15ReadDirectoryResponse\x12\x0b\n\x03uri\x18\x01'
    b" \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x1a\n\x07\x65ntries\x18\x03"
    b' \x03(\x0b\x32\t.DirEntry"1\n\x14MakeDirectoryRequest\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02'
    b' \x01(\t"2\n\x15MakeDirectoryResponse\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02'
    b' \x01(\t".\n\x11RemoveFileRequest\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02'
    b' \x01(\t"/\n\x12RemoveFileResponse\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02'
    b' \x01(\t"C\n\x11RenameFileRequest\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02'
    b' \x01(\t\x12\x13\n\x0bnewFilename\x18\x03 \x01(\t"D\n\x12RenameFileResponse\x12\x0b\n\x03uri\x18\x01'
    b" \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x13\n\x0bnewFilename\x18\x03"
    b' \x01(\t"9\n\x0ePutFileRequest\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02'
    b' \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c":\n\x0fPutFileResponse\x12\x0b\n\x03uri\x18\x01'
    b" \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0c\n\x04size\x18\x03"
    b' \x01(\r"+\n\x0eGetFileRequest\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02'
    b' \x01(\t"H\n\x0fGetFileResponse\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02'
    b" \x01(\t\x12\x0c\n\x04size\x18\x03 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x04"
    b' \x01(\x0c",\n\x0f\x42ootFileRequest\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02'
    b' \x01(\t"-\n\x10\x42ootFileResponse\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02'
    b' \x01(\t"4\n\rFieldsRequest\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x16\n\x06\x66ields\x18\x02'
    b' \x03(\x0e\x32\x06.Field"E\n\x0e\x46ieldsResponse\x12\x0b\n\x03uri\x18\x01'
    b" \x01(\t\x12\x16\n\x06\x66ields\x18\x02 \x03(\x0e\x32\x06.Field\x12\x0e\n\x06values\x18\x03"
    b' \x03(\t"e\n\x11NWACommandRequest\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x02'
    b" \x01(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x01(\t\x12\x16\n\tbinaryArg\x18\x04"
    b' \x01(\x0cH\x00\x88\x01\x01\x42\x0c\n\n_binaryArg"\xfa\x01\n\x12NWACommandResponse\x12\x0b\n\x03uri\x18\x01'
    b" \x01(\t\x12\x34\n\nasciiReply\x18\x02 \x03(\x0b\x32"
    b" .NWACommandResponse.NWAASCIIItem\x12\x19\n\x0c\x62inaryReplay\x18\x03"
    b" \x01(\x0cH\x00\x88\x01\x01\x1au\n\x0cNWAASCIIItem\x12\x38\n\x04item\x18\x01"
    b" \x03(\x0b\x32*.NWACommandResponse.NWAASCIIItem.ItemEntry\x1a+\n\tItemEntry\x12\x0b\n\x03key\x18\x01"
    b" \x01(\t\x12\r\n\x05value\x18\x02"
    b' \x01(\t:\x02\x38\x01\x42\x0f\n\r_binaryReplay*3\n\x0c\x41\x64\x64ressSpace\x12\x0c\n\x08\x46xPakPro\x10\x00\x12\x0c\n\x08SnesABus\x10\x01\x12\x07\n\x03Raw\x10\x02*H\n\rMemoryMapping\x12\x0b\n\x07Unknown\x10\x00\x12\t\n\x05HiROM\x10\x01\x12\t\n\x05LoROM\x10\x02\x12\x0b\n\x07\x45xHiROM\x10\x03\x12\x07\n\x03SA1\x10\x04*\xb3\x02\n\x10\x44\x65viceCapability\x12\x08\n\x04None\x10\x00\x12\x0e\n\nReadMemory\x10\x01\x12\x0f\n\x0bWriteMemory\x10\x02\x12\x0e\n\nExecuteASM\x10\x03\x12\x0f\n\x0bResetSystem\x10\x04\x12\x19\n\x15PauseUnpauseEmulation\x10\x05\x12\x18\n\x14PauseToggleEmulation\x10\x06\x12\x0f\n\x0bResetToMenu\x10\x07\x12\x0f\n\x0b\x46\x65tchFields\x10\x08\x12\x11\n\rReadDirectory\x10\n\x12\x11\n\rMakeDirectory\x10\x0b\x12\x0e\n\nRemoveFile\x10\x0c\x12\x0e\n\nRenameFile\x10\r\x12\x0b\n\x07PutFile\x10\x0e\x12\x0b\n\x07GetFile\x10\x0f\x12\x0c\n\x08\x42ootFile\x10\x10\x12\x0e\n\nNWACommand\x10\x14*\xa1\x01\n\x05\x46ield\x12\x0e\n\nDeviceName\x10\x00\x12\x11\n\rDeviceVersion\x10\x01\x12\x10\n\x0c\x44\x65viceStatus\x10\x02\x12\x0c\n\x08\x43oreName\x10\x14\x12\x0f\n\x0b\x43oreVersion\x10\x15\x12\x10\n\x0c\x43orePlatform\x10\x16\x12\x0f\n\x0bRomFileName\x10(\x12\x0f\n\x0bRomHashType\x10)\x12\x10\n\x0cRomHashValue\x10**\'\n\x0c\x44irEntryType\x12\r\n\tDirectory\x10\x00\x12\x08\n\x04\x46ile\x10\x01\x32=\n\x07\x44\x65vices\x12\x32\n\x0bListDevices\x12\x0f.DevicesRequest\x1a\x10.DevicesResponse"\x00\x32\xaa\x02\n\rDeviceControl\x12:\n\x0bResetSystem\x12\x13.ResetSystemRequest\x1a\x14.ResetSystemResponse"\x00\x12:\n\x0bResetToMenu\x12\x13.ResetToMenuRequest\x1a\x14.ResetToMenuResponse"\x00\x12J\n\x15PauseUnpauseEmulation\x12\x16.PauseEmulationRequest\x1a\x17.PauseEmulationResponse"\x00\x12U\n\x14PauseToggleEmulation\x12\x1c.PauseToggleEmulationRequest\x1a\x1d.PauseToggleEmulationResponse"\x00\x32\x81\x04\n\x0c\x44\x65viceMemory\x12L\n\rMappingDetect\x12\x1b.DetectMemoryMappingRequest\x1a\x1c.DetectMemoryMappingResponse"\x00\x12\x43\n\nSingleRead\x12\x18.SingleReadMemoryRequest\x1a\x19.SingleReadMemoryResponse"\x00\x12\x46\n\x0bSingleWrite\x12\x19.SingleWriteMemoryRequest\x1a\x1a.SingleWriteMemoryResponse"\x00\x12@\n\tMultiRead\x12\x17.MultiReadMemoryRequest\x1a\x18.MultiReadMemoryResponse"\x00\x12\x43\n\nMultiWrite\x12\x18.MultiWriteMemoryRequest\x1a\x19.MultiWriteMemoryResponse"\x00\x12\x45\n\nStreamRead\x12\x17.MultiReadMemoryRequest\x1a\x18.MultiReadMemoryResponse"\x00(\x01\x30\x01\x12H\n\x0bStreamWrite\x12\x18.MultiWriteMemoryRequest\x1a\x19.MultiWriteMemoryResponse"\x00(\x01\x30\x01\x32\x9b\x03\n\x10\x44\x65viceFilesystem\x12@\n\rReadDirectory\x12\x15.ReadDirectoryRequest\x1a\x16.ReadDirectoryResponse"\x00\x12@\n\rMakeDirectory\x12\x15.MakeDirectoryRequest\x1a\x16.MakeDirectoryResponse"\x00\x12\x37\n\nRemoveFile\x12\x12.RemoveFileRequest\x1a\x13.RemoveFileResponse"\x00\x12\x37\n\nRenameFile\x12\x12.RenameFileRequest\x1a\x13.RenameFileResponse"\x00\x12.\n\x07PutFile\x12\x0f.PutFileRequest\x1a\x10.PutFileResponse"\x00\x12.\n\x07GetFile\x12\x0f.GetFileRequest\x1a\x10.GetFileResponse"\x00\x12\x31\n\x08\x42ootFile\x12\x10.BootFileRequest\x1a\x11.BootFileResponse"\x00\x32>\n\nDeviceInfo\x12\x30\n\x0b\x46\x65tchFields\x12\x0e.FieldsRequest\x1a\x0f.FieldsResponse"\x00\x32\x44\n\tDeviceNWA\x12\x37\n\nNWACommand\x12\x12.NWACommandRequest\x1a\x13.NWACommandResponse"\x00\x42?\n\x15\x63om.github.alttpo.sniZ'
    b" github.com/alttpo/sni/protos/sni\xaa\x02\x03SNIb\x06proto3"
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "sni.sni_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS is False:
    _globals["DESCRIPTOR"]._options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b"\n\025com.github.alttpo.sniZ github.com/alttpo/sni/protos/sni\252\002\003SNI"
    )
    _globals["_DEVICESRESPONSE_DEVICE"].fields_by_name["system"]._options = None
    _globals["_DEVICESRESPONSE_DEVICE"].fields_by_name["system"]._serialized_options = b"\030\001"
    _globals["_NWACOMMANDRESPONSE_NWAASCIIITEM_ITEMENTRY"]._options = None
    _globals["_NWACOMMANDRESPONSE_NWAASCIIITEM_ITEMENTRY"]._serialized_options = b"8\001"
    _globals["_ADDRESSSPACE"]._serialized_start = 3625
    _globals["_ADDRESSSPACE"]._serialized_end = 3676
    _globals["_MEMORYMAPPING"]._serialized_start = 3678
    _globals["_MEMORYMAPPING"]._serialized_end = 3750
    _globals["_DEVICECAPABILITY"]._serialized_start = 3753
    _globals["_DEVICECAPABILITY"]._serialized_end = 4060
    _globals["_FIELD"]._serialized_start = 4063
    _globals["_FIELD"]._serialized_end = 4224
    _globals["_DIRENTRYTYPE"]._serialized_start = 4226
    _globals["_DIRENTRYTYPE"]._serialized_end = 4265
    _globals["_DEVICESREQUEST"]._serialized_start = 17
    _globals["_DEVICESREQUEST"]._serialized_end = 48
    _globals["_DEVICESRESPONSE"]._serialized_start = 51
    _globals["_DEVICESRESPONSE"]._serialized_end = 274
    _globals["_DEVICESRESPONSE_DEVICE"]._serialized_start = 113
    _globals["_DEVICESRESPONSE_DEVICE"]._serialized_end = 274
    _globals["_RESETSYSTEMREQUEST"]._serialized_start = 276
    _globals["_RESETSYSTEMREQUEST"]._serialized_end = 309
    _globals["_RESETSYSTEMRESPONSE"]._serialized_start = 311
    _globals["_RESETSYSTEMRESPONSE"]._serialized_end = 345
    _globals["_RESETTOMENUREQUEST"]._serialized_start = 347
    _globals["_RESETTOMENUREQUEST"]._serialized_end = 380
    _globals["_RESETTOMENURESPONSE"]._serialized_start = 382
    _globals["_RESETTOMENURESPONSE"]._serialized_end = 416
    _globals["_PAUSEEMULATIONREQUEST"]._serialized_start = 418
    _globals["_PAUSEEMULATIONREQUEST"]._serialized_end = 470
    _globals["_PAUSEEMULATIONRESPONSE"]._serialized_start = 472
    _globals["_PAUSEEMULATIONRESPONSE"]._serialized_end = 525
    _globals["_PAUSETOGGLEEMULATIONREQUEST"]._serialized_start = 527
    _globals["_PAUSETOGGLEEMULATIONREQUEST"]._serialized_end = 569
    _globals["_PAUSETOGGLEEMULATIONRESPONSE"]._serialized_start = 571
    _globals["_PAUSETOGGLEEMULATIONRESPONSE"]._serialized_end = 614
    _globals["_DETECTMEMORYMAPPINGREQUEST"]._serialized_start = 617
    _globals["_DETECTMEMORYMAPPINGREQUEST"]._serialized_end = 786
    _globals["_DETECTMEMORYMAPPINGRESPONSE"]._serialized_start = 788
    _globals["_DETECTMEMORYMAPPINGRESPONSE"]._serialized_end = 914
    _globals["_READMEMORYREQUEST"]._serialized_start = 917
    _globals["_READMEMORYREQUEST"]._serialized_end = 1064
    _globals["_READMEMORYRESPONSE"]._serialized_start = 1067
    _globals["_READMEMORYRESPONSE"]._serialized_end = 1281
    _globals["_WRITEMEMORYREQUEST"]._serialized_start = 1284
    _globals["_WRITEMEMORYREQUEST"]._serialized_end = 1432
    _globals["_WRITEMEMORYRESPONSE"]._serialized_start = 1435
    _globals["_WRITEMEMORYRESPONSE"]._serialized_end = 1650
    _globals["_SINGLEREADMEMORYREQUEST"]._serialized_start = 1652
    _globals["_SINGLEREADMEMORYREQUEST"]._serialized_end = 1727
    _globals["_SINGLEREADMEMORYRESPONSE"]._serialized_start = 1729
    _globals["_SINGLEREADMEMORYRESPONSE"]._serialized_end = 1807
    _globals["_SINGLEWRITEMEMORYREQUEST"]._serialized_start = 1809
    _globals["_SINGLEWRITEMEMORYREQUEST"]._serialized_end = 1886
    _globals["_SINGLEWRITEMEMORYRESPONSE"]._serialized_start = 1888
    _globals["_SINGLEWRITEMEMORYRESPONSE"]._serialized_end = 1968
    _globals["_MULTIREADMEMORYREQUEST"]._serialized_start = 1970
    _globals["_MULTIREADMEMORYREQUEST"]._serialized_end = 2045
    _globals["_MULTIREADMEMORYRESPONSE"]._serialized_start = 2047
    _globals["_MULTIREADMEMORYRESPONSE"]._serialized_end = 2125
    _globals["_MULTIWRITEMEMORYREQUEST"]._serialized_start = 2127
    _globals["_MULTIWRITEMEMORYREQUEST"]._serialized_end = 2204
    _globals["_MULTIWRITEMEMORYRESPONSE"]._serialized_start = 2206
    _globals["_MULTIWRITEMEMORYRESPONSE"]._serialized_end = 2286
    _globals["_READDIRECTORYREQUEST"]._serialized_start = 2288
    _globals["_READDIRECTORYREQUEST"]._serialized_end = 2337
    _globals["_DIRENTRY"]._serialized_start = 2339
    _globals["_DIRENTRY"]._serialized_end = 2392
    _globals["_READDIRECTORYRESPONSE"]._serialized_start = 2394
    _globals["_READDIRECTORYRESPONSE"]._serialized_end = 2472
    _globals["_MAKEDIRECTORYREQUEST"]._serialized_start = 2474
    _globals["_MAKEDIRECTORYREQUEST"]._serialized_end = 2523
    _globals["_MAKEDIRECTORYRESPONSE"]._serialized_start = 2525
    _globals["_MAKEDIRECTORYRESPONSE"]._serialized_end = 2575
    _globals["_REMOVEFILEREQUEST"]._serialized_start = 2577
    _globals["_REMOVEFILEREQUEST"]._serialized_end = 2623
    _globals["_REMOVEFILERESPONSE"]._serialized_start = 2625
    _globals["_REMOVEFILERESPONSE"]._serialized_end = 2672
    _globals["_RENAMEFILEREQUEST"]._serialized_start = 2674
    _globals["_RENAMEFILEREQUEST"]._serialized_end = 2741
    _globals["_RENAMEFILERESPONSE"]._serialized_start = 2743
    _globals["_RENAMEFILERESPONSE"]._serialized_end = 2811
    _globals["_PUTFILEREQUEST"]._serialized_start = 2813
    _globals["_PUTFILEREQUEST"]._serialized_end = 2870
    _globals["_PUTFILERESPONSE"]._serialized_start = 2872
    _globals["_PUTFILERESPONSE"]._serialized_end = 2930
    _globals["_GETFILEREQUEST"]._serialized_start = 2932
    _globals["_GETFILEREQUEST"]._serialized_end = 2975
    _globals["_GETFILERESPONSE"]._serialized_start = 2977
    _globals["_GETFILERESPONSE"]._serialized_end = 3049
    _globals["_BOOTFILEREQUEST"]._serialized_start = 3051
    _globals["_BOOTFILEREQUEST"]._serialized_end = 3095
    _globals["_BOOTFILERESPONSE"]._serialized_start = 3097
    _globals["_BOOTFILERESPONSE"]._serialized_end = 3142
    _globals["_FIELDSREQUEST"]._serialized_start = 3144
    _globals["_FIELDSREQUEST"]._serialized_end = 3196
    _globals["_FIELDSRESPONSE"]._serialized_start = 3198
    _globals["_FIELDSRESPONSE"]._serialized_end = 3267
    _globals["_NWACOMMANDREQUEST"]._serialized_start = 3269
    _globals["_NWACOMMANDREQUEST"]._serialized_end = 3370
    _globals["_NWACOMMANDRESPONSE"]._serialized_start = 3373
    _globals["_NWACOMMANDRESPONSE"]._serialized_end = 3623
    _globals["_NWACOMMANDRESPONSE_NWAASCIIITEM"]._serialized_start = 3489
    _globals["_NWACOMMANDRESPONSE_NWAASCIIITEM"]._serialized_end = 3606
    _globals["_NWACOMMANDRESPONSE_NWAASCIIITEM_ITEMENTRY"]._serialized_start = 3563
    _globals["_NWACOMMANDRESPONSE_NWAASCIIITEM_ITEMENTRY"]._serialized_end = 3606
    _globals["_DEVICES"]._serialized_start = 4267
    _globals["_DEVICES"]._serialized_end = 4328
    _globals["_DEVICECONTROL"]._serialized_start = 4331
    _globals["_DEVICECONTROL"]._serialized_end = 4629
    _globals["_DEVICEMEMORY"]._serialized_start = 4632
    _globals["_DEVICEMEMORY"]._serialized_end = 5145
    _globals["_DEVICEFILESYSTEM"]._serialized_start = 5148
    _globals["_DEVICEFILESYSTEM"]._serialized_end = 5559
    _globals["_DEVICEINFO"]._serialized_start = 5561
    _globals["_DEVICEINFO"]._serialized_end = 5623
    _globals["_DEVICENWA"]._serialized_start = 5625
    _globals["_DEVICENWA"]._serialized_end = 5693
# @@protoc_insertion_point(module_scope)