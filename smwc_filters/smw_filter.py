"""
Author: R3tr0BoiDX

Date: 2023-10-18

Description: This module contains the filters for all SMW sections on SMWC API.
"""
from typing import List, Optional, Union
from enum import Enum

from ._generator import ParamSet, ParamField


class SMWDifficulty(Enum):
    """
    the difficulty of a SMW hack.
    """

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


class SMWGraphicsType(Enum):
    """
    Type of a SMW graphic.
    """

    ORIGINAL = ("Original", 52)
    RIPPED = ("Ripped", 53)


class SMWPurpose(Enum):
    """
    the purpose of a SMW graphic.
    """

    BACKGROUND = ("Background", 54)
    FOREGROUND = ("Foreground", 55)
    SPRITE = ("Sprite", 56)
    PLAYER = ("Player", 57)
    LAYER_3 = ("Layer 3", 58)
    OVERWORLD = ("Overworld", 59)
    FONT = ("Font", 60)
    MISCELLANEOUS = ("Miscellaneous", 61)
    GRAPHICS_HACK = ("Graphics Hack", 108)


class SMWSlotsUsed(Enum):
    """
    how many slots are used by a SMW graphic.
    """

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


class SMWPaletteRowsUsed(Enum):
    """
    how many palette rows are used by a SMW graphic.
    """

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
    """
    Type of a SMW music entry.
    """

    SONG = ("Song", 109)
    SOUNDTRACK = ("Soundtrack", 110)
    SOUND_EFFECT = ("Sound Effect", 111)
    MISC = ("Misc.", 112)


class SMWSampleUsage(Enum):
    """
    the sample usage of a SMW music entry.
    """

    NONE = ("None", 155)
    LIGHT = ("Light", 156)
    MANY = ("Many", 157)


class SMWSource(Enum):
    """
    the source of a SMW music entry.
    """

    PORT = ("Port", 158)
    REMIX = ("Remix", 159)
    ORIGINAL = ("Original", 160)


class SMWCollection(Enum):
    """
    the collection status of a BRR sample.
    """

    COMPILATION = ("Compilation", 134)
    SINGLE = ("Single", 135)


class SMWSpritesTool(Enum):
    """
    the tool used to create a SMW sprite.
    """

    PIXI = ("PIXI", 142)
    GIEPY = ("GIEPY", 143)
    ROMIS_SPRITE_TOOL = ("Romi's Spritetool", 41)
    OVERWORLD_SPRITE_TOOL = ("Overworld Spritetool", 43)
    OTHER = ("Other", 45)


class SMWSpriteType(Enum):
    """
    Type of a SMW sprite.
    """

    STANDARD = ("Standard", 46)
    SHOOTER = ("Shooter", 47)
    GENERATOR = ("Generator", 48)
    OVERWORLD = ("Overworld", 49)
    CLUSTER = ("Cluster", 64)
    EXTENDED = ("Extended", 65)
    RUN_ONCE = ("Run-Once", 66)
    OTHER = ("Other", 51)


class SMWPatchTool(Enum):
    """
    the tool required to insert a SMW patch.
    """

    XKAS = ("xkas", 1)
    ASAR = ("Asar", 2)
    XKAS_OR_ASAR = ("xkas or Asar", 3)


class SMWFeaturedPatches(Enum):
    """
    if a SMW patch was featured.
    """

    NO = ("No", 70)
    YES = ("Yes", 71)
    ESSENTIAL = ("Essential", 72)


class SMWUberASMType(Enum):
    """
    Type of a SMW UberASM.
    """

    LEVEL = ("Level", 138)
    OVERWORLD = ("Overworld", 139)
    GAME_MODE = ("Game Mode", 140)
    GLOBAL = ("Global", 152)


def get_smwhacks_param(
    name: Optional[str] = None,
    author: Optional[Union[str, List[str]]] = None,
    tags: Optional[Union[str, List[str]]] = None,
    demo: Optional[bool] = None,
    featured: Optional[bool] = None,
    difficulty: Optional[List[SMWDifficulty]] = None,
    desc: Optional[str] = None,
) -> ParamSet:
    """
    Returns a `ParamSet`, which represents the parameters for the SMW hacks section.

    Args:
        name (str, optional): Part of the name of the hack.
        author (str/List[str], optional): The author(s) that contributed to the hack.
        tags (str/List[str], optional): The tag(s) of the hack.
        demo (bool, optional): Whether the hack is a demo.
        featured (bool, optional): Whether the hack was featured.
        difficulty (SMWDifficulty/List[SMWDifficulty], optional): The difficulty of the hack.
        desc (str, optional): Part of the description of the hack.

    Returns:
        ParamSet: The specified parameters for the SMW hacks section.
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
    if featured is not None:
        params.append((featured, ParamField.FEATURED))
    if difficulty is not None:
        params.append((difficulty, ParamField.DIFFICULTY))
    if desc is not None:
        params.append((desc, ParamField.DESCRIPTION))

    return ParamSet(params)


def get_sramdatabase_param(
    name: Optional[str] = None,
    author: Optional[Union[str, List[str]]] = None,
    tags: Optional[Union[str, List[str]]] = None,
) -> ParamSet:
    """
    Returns a `ParamSet`, which represents the parameters for the SRAM database section.

    Args:
        name (str, optional): Part of the name of the SRAM save.
        author (str/List[str], optional): The author(s) that contributed to the SRAM save.
        tags (str/List[str], optional): The tag(s) of the SRAM save.

    Returns:
        ParamSet: The specified parameters for the SRAM database section.
    """
    params = []
    if name is not None:
        params.append((name, ParamField.NAME))
    if author is not None:
        params.append((author, ParamField.AUTHOR))
    if tags is not None:
        params.append((tags, ParamField.TAGS))

    return ParamSet(params)


def get_smwgraphics_param(
    name: Optional[str] = None,
    author: Optional[Union[str, List[str]]] = None,
    tags: Optional[Union[str, List[str]]] = None,
    graphics_type: Optional[List[SMWGraphicsType]] = None,
    purpose: Optional[List[SMWPurpose]] = None,
    slots_used: Optional[List[SMWSlotsUsed]] = None,
    palette_rows_used: Optional[List[SMWPaletteRowsUsed]] = None,
    desc: Optional[str] = None,
) -> ParamSet:
    """
    Returns a `ParamSet`, which represents the parameters for the SMW graphics section.

    Args:
        name (str, optional): Part of the name of the graphic.
        author (str/List[str], optional): The author(s) that contributed to the graphic.
        tags (str/List[str], optional): The tag(s) of the graphic.
        graphics_type (SMWGraphicsType/List[SMWGraphicsType], optional): The type(s) of the graphic.
        purpose (SMWPurpose/List[SMWPurpose], optional): The purpose(s) of the graphic.
        slots_used (SMWSlotsUsed/List[SMWSlotsUsed], optional): The slot(s) used by the graphic.
        palette_rows_used (SMWPaletteRowsUsed/List[SMWPaletteRowsUsed], optional): The palette rows used by the graphic.
        desc (str, optional): Part of the description of the graphic.

    Returns:
        ParamSet: The specified parameters for the SMW graphics section.
    """
    params = []
    if name is not None:
        params.append((name, ParamField.NAME))
    if author is not None:
        params.append((author, ParamField.AUTHOR))
    if tags is not None:
        params.append((tags, ParamField.TAGS))
    if graphics_type is not None:
        params.append((graphics_type, ParamField.TYPE))
    if purpose is not None:
        params.append((purpose, ParamField.PURPOSE))
    if slots_used is not None:
        params.append((slots_used, ParamField.SLOTS))
    if palette_rows_used is not None:
        params.append((palette_rows_used, ParamField.PALETTES))
    if desc is not None:
        params.append((desc, ParamField.DESCRIPTION))

    return ParamSet(params)


def get_smwmusic_param(
    name: Optional[str] = None,
    author: Optional[Union[str, List[str]]] = None,
    tags: Optional[Union[str, List[str]]] = None,
    music_type: Optional[List[SMWMusicType]] = None,
    sample_usage: Optional[List[SMWSampleUsage]] = None,
    source: Optional[List[SMWSource]] = None,
    featured: Optional[bool] = None,
    desc: Optional[str] = None,
) -> ParamSet:
    """
    Returns a `ParamSet`, which represents the parameters for the SMW music section.

    Args:
        name (str, optional): Part of the name of the music entry.
        author (str/List[str], optional): The author(s) that contributed to the music entry.
        tags (str/List[str], optional): The tag(s) of the music entry.
        music_type (SMWMusicType/List[SMWMusicType], optional): The type(s) of the music entry.
        sample_usage (SMWSampleUsage/List[SMWSampleUsage], optional): The sample usage of the music entry.
        source (SMWSource/List[SMWSource], optional): The source(s) of the music entry.
        featured (bool, optional): Whether the music entry was featured.
        desc (str, optional): Part of the description of the music entry.

    Returns:
        ParamSet: The specified parameters for the SMW music section.
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
    if sample_usage is not None:
        params.append((sample_usage, ParamField.SAMPLED))
    if source is not None:
        params.append((source, ParamField.SOURCE_LIST))
    if featured is not None:
        params.append((featured, ParamField.FEATURED))
    if desc is not None:
        params.append((desc, ParamField.DESCRIPTION))

    return ParamSet(params)


def get_brrsamples_param(
    name: Optional[str] = None,
    author: Optional[Union[str, List[str]]] = None,
    tags: Optional[Union[str, List[str]]] = None,
    collection: Optional[List[SMWCollection]] = None,
    desc: Optional[str] = None,
) -> ParamSet:
    """
    Returns a `ParamSet`, which represents the parameters for the BRR samples section.

    Args:
        name (str, optional): Part of the name of the BRR sample.
        author (str/List[str], optional): The author(s) that contributed to the BRR sample.
        tags (str/List[str], optional): The tag(s) of the BRR sample.
        collection (SMWCollection/List[SMWCollection], optional): The collection status of the BRR sample.
        desc (str, optional): Part of the description of the BRR sample.

    Returns:
        ParamSet: The specified parameters for the BRR samples section.
    """
    params = []
    if name is not None:
        params.append((name, ParamField.NAME))
    if author is not None:
        params.append((author, ParamField.AUTHOR))
    if tags is not None:
        params.append((tags, ParamField.TAGS))
    if collection is not None:
        params.append((collection, ParamField.COLLECTION))
    if desc is not None:
        params.append((desc, ParamField.DESCRIPTION))

    return ParamSet(params)


def get_smwblocks_param(
    name: Optional[str] = None,
    author: Optional[Union[str, List[str]]] = None,
    tags: Optional[Union[str, List[str]]] = None,
    act_as: Optional[str] = None,
    includes_gfx: Optional[bool] = None,
    desc: Optional[str] = None,
) -> ParamSet:
    """
    Returns a `ParamSet`, which represents the parameters for the SMW blocks section.

    Args:
        name (str, optional): Part of the name of the block.
        author (str/List[str], optional): The author(s) that contributed to the block.
        tags (str/List[str], optional): The tag(s) of the block.
        act_as (str, optional): What the tile should this block act like.
        includes_gfx (bool, optional): Whether the block includes graphics.
        desc (str, optional): Part of the description of the block.

    Returns:
        ParamSet: The specified parameters for the SMW blocks section.
    """
    params = []
    if name is not None:
        params.append((name, ParamField.NAME))
    if author is not None:
        params.append((author, ParamField.AUTHOR))
    if tags is not None:
        params.append((tags, ParamField.TAGS))
    if act_as is not None:
        params.append((act_as, ParamField.ACTAS))
    if includes_gfx is not None:
        params.append((includes_gfx, ParamField.INCLUDESGFX))
    if desc is not None:
        params.append((desc, ParamField.DESCRIPTION))

    return ParamSet(params)


def get_smwsprites_param(
    name: Optional[str] = None,
    author: Optional[Union[str, List[str]]] = None,
    tags: Optional[Union[str, List[str]]] = None,
    tool: Optional[List[SMWSpritesTool]] = None,
    sprite_type: Optional[List[SMWSpriteType]] = None,
    dynamic: Optional[bool] = None,
    disassembly: Optional[bool] = None,
    includes_gfx: Optional[bool] = None,
    desc: Optional[str] = None,
) -> ParamSet:
    """
    Returns a `ParamSet`, which represents the parameters for the SMW sprites section.

    Args:
        name (str, optional): Part of the name of the sprite.
        author (str/List[str], optional): The author(s) that contributed to the sprite.
        tags (str/List[str], optional): The tag(s) of the sprite.
        tool (SMWSpritesTool/List[SMWSpritesTool], optional): The tool(s) required to insert the sprite.
        sprite_type (SMWSpriteType/List[SMWSpriteType], optional): The type(s) of the sprite.
        dynamic (bool, optional): Whether the sprite is dynamic.
        disassembly (bool, optional): Whether the sprite is a disassembly.
        includes_gfx (bool, optional): Whether the sprite includes graphics.
        desc (str, optional): Part of the description of the sprite.

    Returns:
        ParamSet: The specified parameters for the SMW sprites section.
    """
    params = []
    if name is not None:
        params.append((name, ParamField.NAME))
    if author is not None:
        params.append((author, ParamField.AUTHOR))
    if tags is not None:
        params.append((tags, ParamField.TAGS))
    if tool is not None:
        params.append((tool, ParamField.TOOL))
    if sprite_type is not None:
        params.append((sprite_type, ParamField.TYPE))
    if dynamic is not None:
        params.append((dynamic, ParamField.DYNAMIC))
    if disassembly is not None:
        params.append((disassembly, ParamField.DISASSEMBLY))
    if includes_gfx is not None:
        params.append((includes_gfx, ParamField.INCLUDESGFX))
    if desc is not None:
        params.append((desc, ParamField.DESCRIPTION))

    return ParamSet(params)


def get_smwpatches_param(
    name: Optional[str] = None,
    author: Optional[Union[str, List[str]]] = None,
    tags: Optional[Union[str, List[str]]] = None,
    tool: Optional[List[SMWPatchTool]] = None,
    requires_free_space: Optional[bool] = None,
    bug_fix: Optional[bool] = None,
    featured: Optional[List[SMWFeaturedPatches]] = None,
    desc: Optional[str] = None,
) -> ParamSet:
    """
    Returns a `ParamSet`, which represents the parameters for the SMW patches section.

    Args:
        name (str, optional): Part of the name of the patch.
        author (str/List[str], optional): The author(s) that contributed to the patch.
        tags (str/List[str], optional): The tag(s) of the patch.
        tool (SMWPatchTool/List[SMWPatchTool], optional): The tool(s) required to insert the patch.
        requires_free_space (bool, optional): Whether the patch requires free space.
        bug_fix (bool, optional): Whether the patch is a bug fix in the original game.
        featured (SMWFeaturedPatches/List[SMWFeaturedPatches], optional): Whether the patch was featured.
        desc (str, optional): Part of the description of the patch.

    Returns:
        ParamSet: The specified parameters for the SMW patches section.
    """
    params = []
    if name is not None:
        params.append((name, ParamField.NAME))
    if author is not None:
        params.append((author, ParamField.AUTHOR))
    if tags is not None:
        params.append((tags, ParamField.TAGS))
    if tool is not None:
        params.append((tool, ParamField.TOOL))
    if requires_free_space is not None:
        params.append((requires_free_space, ParamField.FREESPACE))
    if bug_fix is not None:
        params.append((bug_fix, ParamField.BUGFIX))
    if featured is not None:
        params.append((featured, ParamField.FEATURED_LIST))
    if desc is not None:
        params.append((desc, ParamField.DESCRIPTION))

    return ParamSet(params)


def get_uberasm_param(
    name: Optional[str] = None,
    author: Optional[Union[str, List[str]]] = None,
    tags: Optional[Union[str, List[str]]] = None,
    uberasm_type: Optional[List[SMWUberASMType]] = None,
    includes_gfx: Optional[bool] = None,
    includes_hijack: Optional[bool] = None,
    featured: Optional[bool] = None,
    desc: Optional[str] = None,
) -> ParamSet:
    """
    Returns a `ParamSet`, which represents the parameters for the UberASM section.

    Args:
        name (str, optional): Part of the name of the UberASM.
        author (str/List[str], optional): The author(s) that contributed to the UberASM.
        tags (str/List[str], optional): The tag(s) of the UberASM.
        uberasm_type (SMWUberASMType/List[SMWUberASMType], optional): The type(s) of the UberASM.
        includes_gfx (bool, optional): Whether the UberASM includes graphics.
        includes_hijack (bool, optional): Whether the UberASM hijacks or other internal changes to the game.
        featured (bool, optional): Whether the UberASM was featured.
        desc (str, optional): Part of the description of the UberASM.

    Returns:
        ParamSet: The specified parameters for the UberASM section.
    """
    params = []
    if name is not None:
        params.append((name, ParamField.NAME))
    if author is not None:
        params.append((author, ParamField.AUTHOR))
    if tags is not None:
        params.append((tags, ParamField.TAGS))
    if uberasm_type is not None:
        params.append((uberasm_type, ParamField.TYPE))
    if includes_gfx is not None:
        params.append((includes_gfx, ParamField.INCLUDESGFX))
    if includes_hijack is not None:
        params.append((includes_hijack, ParamField.INCLUDESHIJACK))
    if featured is not None:
        params.append((featured, ParamField.FEATURED))
    if desc is not None:
        params.append((desc, ParamField.DESCRIPTION))

    return ParamSet(params)
