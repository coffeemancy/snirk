from snirk.types import AddressEnum
from snirk.types import MemData


class AlttprAddresses(AddressEnum):
    # current MSU is $010B in WRAM (starts at 0xF50000)
    # https://github.com/KatDevsGames/z3randomizer/blob/master/msu.asm#L126
    CURRENT_MSU = (0xF5010B, 0x1)

    # from https://github.com/KrisDavie/DoorTracker/blob/main/DoorsTracker.py
    DUNGEON = (0xF5040C, 0x1)
    GAMEMODE = (0xF50010, 0x1)
    INDOORS = (0xF5001B, 0x1)
    LAMPCONE = (0xF50458, 0x1)


class AlttprMemData(MemData):
    memclass = AlttprAddresses
