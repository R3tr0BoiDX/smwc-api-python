from typing import List, Optional
from enum import Enum

from ._generator import ParamSet, ParamField


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
) -> ParamSet:
    params = []
    if name is not None:
        params.append((name, ParamField.NAME))
    if author is not None:
        params.append((author, ParamField.AUTHOR))
    if tags is not None:
        params.append((tags, ParamField.TAGS))
    if os is not None:
        params.append((os, ParamField.OS))
    if platform is not None:
        params.append((platform, ParamField.PLATFORMS))
    if game is not None:
        params.append((game, ParamField.GAMES))
    if source_available is not None:
        params.append((source_available, ParamField.SOURCE))
    if featured is not None:
        params.append((featured, ParamField.FEATURED_LIST))
    if desc is not None:
        params.append((desc, ParamField.DESCRIPTION))

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
) -> ParamSet:
    params = []
    if name is not None:
        params.append((name, ParamField.NAME))
    if author is not None:
        params.append((author, ParamField.AUTHOR))
    if tags is not None:
        params.append((tags, ParamField.TAGS))
    if platform is not None:
        params.append((platform, ParamField.PLATFORMS))
    if game is not None:
        params.append((game, ParamField.GAMES))
    if doc_type is not None:
        params.append((doc_type, ParamField.TYPE))
    if language is not None:
        params.append((language, ParamField.LANGUAGE))
    if desc is not None:
        params.append((desc, ParamField.DESCRIPTION))

    return ParamSet(params)
