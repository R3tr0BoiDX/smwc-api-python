"""
Author: R3tr0BoiDX

Date: 2023-10-18

Description: This module contains the Version class, which represents a version of a file on SMW Central.
"""


class Version:
    """
    Represents a version of a file on SMW Central.

    Attributes:
        id (int): File ID of this version.
        name (str): Name of this version.
        obsolete (bool): Whether this version is obsolete.
    """

    id: int
    name: str
    obsolete: bool

    def __init__(self, data: dict) -> None:
        self.id = int(data.get("id"))
        self.name = data.get("name")
        self.obsolete = bool(data.get("obsolete"))
