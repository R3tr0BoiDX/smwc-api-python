from enum import Enum
from typing import Any, List, Tuple, Union
from urllib.parse import quote_plus

from constants import BASE_URL

SAFE_CHARS = '"*-.<>_'

# todo: submodule for every section
# todo: adjust all get_param functions to have union for enum and list of enum


class ParamType(Enum):
    STRING = 1
    BOOL = 2
    LIST = 3
    CSV = 4


# todo: recheck with new API specification
class ParamField(Enum):
    ACTAS = ("actas", ParamType.STRING)
    AUTHOR = ("author", ParamType.STRING)
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
    def __init__(self, params: List[Tuple[Any, ParamField]] = None):
        self.params = params or {}

    def __str__(self):
        return "&".join(_form_params(self.params))


def construct_url(params: str, base_url: str = BASE_URL) -> str:
    full_url = f"{base_url}?{params}"
    return full_url


def _form_params(params: list) -> List[str]:
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
    return f"f%5B{name}%5D={_encode_value(value)}"
    # [name]=value
    # example: [name]=value


def _form_bool_param(name: str, value: bool) -> str:
    return f"f%5B{name}%5D={1 if value else 0}"
    # [name]=value
    # example: [featured]=1


def _form_csv_param(name: str, values: Union[str, List[str]]) -> str:
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
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(_flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


def _encode_value(value: str, additional_safe: str = "") -> str:
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
