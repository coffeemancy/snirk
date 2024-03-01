from collections import UserDict
from enum import Enum
from functools import singledispatchmethod
from typing import ClassVar, Optional, Type, Union

from snirk.sni import sni_pb2 as pb


# CLASSES ####################################################################


class AddressEnum(Enum):
    """Enum of address keys mapped to address and size.

    Supports getting via attribute (per typical enum) as well as getting via string key.
    """

    def __init__(self, address: int, size: int):
        self.address = address
        self.size = size

    @classmethod
    def get(cls, address: int):
        """Lookup by address."""
        return next(member for member in cls if member.address == address)


class MemData(UserDict):
    """Dict-like container for mapping of memory addresses to values parsed from gRPC response.

    Intended to be subclassed by apps using Snirk with a relevant AddressEnum subclass.

    Allows lookup via indexing ("[...]") from: address enum (AddressEnum), memory address (int), or key (str).
    Preferred method is generally by AddressEnum for static use so mypy/type-checker can catch, instead of
    runtime errors (where possible).

    :param memclass: AddressEnum subclass associated with this MemData subclass
    :type memclass: Type[AddressEnum]
    """

    # set in subclasses to a particular AddressEnum subclass
    memclass: ClassVar[Type[AddressEnum]]

    def __init__(self, response: Optional[Union[pb.MultiReadMemoryResponse, pb.SingleReadMemoryResponse]] = None):
        """Initialize memory data with optional parsing of gRPC response into data.

        :param response: SNI multi read memory response to parse
        """
        self.data: dict[AddressEnum, int] = {}

        if response:
            self.parse(response)

    def __getitem__(self, key: Union[AddressEnum, int, str]) -> int:
        """Lookup memory data via key.

        Try to lookup via key directly (e.g. AddressEnum). On KeyError, if int, perform lookup via address.
        When string, lookup via AddressEnum (using string). Otherwise, raise a KeyError.

        :param key: key to lookup from data
        :raises KeyError: cannot find key in data
        """
        if isinstance(key, int):
            return self.data[self.memclass.get(key)]
        elif isinstance(key, str):
            return self.data[self.memclass[key]]
        return self.data[key]

    @singledispatchmethod
    def parse(self, response):
        """Parse gRPC response into data.

        :param response: SNI single/multi read memory response to parse
        :type response: Union[pb.MultiReadMemoryResponse, pb.SingleReadMemoryResponse]
        """
        raise NotImplementedError(f"Cannot parse response: {response}")

    @parse.register
    def _(self, response: pb.MultiReadMemoryResponse):
        self.data = {self.memclass.get(msg.requestAddress): int(msg.data.hex(), 16) for msg in response.responses}

    @parse.register
    def _(self, response: pb.SingleReadMemoryResponse):
        msg = response.response
        self.data = {self.memclass.get(msg.requestAddress): int(msg.data.hex(), 16)}
