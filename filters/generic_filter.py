from typing import List, Optional
from enum import Enum

from ._generator import ParamSet, ParamType


class OperatingSystem(Enum):
    WINDOWS = ("Windows", 76)
    MAC = ("Mac OS X", 77)
    LINUX = ("Linux", 78)
    OTHER = ("Other", 79)


class Platform(Enum):
    GENERAL = ("General", 80)
    SNES = ("SNES", 81)
    N64 = ("N64", 82)


class Game(Enum):
    GENERAL = ("General", 83)
    SMW = ("SMW", 84)
    YI = ("YI", 85)
    SM64 = ("SM64", 86)


class FeaturedTool(Enum):
    NO = ("No", 73)
    YES = ("Yes", 74)
    ESSENTIAL = ("Essential", 75)


class DocumentType(Enum):
    DOCUMENTATION = ("Documentation", 87)
    TUTORIAL = ("Tutorial", 88)


class Language(Enum):
    ENGLISH = ("English", 96)
    PORTUGUESE = ("Portuguese", 97)
    DUTCH = ("Dutch", 98)
    SPANISH = ("Spanish", 99)
    FRENCH = ("French", 100)
    GERMAN = ("German", 101)
    ITALIAN = ("Italian", 102)
    OTHER = ("Other", 103)


def get_tools_param(
    name: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    os: Optional[List[OperatingSystem]] = None,
    platform: Optional[List[Platform]] = None,
    game: Optional[List[Game]] = None,
    source_available: Optional[bool] = None,
    featured: Optional[List[FeaturedTool]] = None,
    desc: Optional[str] = None,
):
    params = []
    if name is not None:
        params.append(("name", name, ParamType.STR))
    if author is not None:
        params.append(("author", author, ParamType.STR))
    if tags is not None:
        params.append(("tags", tags, ParamType.CSV))
    if os is not None:
        params.append(("os", [o.value[1] for o in os], ParamType.LIST))
    if platform is not None:
        params.append(("platforms", [p.value[1] for p in platform], ParamType.LIST))
    if game is not None:
        params.append(("games", [g.value[1] for g in game], ParamType.LIST))
    if source_available is not None:
        params.append(("source", source_available, ParamType.BOOL))
    if featured is not None:
        params.append(("featured", [f.value[1] for f in featured], ParamType.LIST))
    if desc is not None:
        params.append(("description", desc, ParamType.STR))

    return ParamSet(params)


def get_documents_param(
    name: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    platform: Optional[List[Platform]] = None,
    game: Optional[List[Game]] = None,
    doc_type: Optional[List[DocumentType]] = None,
    language: Optional[List[Language]] = None,
    desc: Optional[str] = None,
):
    params = []
    if name is not None:
        params.append(("name", name, ParamType.STR))
    if author is not None:
        params.append(("author", author, ParamType.STR))
    if tags is not None:
        params.append(("tags", tags, ParamType.CSV))
    if platform is not None:
        params.append(("platforms", [p.value[1] for p in platform], ParamType.LIST))
    if game is not None:
        params.append(("games", [g.value[1] for g in game], ParamType.LIST))
    if doc_type is not None:
        params.append(("type", [t.value[1] for t in doc_type], ParamType.LIST))
    if language is not None:
        params.append(("language", [lang.value[1] for lang in language], ParamType.LIST))
    if desc is not None:
        params.append(("description", desc, ParamType.STR))

    return ParamSet(params)
