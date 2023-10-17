from enum import Enum
from smwc_types import File
from typing import List

from helper import convert_yes_no, extract_number

LENGTH_UNIT = "exit"


class Difficulty(Enum):
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


class SMWFile(File):
    demo: bool
    featured: bool
    length: int
    difficulties: List[Difficulty]

    def __init__(self, data: dict) -> None:
        super().__init__(data)

        # Set new attributes
        self.demo = convert_yes_no(data.get("demo"))
        self.featured = convert_yes_no(data.get("featured"))
        self.length = extract_number(data.get("length"))
        self.difficulties = get_difficulties(data.get("difficulty"))
        self.description = data.get("description")


def get_difficulties(difficulty_raw: str) -> List[Difficulty]:
    difficulties = difficulty_raw.split(", ")

    for difficulty in difficulties:
        return difficulty_string_to_enum(difficulty)


def difficulty_string_to_enum(value: str) -> Difficulty:
    for difficulty in Difficulty:
        if difficulty.value[0] == value:
            return difficulty
