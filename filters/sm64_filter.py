from typing import List, Optional
from enum import Enum

from ._generator import ParamSet, ParamType


class Difficulty(Enum):
    EASY = ("Easy", 148)
    INTERMEDIATE = ("Intermediate", 149)
    HARD = ("Hard", 150)
    KAIZO = ("Kaizo", 151)


class TexturesType(Enum):
    ORIGINAL = ("Original", 39)
    RIPPED = ("Ripped", 40)


class Nlist(Enum):
    NLST0 = ("NLST 0 (SFX)", 1)
    NLST1 = ("NLST 1 (SFX, Footsteps)", 2)
    NLST2 = ("NLST 2 (SFX, Water)", 3)
    NLST3 = ("NLST 3 (SFX, Sand?)", 4)
    NLST4 = ("NLST 4 (SFX)", 5)
    NLST5 = ("NLST 5 (SFX)", 6)
    NLST6 = ("NLST 6 (SFX)", 7)
    NLST7 = ("NLST 7 (SFX, misc)", 8)
    NLST8 = ("NLST 8 (Mario's NLST)", 9)
    NLST9 = ("NLST 9 (SFX)", 10)
    NLST10 = ("NLST 10 (SFX, Voices)", 11)
    NLST11 = ("NLST 11 (Snow)", 12)
    NLST12 = ("NLST 12 (Unused)", 13)
    NLST13 = ("NLST 13 (Koopa the Quick, Slide Levels)", 14)
    NLST14 = ("NLST 14 (Inside Castle Walls)", 15)
    NLST15 = ("NLST 15 (Shifting Sand Land/Lethal Lava Land)", 16)
    NLST16 = ("NLST 16 (Haunted House)", 17)
    NLST17 = ("NLST 17 (Title Screen)", 18)
    NLST18 = ("NLST 18 (Bowser Battle)", 19)
    NLST19 = ("NLST 19 (Jolly Roger Bay/Dire Dire Docks)", 20)
    NLST20 = ("NLST 20 (Piranha Plant's Sleeping Melody)", 21)
    NLST21 = ("NLST 21 (Hazy Maze Cave)", 22)
    NLST22 = ("NLST 22 (Star Select)", 23)
    NLST23 = ("NLST 23 (Wing Cap)", 24)
    NLST24 = ("NLST 24 (Metal Cap)", 25)
    NLST25 = ("NLST 25 (Bowser Course)", 26)
    NLST26 = ("NLST 26 (Fanfares)", 27)
    NLST27 = ("NLST 27 (Boss Fight)", 28)
    NLST28 = ("NLST 28 (Looping Stairs)", 29)
    NLST29 = ("NLST 29 (Final Bowser Battle)", 30)
    NLST30 = ("NLST 30 (Peach Message)", 31)
    NLST31 = ("NLST 31 (Star Appears)", 32)
    NLST32 = ("NLST 32 (Toad)", 33)
    NLST33 = ("NLST 33 (Ghost Merry-Go-Round)", 34)
    NLST34 = ("NLST 34 (Bob-Omb Battlefield)", 35)
    NLST35 = ("NLST 35 (Ending)", 36)
    NLST36 = ("NLST 36 (File Select)", 37)
    NLST37 = ("NLST 37 (Credits)", 38)


def get_sm64hacks_param(
    name: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    difficulty: Optional[List[Difficulty]] = None,
    demo: Optional[bool] = None,
    desc: Optional[str] = None,
) -> ParamSet:
    params = []
    if name is not None:
        params.append(("name", name, ParamType.STR))
    if author is not None:
        params.append(("author", author, ParamType.STR))
    if tags is not None:
        params.append(("tags", tags, ParamType.CSV))
    if difficulty is not None:
        params.append(("difficulty", [d.value[1] for d in difficulty], ParamType.LIST))
    if demo is not None:
        params.append(("demo", demo, ParamType.BOOL))
    if desc is not None:
        params.append(("description", desc, ParamType.STR))

    return ParamSet(params)


def get_sm64textures_param(
    name: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    textures_type: Optional[List[TexturesType]] = None,
    desc: Optional[str] = None,
) -> ParamSet:
    params = []
    if name is not None:
        params.append(("name", name, ParamType.STR))
    if author is not None:
        params.append(("author", author, ParamType.STR))
    if tags is not None:
        params.append(("tags", tags, ParamType.CSV))
    if textures_type is not None:
        params.append(
            ("type", [t.value[1] for t in textures_type], ParamType.LIST)
        )
    if desc is not None:
        params.append(("description", desc, ParamType.STR))

    return ParamSet(params)


def get_sm64music_param(
    name: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    nlist: Optional[List[Nlist]] = None,
    desc: Optional[str] = None,
) -> ParamSet:
    params = []
    if name is not None:
        params.append(("name", name, ParamType.STR))
    if author is not None:
        params.append(("author", author, ParamType.STR))
    if tags is not None:
        params.append(("tags", tags, ParamType.CSV))
    if nlist is not None:
        params.append(("nlist", [n.value[1] for n in nlist], ParamType.LIST))
    if desc is not None:
        params.append(("description", desc, ParamType.STR))

    return ParamSet(params)
