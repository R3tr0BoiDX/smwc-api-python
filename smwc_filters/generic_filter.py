"""
Author: R3tr0BoiDX

Date: 2023-10-18

Description: This module contains the filters for generic sections on SMWC API.
"""
from typing import List, Optional, Union
from enum import Enum

from ._generator import ParamSet, ParamField


class OperatingSystem(Enum):
    """
    the operating system a tool runs on.
    """

    WINDOWS = ("Windows", 76)
    MAC = ("Mac OS X", 77)
    LINUX = ("Linux", 78)
    OTHER = ("Other", 79)


class Platform(Enum):
    """
    the platform a tool can be used for.
    """

    GENERAL = ("General", 80)
    SNES = ("SNES", 81)
    N64 = ("N64", 82)


class Game(Enum):
    """
    for which game a tool can be used for.
    """

    GENERAL = ("General", 83)
    SMW = ("SMW", 84)
    YI = ("YI", 85)
    SM64 = ("SM64", 86)


class FeaturedTool(Enum):
    """
    if the tool was featured or not.
    """

    NO = ("No", 73)
    YES = ("Yes", 74)
    ESSENTIAL = ("Essential", 75)


class DocumentType(Enum):
    """
    Type of a document.
    """

    DOCUMENTATION = ("Documentation", 87)
    TUTORIAL = ("Tutorial", 88)


class Language(Enum):
    """
    the language of a document.
    """

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
    author: Optional[Union[str, List[str]]] = None,
    tags: Optional[Union[str, List[str]]] = None,
    os: Optional[List[OperatingSystem]] = None,
    platform: Optional[List[Platform]] = None,
    game: Optional[List[Game]] = None,
    source_available: Optional[bool] = None,
    featured: Optional[List[FeaturedTool]] = None,
    desc: Optional[str] = None,
) -> ParamSet:
    """
    Returns a `ParamSet`, which represents the parameters for the tools section.

    Args:
        name (str, optional): Part of the name of the tool.
        author (str/List[str], optional): The author(s) that contributed to the tool.
        tags (str/List[str], optional): The tag(s) of the tool.
        os (OperatingSystem/List[OperatingSystem], optional): The operating system(s) the tool runs on.
        platform (Platform/List[Platform], optional): The platform(s) the tool can be used for.
        game (Game/List[Game], optional): The game(s) the tool can be used for.
        source_available (bool, optional): Whether the source code of the tool is available.
        featured (FeaturedTool/List[FeaturedTool], optional): Whether the tool was featured.
        desc (str, optional): Part of the description of the tool.

    Returns:
        ParamSet: The specified parameters for the tools section.
    """
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
    author: Optional[Union[str, List[str]]] = None,
    tags: Optional[Union[str, List[str]]] = None,
    platform: Optional[List[Platform]] = None,
    game: Optional[List[Game]] = None,
    doc_type: Optional[List[DocumentType]] = None,
    language: Optional[List[Language]] = None,
    desc: Optional[str] = None,
) -> ParamSet:
    """
    Returns a `ParamSet`, which represents the parameters for the documents section.

    Args:
        name (str, optional): Part of the name of the document.
        author (str/List[str], optional): The author(s) that contributed to the document.
        tags (str/List[str], optional): The tag(s) of the document.
        platform (Platform/List[Platform], optional): The platform(s) the document targets.
        game (Game/List[Game], optional): The game(s) the document targets.
        doc_type (DocumentType/List[DocumentType], optional): The type(s) of the document.
        language (Language/List[Language], optional): The language(s) of the document.
        desc (str, optional): Part of the description of the document.

    Returns:
        ParamSet: The specified parameters for the documents section.
    """
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
