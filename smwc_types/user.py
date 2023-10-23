"""
Author: R3tr0BoiDX

Date: 2023-10-18

Description: This module contains the User class, which is used to represent a user on SMWC.
"""
from typing import Union


class User:
    """
    Represents a user on SMWC.

    Attributes:
        id: User ID on SMW Central. For unregistered users, this will be `None`.
        name: If the user is registered, this will be their SMW Central username.
    """

    id: Union[str, None]
    name: str

    def __init__(self, data: dict) -> None:
        self.id = data.get("id")
        self.name = data.get("name")
