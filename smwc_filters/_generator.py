"""
Author: R3tr0BoiDX

Date: 2023-10-18

Description:
    This module contains the ParamSet class, which represents a set of parameters
    which are used to filter SMW files on SMW Central. It also contains the ParamField
    and ParamType enums, which are used to specify the type of a parameter.
    Furthermore, it contains functions to construct a URL from a ParamSet.

TODOs:
    todo: Submodule for every section
    todo: Adjust all get_param functions accept union for enum and list of enum, in case of a list
"""

from enum import Enum
from typing import Any, List, Tuple, Union
from urllib.parse import quote_plus

SAFE_CHARS = '"*-.<>_'


class ParamType(Enum):
    """
    Type of a parameter.
    """

    STRING = 1
    BOOL = 2
    LIST = 3
    CSV = 4


# todo: recheck with new API specification
class ParamField(Enum):
    """
    a parameter on SMW Central.
    It contains the name and type of each parameter.
    """

    ACTAS = ("actas", ParamType.STRING)
    AUTHOR = ("author", ParamType.CSV)
    BUGFIX = ("bugfix", ParamType.BOOL)
    COLLECTION = ("collection", ParamType.LIST)
    CUSTOM = ("custom", ParamType.BOOL)
    DEMO = ("demo", ParamType.BOOL)
    DESCRIPTION = ("description", ParamType.STRING)
    DIFFICULTY = ("difficulty", ParamType.LIST)
    DISASSEMBLY = ("disassembly", ParamType.BOOL)
    DYNAMIC = ("dynamic", ParamType.BOOL)
    FEATURED = ("featured", ParamType.BOOL)
    FEATURED_LIST = ("featured", ParamType.LIST)
    FREESPACE = ("freespace", ParamType.BOOL)
    GAMES = ("games", ParamType.LIST)
    INCLUDESGFX = ("includesgfx", ParamType.BOOL)
    INCLUDESHIJACK = ("includeshijack", ParamType.BOOL)
    LANGUAGE = ("language", ParamType.LIST)
    NAME = ("name", ParamType.STRING)
    NLIST = ("nlist", ParamType.LIST)
    OS = ("os", ParamType.LIST)
    PALETTES = ("palettes", ParamType.LIST)
    PLATFORMS = ("platforms", ParamType.LIST)
    PURPOSE = ("purpose", ParamType.LIST)
    SAMPLED = ("sampled", ParamType.BOOL)
    SAMPLES = ("samples", ParamType.LIST)
    SLOTS = ("slots", ParamType.LIST)
    SOURCE = ("source", ParamType.BOOL)
    SOURCE_LIST = ("source", ParamType.LIST)
    TAGS = ("tags", ParamType.CSV)
    TOOL = ("tool", ParamType.LIST)
    TYPE = ("type", ParamType.LIST)


class ParamSet:
    """
    Represents a set of parameters, which are used to filter files on SMW Central.
    """

    def __init__(self, params: List[Tuple[Any, ParamField]] = None):
        self.params = params or {}

    def __str__(self):
        return "&".join(_form_params(self.params))


def _form_params(params: list) -> List[str]:
    """
    Forms a list of parameters from a list of tuples.
    Each tuple contains the value and the field of a parameter.
    The field is an instance of the `ParamField` enum, which specifies the type and name of the parameter.
    The function returns a list of strings, which are the parameters.

    Args:
        params (list): List of tuples, which contain the value and field of a parameter.

    Returns:
        List[str]: List of strings, which can be linked together to form a URL.
    """
    if len(params) == 0:
        return ""

    result = []
    for param in params:
        value, field = param
        name, param_type = field.value

        if param_type == ParamType.BOOL:
            result.append(_form_bool_param(name, value))
        elif param_type == ParamType.STRING:
            result.append(_form_str_param(name, value))
        elif param_type == ParamType.LIST:
            result.append(_form_list_param(name, value))
        elif param_type == ParamType.CSV:
            result.append(_form_csv_param(name, value))
        else:
            raise TypeError(f"Unsupported type for key '{name}': {param_type}")

    return _flatten_list(result)


def _form_str_param(name: str, value: str) -> str:
    """
    Forms a parameter from a name and a string value.

    Args:
        name (str): Name of the parameter.
        value (str): Value of the parameter.

    Returns:
        str: Formed parameter string.
    """
    return f"f%5B{name}%5D={_encode_value(value)}"
    # [name]=value
    # example: [name]=value


def _form_bool_param(name: str, value: bool) -> str:
    """
    Forms a parameter from a name and a boolean value.

    Args:
        name (str): Name of the parameter.
        value (bool): Value of the parameter.

    Returns:
        str: Formed parameter string.
    """
    return f"f%5B{name}%5D={1 if value else 0}"
    # [name]=value
    # example: [featured]=1


def _form_csv_param(name: str, values: Union[str, List[str]]) -> str:
    """
    Forms a parameter from a name and a string or list of strings.

    Args:
        name (str): Name of the parameter.
        values (Union[str, List[str]]): (List of) value(s) of the parameter.

    Returns:
        str: Formed CSV parameter string.
    """
    # convert single enum to list
    if isinstance(values, str):
        values = [values]

    if len(values) == 0:
        return ""

    encoded_values = [_encode_value(value) for value in values]
    param = f"f%5B{name}%5D={'%2C+'.join(encoded_values)}"
    return param
    # [name]=value1,+value2,+value3
    # example: [games]=1,+2,+3


def _form_list_param(name: str, values: Union[Enum, List[Enum]]) -> List[str]:
    """
    Forms a parameter from a name and an enum or list of enums.

    Args:
        name (str): Name of the parameter.
        values (Union[Enum, List[Enum]]): (List of) value(s) of the parameter.

    Returns:
        List[str]: Formed list parameter strings.
    """
    # convert single enum to list
    if isinstance(values, Enum):
        values = [values]

    result = []
    if len(values) == 0:
        return result

    values = [value.value[1] for value in values]
    for value in values:
        result.append(f"f%5B{name}%5D%5B%5D={value}")
        # [name][]=value
        # example: [games][]=1&[games][]=2&[games][]=3

    return result


def _flatten_list(nested_list):
    """
    Flattens a nested list.

    Args:
        nested_list (list): Nested list to flatten.

    Returns:
        list: Flattened list.
    """
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(_flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


def _encode_value(value: str, additional_safe: str = "") -> str:
    """
    Encodes a string for a URL.

    Args:
        value (str): String to encode.
        additional_safe (str, optional): Additional characters to encode. Defaults to "".

    Returns:
        str: URL safe encoded string.
    """
    return quote_plus(value, safe=SAFE_CHARS + additional_safe)


# pylint: disable=pointless-string-statement
"""
Param field statistics:
-----------------------------------------------------
COUNT    | LINE
-----------------------------------------------------
      18 | author, STRING
      18 | name, STRING
      18 | tags, CSV
      17 | description, STRING
       9 | type, LIST
       6 | featured, BOOL
       3 | demo, BOOL
       3 | includesgfx, BOOL
       2 | bugfix, BOOL
       2 | featured, LIST
       2 | freespace, BOOL
       2 | games, LIST
       2 | includeshijack, BOOL
       2 | platforms, LIST
       2 | tool, LIST
       1 | actas, STRING
       1 | collection, LIST
       1 | custom, BOOL
       1 | difficulty, LIST
       1 | disassembly, BOOL
       1 | dynamic, BOOL
       1 | language, LIST
       1 | nlist, LIST
       1 | os, LIST
       1 | palettes, LIST
       1 | purpose, LIST
       1 | sampled, BOOL
       1 | samples, LIST
       1 | slots, LIST
       1 | source, BOOL
       1 | source, LIST
-----------------------------------------------------
     122 | TOTAL PARAMS
      31 | DISTINCT PARAMS
"""
