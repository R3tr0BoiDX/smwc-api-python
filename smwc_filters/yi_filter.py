"""
Author: R3tr0BoiDX

Date: 2023-10-18

Description: This module contains the filters for all YI sections on SMWC API.
"""
from typing import List, Optional, Union
from enum import Enum

from ._generator import ParamSet, ParamField


class YIMusicType(Enum):
    """
    Type of a YI music entry.
    """

    SONG = ("Song", 144)
    SOUNDTRACK = ("Soundtrack", 145)
    SOUND_EFFECT = ("Sound Effect", 146)
    MISC = ("Misc", 147)


class YIFeaturedPatches(Enum):
    """
    if the patch was featured or not.
    """

    NO = ("No", 136)
    YES = ("Yes", 137)


class YISPASMType(Enum):
    """
    Type of a SPASM.
    """

    INIT = ("Init", 153)
    MAIN = ("Main", 154)


def get_yihacks_param(
    name: Optional[str] = None,
    author: Optional[Union[str, List[str]]] = None,
    tags: Optional[Union[str, List[str]]] = None,
    demo: Optional[bool] = None,
    desc: Optional[str] = None,
) -> ParamSet:
    """
    Returns a `ParamSet`, which represents the parameters for the YI hacks section.

    Args:
        name (str, optional): Part of the name of the hack.
        author (str/List[str], optional): The author(s) that contributed to the hack.
        tags (str/List[str], optional): The tag(s) of the hack.
        demo (bool, optional): Whether the hack is a demo.
        desc (str, optional): Part of the description of the hack.

    Returns:
        ParamSet: The specified parameters for the YI hacks section.
    """
    params = []
    if name is not None:
        params.append((name, ParamField.NAME))
    if author is not None:
        params.append((author, ParamField.AUTHOR))
    if tags is not None:
        params.append((tags, ParamField.TAGS))
    if demo is not None:
        params.append((demo, ParamField.DEMO))
    if desc is not None:
        params.append((desc, ParamField.DESCRIPTION))

    return ParamSet(params)


def get_yimusic_param(
    name: Optional[str] = None,
    author: Optional[Union[str, List[str]]] = None,
    tags: Optional[Union[str, List[str]]] = None,
    music_type: Optional[List[YIMusicType]] = None,
    sampled: Optional[bool] = None,
    custom: Optional[bool] = None,
    featured: Optional[bool] = None,
    desc: Optional[str] = None,
) -> ParamSet:
    """
    Returns a `ParamSet`, which represents the parameters for the YI music section.

    Args:
        name (str, optional): Part of the name of the music entry.
        author (str/List[str], optional): The author(s) that contributed to the music entry.
        tags (str/List[str], optional): The tag(s) of the music entry.
        music_type (YIMusicType/List[YIMusicType], optional): The type(s) of the music entry.
        sampled (bool, optional): Whether the music uses custom samples.
        custom (bool, optional): Whether the music is original.
        featured (bool, optional): Whether the music was featured.
        desc (str, optional): Part of the description of the music entry.

    Returns:
        ParamSet: The specified parameters for the YI music section.
    """
    params = []
    if name is not None:
        params.append((name, ParamField.NAME))
    if author is not None:
        params.append((author, ParamField.AUTHOR))
    if tags is not None:
        params.append((tags, ParamField.TAGS))
    if music_type is not None:
        params.append((music_type, ParamField.TYPE))
    if sampled is not None:
        params.append((sampled, ParamField.SAMPLED))
    if custom is not None:
        params.append((custom, ParamField.CUSTOM))
    if featured is not None:
        params.append((featured, ParamField.FEATURED))
    if desc is not None:
        params.append((desc, ParamField.DESCRIPTION))

    return ParamSet(params)


def get_yipatches_param(
    name: Optional[str] = None,
    author: Optional[Union[str, List[str]]] = None,
    tags: Optional[Union[str, List[str]]] = None,
    requires_free_space: Optional[bool] = None,
    bug_fix: Optional[bool] = None,
    featured: Optional[List[YIFeaturedPatches]] = None,
    desc: Optional[str] = None,
) -> ParamSet:
    """
    Returns a `ParamSet`, which represents the parameters for the YI patches section.

    Args:
        name (str, optional): Part of the name of the patch.
        author (str/List[str], optional): The author(s) that contributed to the patch.
        tags (str/List[str], optional): The tag(s) of the patch.
        requires_free_space (bool, optional): Whether the patch requires free space.
        bug_fix (bool, optional): Whether the patch is a bug fix in the original game.
        featured (YIFeaturedPatches/List[YIFeaturedPatches], optional): Whether the patch was featured.
        desc (str, optional): Part of the description of the patch.

    Returns:
        ParamSet: The specified parameters for the YI patches section.
    """
    params = []
    if name is not None:
        params.append((name, ParamField.NAME))
    if author is not None:
        params.append((author, ParamField.AUTHOR))
    if tags is not None:
        params.append((tags, ParamField.TAGS))
    if requires_free_space is not None:
        params.append((requires_free_space, ParamField.FREESPACE))
    if bug_fix is not None:
        params.append((bug_fix, ParamField.BUGFIX))
    if featured is not None:
        params.append((featured, ParamField.FEATURED_LIST))
    if desc is not None:
        params.append((desc, ParamField.DESCRIPTION))

    return ParamSet(params)


def get_spasm_param(
    name: Optional[str] = None,
    author: Optional[Union[str, List[str]]] = None,
    tags: Optional[Union[str, List[str]]] = None,
    spasm_type: Optional[List[YISPASMType]] = None,
    includes_hijack: Optional[bool] = None,
    featured: Optional[bool] = None,
    desc: Optional[str] = None,
) -> ParamSet:
    """
    Returns a `ParamSet`, which represents the parameters for the SPASM section.

    Args:
        name (str, optional): Part of the name of the SPASM.
        author (str/List[str], optional): The author(s) that contributed to the SPASM.
        tags (str/List[str], optional): The tag(s) of the SPASM.
        spasm_type (YISPASMType/List[YISPASMType], optional): The type(s) of the SPASM.
        includes_hijack (bool, optional): Whether the SPASM includes hijack.
        featured (bool, optional): Whether the SPASM was featured.
        desc (str, optional): Part of the description of the SPASM.

    Returns:
        ParamSet: The specified parameters for the SPASM section.
    """
    params = []
    if name is not None:
        params.append((name, ParamField.NAME))
    if author is not None:
        params.append((author, ParamField.AUTHOR))
    if tags is not None:
        params.append((tags, ParamField.TAGS))
    if spasm_type is not None:
        params.append((spasm_type, ParamField.TYPE))
    if includes_hijack is not None:
        params.append((includes_hijack, ParamField.INCLUDESHIJACK))
    if featured is not None:
        params.append((featured, ParamField.FEATURED))
    if desc is not None:
        params.append((desc, ParamField.DESCRIPTION))

    return ParamSet(params)
