import pytest

from snirk.api import Snirk, SnirkError

import snirk.sni.sni_pb2 as pb


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "capability",
    (pb.DeviceCapability.ReadMemory, pb.DeviceCapability.WriteMemory, pb.DeviceCapability.ResetSystem),
    ids=("ReadMemory", "WriteMemory", "ResetSystem"),
)
async def test_ensure_capability(sni_devices, capability):
    snirk = Snirk()
    assert await snirk.ensure_capability(capability)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "kwargs, expected",
    (
        ({}, "fxpakpro://./dev/ttyACM1"),
        ({"kind": "retroarch"}, "ra://127.0.0.1:55355"),
        ({"uri": "ra://127.0.0.1:55355"}, "ra://127.0.0.1:55355"),
        ({"kind": "fxpakpro", "uri": "fxpakpro://./dev/ttyACM1"}, "fxpakpro://./dev/ttyACM1"),
    ),
    ids=["default", "kind", "uri", "kind+uri"],
)
async def test_find_device(sni_devices, kwargs, expected):
    snirk = Snirk()
    result = await snirk.find_device(**kwargs, timeout=0.1)
    assert result.uri == expected


@pytest.mark.asyncio
async def test_find_device_missing(helpers):
    """Ensure exception raised if cannot find any SNI devices."""
    with helpers.patch_devices():
        snirk = Snirk()
        with pytest.raises(SnirkError) as ex:
            await snirk.find_device(timeout=0.1)

    assert "Could not find any SNI devices" in str(ex)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "kwargs, expected",
    (
        ({}, {"fxpakpro", "retroarch"}),
        ({"kind": "fxpakpro"}, {"fxpakpro"}),
        ({"kind": "retroarch"}, {"retroarch"}),
    ),
    ids=["all", "fxpakpro", "retroarch"],
)
async def test_list_devices(sni_devices, kwargs, expected):
    snirk = Snirk()
    results = await snirk.list_devices(**kwargs, timeout=0.1)
    device_kinds = {device.kind for device in results}
    assert device_kinds == expected
