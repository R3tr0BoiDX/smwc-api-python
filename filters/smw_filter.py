from typing import List, Optional
from enum import Enum

from ._generator import form_params


class HackType(Enum):
    EASY = ("Standard: Easy", 104)
    NORMAL = ("Standard: Normal", 105)
    HARD = ("Standard: Hard", 106)
    VERY_HARD = ("Standard: Very Hard", 141)
    KAIZO_BEGINNER = ("Kaizo: Beginner", 196)
    KAIZO_INTERMEDIATE = ("Kaizo: Intermediate", 107)
    KAIZO_EXPERT = ("Kaizo: Expert", 197)
    TOOL_ASSISTED_KAIZO = ("Tool-Assisted: Kaizo", 124)
    TOOL_ASSISTED_PIT = ("Tool-Assisted: Pit", 125)
    MISC_TROLL = ("Misc.: Troll", 161)


class GraphicsType(Enum):
    ORIGINAL = ("Original", 52)
    RIPPED = ("Ripped", 53)


class Purpose(Enum):
    BACKGROUND = ("Background", 54)
    FOREGROUND = ("Foreground", 55)
    SPRITE = ("Sprite", 56)
    PLAYER = ("Player", 57)
    LAYER_3 = ("Layer 3", 58)
    OVERWORLD = ("Overworld", 59)
    FONT = ("Font", 60)
    MISCELLANEOUS = ("Miscellaneous", 61)
    GRAPHICS_HACK = ("Graphics Hack", 108)


class SlotsUsed(Enum):
    BG1 = ("BG1", 162)
    BG2 = ("BG2", 163)
    BG3 = ("BG3", 164)
    FG1 = ("FG1", 165)
    FG2 = ("FG2", 166)
    FG3 = ("FG3", 167)
    FG4 = ("FG4", 168)
    FG5 = ("FG5", 169)
    FG6 = ("FG6", 170)
    SP1 = ("SP1", 171)
    SP2 = ("SP2", 172)
    SP3 = ("SP3", 173)
    SP4 = ("SP4", 174)
    LG1 = ("LG1", 175)
    LG2 = ("LG2", 176)
    LG3 = ("LG3", 177)
    LG4 = ("LG4", 178)
    AN2 = ("AN2", 179)


class PaletteRowsUsed(Enum):
    ROWS_0 = ("0", 180)
    ROWS_1 = ("1", 181)
    ROWS_2 = ("2", 182)
    ROWS_3 = ("3", 183)
    ROWS_4 = ("4", 184)
    ROWS_5 = ("5", 185)
    ROWS_6 = ("6", 186)
    ROWS_7 = ("7", 187)
    ROWS_8 = ("8", 188)
    ROWS_9 = ("9", 189)
    ROWS_A = ("A", 190)
    ROWS_B = ("B", 191)
    ROWS_C = ("C", 192)
    ROWS_D = ("D", 193)
    ROWS_E = ("E", 194)
    ROWS_F = ("F", 195)


class SMWMusicType(Enum):
    SONG = ("Song", 109)
    SOUNDTRACK = ("Soundtrack", 110)
    SOUND_EFFECT = ("Sound Effect", 111)
    MISC = ("Misc.", 112)


class SampleUsage(Enum):
    NONE = ("None", 155)
    LIGHT = ("Light", 156)
    MANY = ("Many", 157)


class Source(Enum):
    PORT = ("Port", 158)
    REMIX = ("Remix", 159)
    ORIGINAL = ("Original", 160)


class Collection(Enum):
    COMPILATION = ("Compilation", 134)
    SINGLE = ("Single", 135)


class SpritesTool(Enum):
    PIXI = ("PIXI", 142)
    GIEPY = ("GIEPY", 143)
    ROMIS_SPRITE_TOOL = ("Romi's Spritetool", 41)
    OVERWORLD_SPRITE_TOOL = ("Overworld Spritetool", 43)
    OTHER = ("Other", 45)


class SpriteType(Enum):
    STANDARD = ("Standard", 46)
    SHOOTER = ("Shooter", 47)
    GENERATOR = ("Generator", 48)
    OVERWORLD = ("Overworld", 49)
    CLUSTER = ("Cluster", 64)
    EXTENDED = ("Extended", 65)
    RUN_ONCE = ("Run-Once", 66)
    OTHER = ("Other", 51)


class PatchTool(Enum):
    XKAS = ("xkas", 1)
    ASAR = ("Asar", 2)
    XKAS_OR_ASAR = ("xkas or Asar", 3)


class FeaturedSMWPatches(Enum):
    NO = ("No", 70)
    YES = ("Yes", 71)
    ESSENTIAL = ("Essential", 72)


class UberASMType(Enum):
    LEVEL = ("Level", 138)
    OVERWORLD = ("Overworld", 139)
    GAME_MODE = ("Game Mode", 140)
    GLOBAL = ("Global", 152)


def get_smwhacks_param(
    name: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    demo: Optional[bool] = None,
    featured: Optional[bool] = None,
    hack_type: Optional[List[HackType]] = None,
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
    if featured is not None:
        params["featured"] = featured
    if hack_type is not None:
        params["difficulty"] = [h.value[1] for h in hack_type]
    if desc is not None:
        params["desc"] = desc

    return form_params(params)


def get_sramdatabase_param(
    name: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
):
    params = {}
    if name is not None:
        params["name"] = name
    if author is not None:
        params["author"] = author
    if tags is not None:
        params["tags"] = tags

    return form_params(params)


def get_smwgraphics_param(
    name: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    graphics_type: Optional[List[GraphicsType]] = None,
    purpose: Optional[List[Purpose]] = None,
    slots_used: Optional[List[SlotsUsed]] = None,
    palette_rows_used: Optional[List[PaletteRowsUsed]] = None,
    desc: Optional[str] = None,
):
    params = {}
    if name is not None:
        params["name"] = name
    if author is not None:
        params["author"] = author
    if tags is not None:
        params["tags"] = tags
    if graphics_type is not None:
        params["type"] = [g.value[1] for g in graphics_type]
    if purpose is not None:
        params["purpose"] = [p.value[1] for p in purpose]
    if slots_used is not None:
        params["slots"] = [s.value[1] for s in slots_used]
    if palette_rows_used is not None:
        params["palette"] = [p.value[1] for p in palette_rows_used]
    if desc is not None:
        params["desc"] = desc

    return form_params(params)


def get_smwmusic_param(
    name: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    music_type: Optional[List[SMWMusicType]] = None,
    sample_usage: Optional[List[SampleUsage]] = None,
    source: Optional[List[Source]] = None,
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
        params["type"] = [m.value[1] for m in music_type]
    if sample_usage is not None:
        params["sample"] = [s.value[1] for s in sample_usage]
    if source is not None:
        params["source"] = [s.value[1] for s in source]
    if featured is not None:
        params["featured"] = featured
    if desc is not None:
        params["desc"] = desc

    return form_params(params)


def get_brrsamples_param(
    name: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    collection: Optional[List[Collection]] = None,
    desc: Optional[str] = None,
):
    params = {}
    if name is not None:
        params["name"] = name
    if author is not None:
        params["author"] = author
    if tags is not None:
        params["tags"] = tags
    if collection is not None:
        params["collection"] = [c.value[1] for c in collection]
    if desc is not None:
        params["desc"] = desc

    return form_params(params)


def get_smwblocks_param(
    name: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    act_as: Optional[str] = None,
    includes_gfx: Optional[bool] = None,
    desc: Optional[str] = None,
):
    params = {}
    if name is not None:
        params["name"] = name
    if author is not None:
        params["author"] = author
    if tags is not None:
        params["tags"] = tags
    if act_as is not None:
        params["act_as"] = act_as
    if includes_gfx is not None:
        params["includes_gfx"] = includes_gfx
    if desc is not None:
        params["desc"] = desc

    return form_params(params)


def get_smwsprites_param(
    name: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    tool: Optional[List[SpritesTool]] = None,
    sprite_type: Optional[List[SpriteType]] = None,
    dynamic: Optional[bool] = None,
    disassembly: Optional[bool] = None,
    includes_gfx: Optional[bool] = None,
    desc: Optional[str] = None,
):
    params = {}
    if name is not None:
        params["name"] = name
    if author is not None:
        params["author"] = author
    if tags is not None:
        params["tags"] = tags
    if tool is not None:
        params["tool"] = [t.value[1] for t in tool]
    if sprite_type is not None:
        params["type"] = [s.value[1] for s in sprite_type]
    if dynamic is not None:
        params["dynamic"] = dynamic
    if disassembly is not None:
        params["disassembly"] = disassembly
    if includes_gfx is not None:
        params["includes_gfx"] = includes_gfx
    if desc is not None:
        params["desc"] = desc

    return form_params(params)


def get_smwpatches_param(
    name: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    tool: Optional[List[PatchTool]] = None,
    requires_free_space: Optional[bool] = None,
    bug_fix: Optional[bool] = None,
    featured: Optional[List[FeaturedSMWPatches]] = None,
    desc: Optional[str] = None,
):
    params = {}
    if name is not None:
        params["name"] = name
    if author is not None:
        params["author"] = author
    if tags is not None:
        params["tags"] = tags
    if tool is not None:
        params["tool"] = [t.value[1] for t in tool]
    if requires_free_space is not None:
        params["requires_free_space"] = requires_free_space
    if bug_fix is not None:
        params["bug_fix"] = bug_fix
    if featured is not None:
        params["featured"] = [f.value[1] for f in featured]
    if desc is not None:
        params["desc"] = desc

    return form_params(params)


def get_uberasm_param(
    name: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    uberasm_type: Optional[List[UberASMType]] = None,
    includes_gfx: Optional[bool] = None,
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
    if uberasm_type is not None:
        params["type"] = [u.value[1] for u in uberasm_type]
    if includes_gfx is not None:
        params["includes_gfx"] = includes_gfx
    if includes_hijack is not None:
        params["includes_hijack"] = includes_hijack
    if featured is not None:
        params["featured"] = featured
    if desc is not None:
        params["desc"] = desc

    return form_params(params)
