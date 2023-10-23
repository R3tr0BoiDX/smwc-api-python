from typing import List, Optional
from enum import Enum

from ._generator import ParamSet, ParamField


class YIMusicType(Enum):
    SONG = ("Song", 144)
    SOUNDTRACK = ("Soundtrack", 145)
    SOUND_EFFECT = ("Sound Effect", 146)
    MISC = ("Misc", 147)


class YIFeaturedPatches(Enum):
    NO = ("No", 136)
    YES = ("Yes", 137)


class YISPASMType(Enum):
    INIT = ("Init", 153)
    MAIN = ("Main", 154)


def get_yihacks_param(
    name: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    demo: Optional[bool] = None,
    desc: Optional[str] = None,
) -> ParamSet:
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
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    music_type: Optional[List[YIMusicType]] = None,
    sampled: Optional[bool] = None,
    custom: Optional[bool] = None,
    featured: Optional[bool] = None,
    desc: Optional[str] = None,
) -> ParamSet:
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
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    requires_free_space: Optional[bool] = None,
    bug_fix: Optional[bool] = None,
    featured: Optional[List[YIFeaturedPatches]] = None,
    desc: Optional[str] = None,
) -> ParamSet:
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
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    spasm_type: Optional[List[YISPASMType]] = None,
    includes_hijack: Optional[bool] = None,
    featured: Optional[bool] = None,
    desc: Optional[str] = None,
) -> ParamSet:
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
