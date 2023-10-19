from enum import Enum
from typing import List
from urllib.parse import quote_plus

from api import BASE_URL

SAFE_CHARS = '"*-.<>_'


class ParamType(Enum):
    STR = 1
    BOOL = 2
    LIST = 3
    CSV = 4


class ParamSet:
    # data structure: list[(name, value, type)]
    def __init__(self, params: dict = None):
        self.params = params or {}

    def __str__(self):
        return "&".join(form_params(self.params))


def construct_url(params: str, base_url: str = BASE_URL) -> str:
    full_url = f"{base_url}?{params}"
    return full_url


def form_params(params: list) -> List[str]:
    if len(params) == 0:
        return ""

    result = []
    for param in params:
        key, value, param_type = param

        if param_type == ParamType.BOOL:
            result.append(form_bool_param(key, value))
        elif param_type == ParamType.STR:
            result.append(form_str_param(key, value))
        elif param_type == ParamType.LIST:
            result.append(form_list_param(key, value))
        elif param_type == ParamType.CSV:
            result.append(form_csv_param(key, value))
        else:
            raise TypeError(f"Unsupported type for key '{key}': {param_type}")

    return flatten_list(result)


def form_str_param(name: str, value: str) -> str:
    return f"f%5B{name}%5D={encode_value(value)}"
    # [name]=value
    # example: [name]=value


def form_bool_param(name: str, value: bool) -> str:
    return f"f%5B{name}%5D={1 if value else 0}"
    # [name]=value
    # example: [featured]=1


def form_csv_param(name: str, values: List[str]) -> str:
    if len(values) == 0:
        return ""

    encoded_values = [encode_value(value) for value in values]
    param = f"f%5B{name}%5D={'%2C+'.join(encoded_values)}"
    return param
    # [name]=value1,+value2,+value3
    # example: [games]=1,+2,+3


def form_list_param(name: str, values: List[int]) -> List[str]:
    result = []
    if len(values) == 0:
        return result

    for value in values:
        result.append(f"f%5B{name}%5D%5B%5D={value}")
        # [name][]=value
        # example: [games][]=1&[games][]=2&[games][]=3

    return result


def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


def encode_value(value: str, additional_safe: str = "") -> str:
    return quote_plus(value, safe=SAFE_CHARS + additional_safe)


def check_list_type(values: list, class_or_tuple: type):
    return all(isinstance(item, class_or_tuple) for item in values)
