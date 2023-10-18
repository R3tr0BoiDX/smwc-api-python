from typing import List

from filters import HackType
from helper import convert_yes_no, extract_number

from ._base_field import Field

LENGTH_UNIT = "exit"


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
