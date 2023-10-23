from .generic_filter import (
    DocumentType,
    FeaturedTool,
    Game,
    Language,
    OperatingSystem,
    Platform,
)
from . import generic_filter as Generic

from .smw_filter import (
    SMWDifficulty,
    SMWGraphicsType,
    SMWPurpose,
    SMWSlotsUsed,
    SMWPaletteRowsUsed,
    SMWMusicType,
    SMWSampleUsage,
    SMWSource,
    SMWCollection,
    SMWSpritesTool,
    SMWSpriteType,
    SMWPatchTool,
    SMWFeaturedPatches,
    SMWUberASMType,
)
from . import smw_filter as SMW

from .yi_filter import YIMusicType, YIFeaturedPatches, YISPASMType
from . import yi_filter as YI

from .sm64_filter import SM64Difficulty, SM64TexturesType, SM64Nlist
from . import sm64_filter as SM64

from ._generator import ParamSet
