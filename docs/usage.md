# Snirk Usage and Examples

This doc demonstrates examples for using the snirk library in an application.

The primary means of interaction is through an instance of a [`Snirk`][Snirk] object, which
manages interaction to a single SNI device (per instance).

## Connecting to SNI devices with Snirk

Below code snippet instantiates a [`Snirk`][Snirk] object:

```python
from snirk import Snirk

snirk = Snirk()
```

!!! note

    By default, this uses an SNI server found at `localhost:8191`. If SNI is running on a different host
    or port, that channel can be specified at instantiation.

### AsyncIO Overview

Snirk uses [`asyncio`][asyncio] for asynchronous communication to SNI devices (e.g. using `async`/`await`).

This means that most methods on a [`Snirk`][Snirk] object return [awaitables][awaitables] (e.g. coroutines),
instead of actual results. For example, running `.find_device` returns a coroutine object:

```raw
>>> snirk.find_device()
<coroutine object Snirk.find_device at 0x74dc0c78a6b0>
```

This fits well with writing asynchronous applications, but for use in a REPL or synchronous applications
(e.g. building CLI tools using Snirk), the [`asyncio.run`][asyncio.run] method can be used to wait for results
(or timeout).

Many of the below examples use `asyncio.run` in this way.

### Listing all connected devices

!!! note

    In the below examples, two SNI devices are connected (FxPak Pro and Retroarch). Your actual devices
    will differ [depending on device, platform, and random assignment](
    https://github.com/alttpo/sni?tab=readme-ov-file#device-uris).

This object can then be used to list all connected devices ([`Snirk.list_devices`][Snirk.list_devices]):

```raw
>>> asyncio.run(snirk.list_devices())
[uri: "fxpakpro://./dev/ttyACM4"
displayName: "/dev/ttyACM4 (1209:5a22)"
kind: "fxpakpro"
capabilities: ReadMemory
capabilities: WriteMemory
capabilities: ResetSystem
capabilities: ResetToMenu
capabilities: ExecuteASM
capabilities: FetchFields
capabilities: ReadDirectory
capabilities: MakeDirectory
capabilities: RemoveFile
capabilities: RenameFile
capabilities: PutFile
capabilities: GetFile
capabilities: BootFile
, uri: "ra://127.0.0.1:55355"
displayName: "RetroArch v1.16.0 (127.0.0.1:55355)"
kind: "retroarch"
capabilities: ReadMemory
capabilities: WriteMemory
capabilities: ResetSystem
capabilities: PauseToggleEmulation
capabilities: FetchFields
defaultAddressSpace: SnesABus
]
```

In the above, details for each device are shown, including the `uri`, `kind` (e.g. "fxpakpro", "retroarch"),
and certain [capabilities][sni-capabilities].

### Selecting a device

The [`Snirk.find_device`][Snirk.find_device] method can be used to find and select a SNI device. The selected
device is cached and used for all subsequent operations with the `Snirk` object.

When multiple devices are connected, the selected device is determined by below:

* If `kind` is specified, filter all devices to only select from devices matching that kind (e.g. "retroarch")
* If `uri` is specified, select the matching device (if it is detected)
* Otherwise, choose the first matching device (which is not necessarily deterministic)

Extending our example above, where two devices (FxPak Pro and Retroarch) are connected, we specify using one
device (the FxPak Pro) with `kind`:

```raw
>>> asyncio.run(snirk.find_device(kind="fxpakpro"))
uri: "fxpakpro://./dev/ttyACM4"
displayName: "/dev/ttyACM4 (1209:5a22)"
kind: "fxpakpro"
capabilities: ReadMemory
capabilities: WriteMemory
capabilities: ResetSystem
capabilities: ResetToMenu
capabilities: ExecuteASM
capabilities: FetchFields
capabilities: ReadDirectory
capabilities: MakeDirectory
capabilities: RemoveFile
capabilities: RenameFile
capabilities: PutFile
capabilities: GetFile
capabilities: BootFile
```

Subsequent calls to `.find_device` will use the value from the cache, unless:

* The `force` parameter is set
* The `kind` or `uri` parameters are used and do not match the currently-cached device

Additionally, the [`Snirk.device`][Snirk.device] property can be used (it performs `asyncio.run` itself):

```raw
>>> snirk.device.uri
'fxpakpro://./dev/ttyACM4'
```

!!! note

    The `kind` or `uri` cannot be specified on the `.device` property, so if a device has not already been
    cached from a previous call to `.find_device` then it will just use the first device found.

## Reading and using memory data from SNI devices

### AddressEnum and MemData

The [`AddressEnum`][AddressEnum] and [`MemData`][MemData] classes are intended
to allow easily translating memory data gRPC responses read over SNI from a game/ROM to named attributes for lookups.

In the below snippet, a (partial) mapping of address/size pairs from [A Link to the Past Randomizer][alttpr] are mapped
to names for easy lookup as an `AddressEnum`. We also create a `MemData` class which uses this new `AddressEnum` type to
translate gRPC responses into a `dict`-like mapping.

```python
--8<-- "examples/snirk_types.py"
```

### Reading a single memory address

The memory reading functions of `Snirk` are intended to be passed [`AddressEnum`][AddressEnum] arguments and return
gRPC responses which can be coerced into `dict` mappings for ease-of-use via [`MemData`][MemData].

In the below snippet, we use [`Snirk.single_read`][Snirk.single_read] with the classes we defined above to read
a single memory address and then coerce into a `dict`:

```python
response = asyncio.run(snirk.single_read(AlttprAddresses.GAMEMODE))
memdata = AlttprMemData(response)
```

```raw
>>> response
uri: "fxpakpro://./dev/ttyACM3"
response {
  requestAddress: 16056336
  deviceAddress: 16056336
  data: "\007"
}

>>> memdata
{<AlttprAddresses.GAMEMODE: (16056336, 1)>: 7}
```

### Reading multiple memory addresses

Below, [`Snirk.multi_read`][Snirk.multi_read] is used to read multiple addresses in a single request:

```python
responses = asyncio.run(snirk.multi_read(*AlttprAddresses))
memdata = AlttprMemData(responses)
```

```raw
>>> responses
uri: "fxpakpro://./dev/ttyACM3"
responses {
  requestAddress: 16056587
  deviceAddress: 16056587
  data: "\024"
}
responses {
  requestAddress: 16057356
  deviceAddress: 16057356
  data: "\000"
}
responses {
  requestAddress: 16056336
  deviceAddress: 16056336
  data: "\007"
}
responses {
  requestAddress: 16056347
  deviceAddress: 16056347
  data: "\001"
}
responses {
  requestAddress: 16057432
  deviceAddress: 16057432
  data: "\000"
}

>>> from pprint import pprint
>>> pprint(memdata)
{<AlttprAddresses.CURRENT_MSU: (16056587, 1)>: 20,
 <AlttprAddresses.GAMEMODE: (16056336, 1)>: 7,
 <AlttprAddresses.DUNGEON: (16057356, 1)>: 0,
 <AlttprAddresses.INDOORS: (16056347, 1)>: 1,
 <AlttprAddresses.LAMPCONE: (16057432, 1)>: 0}
```

### Session context manager

In the above examples, we used `asyncio.run` to resolve awaitables in the python REPL.

Alternatively, in async applications, it can be convenient to use a `Snirk` object in a context manager (similar
to sessions in `aiohttp`), using [`Snirk.session`][Snirk.session].

The below snippet demonstates this session usage, as well as iterating over multiple SNI devices. This snippet
discovers all SNI devices and then reads some memory addresses from each:

```python
--8<-- "examples/snirk_session.py"
```

Example output:

```raw
Device URI: fxpakpro://./dev/ttyACM4
{<AlttprAddresses.DUNGEON: (16057356, 1)>: 85,
 <AlttprAddresses.CURRENT_MSU: (16056587, 1)>: 0,
 <AlttprAddresses.GAMEMODE: (16056336, 1)>: 85,
 <AlttprAddresses.INDOORS: (16056347, 1)>: 85,
 <AlttprAddresses.LAMPCONE: (16057432, 1)>: 85}
Device URI: ra://127.0.0.1:55355
{<AlttprAddresses.DUNGEON: (16057356, 1)>: 255,
 <AlttprAddresses.CURRENT_MSU: (16056587, 1)>: 0,
 <AlttprAddresses.GAMEMODE: (16056336, 1)>: 7,
 <AlttprAddresses.INDOORS: (16056347, 1)>: 1,
 <AlttprAddresses.LAMPCONE: (16057432, 1)>: 0}
```

## Accessing device filesystems over SNI

Not all SNI devices necessarily have a device filesytem which is accessible. To work with device filesystems over SNI,
a separate [`SnirkFilesystem`][SnirkFilesystem] class is provided (which inherits from `Snirk`).

!!! note

    Not all SNI devices necessarily have a device filesytem which is accessible. The `SnirkFilesystem` methods will
    only work on devices with appropriate capabilities (which can be seen on the `.device`). On devices without
    the appropriate capabilities, a `SnirkIncapableError` exception will be raised.

A `SnirkFilesystem` instance provides several methods for interacting with device filesystems:

* [`SnirkFilesystem.get_file`][SnirkFilesystem.get_file]
* [`SnirkFilesystem.put_file`][SnirkFilesystem.put_file]
* [`SnirkFilesystem.remove_file`][SnirkFilesystem.remove_file]
* [`SnirkFilesystem.make_directory`][SnirkFilesystem.make_directory]
* [`SnirkFilesystem.read_directory`][SnirkFilesystem.read_directory]

### Example

The below example snippet shows connecting to a device filesystem and performing several operations:

```python
--8<-- "examples/snirk_filesystem.py"
```

Example output:

```raw
* Device URI: fxpakpro://./dev/ttyACM0
* Making directory: /example...
* Putting file: /example/hello.txt...
* Reading directory: /example...
['hello.txt']
* Reading file: /example/hello.txt...
uri: "fxpakpro://./dev/ttyACM0"
path: "/example/hello.txt"
size: 17
data: "Hello, SNI World."

* Removing file: /example/hello.txt...
* Re-reading directory: /example...
[]
```

[AddressEnum]: api/types.md#snirk.types.AddressEnum
[alttpr]: https://alttpr.com
[asyncio]: https://docs.python.org/3.11/library/asyncio.html
[asyncio.run]: https://docs.python.org/3.11/library/asyncio-runner.html#asyncio.run
[awaitables]: https://docs.python.org/3.11/library/asyncio-task.html#awaitables
[MemData]: api/types.md#snirk.types.MemData
[sni-capabilities]: https://github.com/alttpo/sni?tab=readme-ov-file#capabilities
[Snirk]: api/api.md#snirk.api.Snirk
[Snirk.device]: api/api.md#snirk.api.Snirk.device
[SnirkFilesystem]: api/fs.md#snirk.api.SnirkFilesystem
[SnirkFilesystem.get_file]: api/fs.md#snirk.api.SnirkFilesystem.get_file
[SnirkFilesystem.make_directory]: api/fs.md#snirk.api.SnirkFilesystem.make_directory
[SnirkFilesystem.put_file]: api/fs.md#snirk.api.SnirkFilesystem.put_file
[SnirkFilesystem.read_directory]: api/fs.md#snirk.api.SnirkFilesystem.read_directory
[SnirkFilesystem.remove_file]: api/fs.md#snirk.api.SnirkFilesystem.remove_file
[Snirk.find_device]: api/api.md#snirk.api.Snirk.find_device
[Snirk.list_devices]: api/api.md#snirk.api.Snirk.list_devices
[Snirk.multi_read]: api/api.md#snirk.api.Snirk.multi_read
[Snirk.session]: api/api.md#snirk.api.Snirk.session
[Snirk.single_read]: api/api.md#snirk.api.Snirk.single_read
