"""
Author: R3tr0BoiDX

Date: 2023-10-18

Description:
    This module contains the SM64 class, which represents any SM64 file on SMW Central.
    For every section, there is a corresponding SM64 subclass, which contains
    section-specific information.

TODO: Add remaining SM64 section-specific fields
"""

from ._base_field import Field

from helper import convert_yes_no, extract_number

LENGTH_UNIT = "level"


class SM64:
    class Hack(Field):
        demo: bool
        length: int
        description: str

        def __init__(self, data: dict) -> None:
            self.demo = convert_yes_no(data.get("demo"))
            self.length = extract_number(data.get("length"))
            self.description = data.get("description")
            # todo: there are more fields
