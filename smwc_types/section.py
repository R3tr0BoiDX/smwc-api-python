"""
Author: R3tr0BoiDX

Date: 2023-10-18

Description: This module contains the all the sections available on SMWC.

TODO: I'm really not a fan of this class structure. Show me a better way.
"""


class Section:
    class SMW:
        HACKS = "smwhacks"
        SAVEBASE = "sramdatabase"
        GRAPHICS = "smwgraphics"
        MUSIC = "smwmusic"
        BRR_SAMPLES = "brrsamples"
        BLOCKS = "smwblocks"
        SPRITES = "smwsprites"
        PATCHES = "smwpatches"
        UBERASM = "uberasm"

    class YI:
        HACKS = "yihacks"
        MUSIC = "yimusic"
        PATCHES = "yipatches"
        SPASM = "spasm"

    class SM64:
        HACKS = "sm64hacks"
        TEXTURES = "sm64textures"
        MUSIC = "sm64music"

    class Generic:
        DOCUMENTS = "documents"
        TOOLS = "tools"
