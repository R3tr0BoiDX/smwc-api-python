"""
Author: R3tr0BoiDX

Date: 2023-10-18

Description: This file contains any sorting order that can be used to sort the files in the API.
"""
from enum import Enum


class SortBy(Enum):
    """
    Value to sort the results by,
    """
    DATE = "date"
    NAME = "name"
    FILESIZE = "filesize"
    DOWNLOADS = "downloads"
