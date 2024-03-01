import pytest

from snirk.api import SnirkIncapableError
from snirk.fs import SnirkFilesystem


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "method, args, capability",
    (
        ("get_file", ("missing",), "GetFile"),
        ("make_directory", ("missing",), "MakeDirectory"),
        (
            "put_file",
            (
                b"",
                "missing",
            ),
            "PutFile",
        ),
        ("read_directory", ("missing",), "ReadDirectory"),
        ("remove_file", ("missing",), "RemoveFile"),
    ),
    ids=("get_file", "make_directory", "put_file", "read_directory", "remove_file"),
)
async def test_incapable(helpers, retroarch, method, args, capability):
    """Check that incapable devices raise exception on filesystem operations."""
    with helpers.patch_devices(retroarch):
        snirk = SnirkFilesystem()
        with pytest.raises(SnirkIncapableError) as exc:
            await getattr(snirk, method)(*args, timeout=0.1)
    assert capability in str(exc)
