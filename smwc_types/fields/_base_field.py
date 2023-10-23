"""
Author: R3tr0BoiDX

Date: 2023-10-18

Description:
    This module contains the base Field class, other fields inherit from this class.
"""
from abc import ABC


class Field(ABC):
    """
    Abstract class, that represents a field on SMW Central.
    Only provides a common interface for all fields, no functionality.
    """
