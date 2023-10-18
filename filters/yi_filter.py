from typing import List, Optional
from enum import Enum

from ._generator import form_params


class YIMusicType(Enum):
    SONG = ("Song", 144)
    SOUNDTRACK = ("Soundtrack", 145)
    SOUND_EFFECT = ("Sound Effect", 146)
    MISC = ("Misc", 147)


class FeaturedYIPatches(Enum):
    NO = ("No", 136)
    YES = ("Yes", 137)


class SPASMType(Enum):
    INIT = ("Init", 153)
    MAIN = ("Main", 154)


def get_yihacks_param(
    name: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    demo: Optional[bool] = None,
    desc: Optional[str] = None,
):
    params = {}
    if name is not None:
        params["name"] = name
    if author is not None:
        params["author"] = author
    if tags is not None:
        params["tags"] = tags
    if demo is not None:
        params["demo"] = demo
    if desc is not None:
        params["desc"] = desc

    return form_params(params)


def get_yimusic_param(
    name: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    music_type: Optional[List[YIMusicType]] = None,
    sampled: Optional[bool] = None,
    custom: Optional[bool] = None,
    featured: Optional[bool] = None,
    desc: Optional[str] = None,
):
    params = {}
    if name is not None:
        params["name"] = name
    if author is not None:
        params["author"] = author
    if tags is not None:
        params["tags"] = tags
    if music_type is not None:
        params["music_type"] = [m.value[1] for m in music_type]
    if sampled is not None:
        params["sampled"] = sampled
    if custom is not None:
        params["custom"] = custom
    if featured is not None:
        params["featured"] = featured
    if desc is not None:
        params["desc"] = desc

    return form_params(params)


def get_yipatches_param(
    name: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    requires_free_space: Optional[bool] = None,
    bug_fix: Optional[bool] = None,
    featured: Optional[List[FeaturedYIPatches]] = None,
    desc: Optional[str] = None,
):
    params = {}
    if name is not None:
        params["name"] = name
    if author is not None:
        params["author"] = author
    if tags is not None:
        params["tags"] = tags
    if requires_free_space is not None:
        params["requires_free_space"] = requires_free_space
    if bug_fix is not None:
        params["bug_fix"] = bug_fix
    if featured is not None:
        params["featured"] = [f.value[1] for f in featured]
    if desc is not None:
        params["desc"] = desc

    return form_params(params)


def get_spasm_param(
    name: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    spasm_type: Optional[List[SPASMType]] = None,
    includes_hijack: Optional[bool] = None,
    featured: Optional[bool] = None,
    desc: Optional[str] = None,
):
    params = {}
    if name is not None:
        params["name"] = name
    if author is not None:
        params["author"] = author
    if tags is not None:
        params["tags"] = tags
    if spasm_type is not None:
        params["spasm_type"] = [s.value[1] for s in spasm_type]
    if includes_hijack is not None:
        params["includes_hijack"] = includes_hijack
    if featured is not None:
        params["featured"] = featured
    if desc is not None:
        params["desc"] = desc

    return form_params(params)
