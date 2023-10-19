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
    HackType,
    GraphicsType,
    Purpose,
    SlotsUsed,
    PaletteRowsUsed,
    SMWMusicType,
    SampleUsage,
    Source,
    Collection,
    SpritesTool,
    SpriteType,
    PatchTool,
    FeaturedSMWPatches,
    UberASMType,
)
from . import smw_filter as SMW

from .yi_filter import YIMusicType, FeaturedYIPatches, SPASMType
from . import yi_filter as YI

from .sm64_filter import Difficulty, TexturesType, Nlist
from . import sm64_filter as SM64
