"""
Author: R3tr0BoiDX

Date: 2023-10-18

Description: Helper functions of any kind
"""
import re

YES_NO_DICT = {"yes": True, "no": False}


def convert_yes_no(yes_no: str) -> bool:
    """
    Converts the strings "Yes" and "No" to their respective boolean values

    Args:
        yes_no (str): The string "Yes" or "No" to convert

    Returns:
        bool: The boolean representation of the string
    """
    return YES_NO_DICT[yes_no.lower()]


def extract_number(text: str) -> int:
    """
    Extracts the first number from a string

    Args:
        text (str): The string to extract the number from

    Returns:
        int: The extracted number
    """
    return int(re.findall(r"\d+", text)[0])
