from enum import Enum
from typing import List

# from filters.smw_filter import HackType
from helper import convert_yes_no, extract_number

from ._base_field import Field

LENGTH_UNIT = "exit"


# todo: remove this
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


class SMW:
    class Hack(Field):
        demo: bool
        featured: bool
        length: int
        difficulties: List[HackType]

        def __init__(self, data: dict) -> None:
            self.demo = convert_yes_no(data.get("demo"))
            self.featured = convert_yes_no(data.get("featured"))
            self.length = extract_number(data.get("length"))
            self.difficulties = get_difficulties(data.get("difficulty"))
            self.description = data.get("description")


def get_difficulties(difficulty_raw: str) -> List[HackType]:
    difficulties = difficulty_raw.split(", ")

    for difficulty in difficulties:
        return difficulty_string_to_enum(difficulty)


def difficulty_string_to_enum(value: str) -> HackType:
    for difficulty in HackType:
        if difficulty.value[0] == value:
            return difficulty
