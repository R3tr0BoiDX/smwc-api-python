from urllib.parse import quote_plus

from typing import List

SAFE_CHARS = '"*-.<>_'

# todo: maybe dont use f%5Bname%5D, instead use [name] and encode the brackets...
# todo: ...and return a dict and let request form the url

def form_params(params: dict) -> List[str]:
    if len(params) == 0:
        return ""

    result = []
    for key, value in params.items():
        if isinstance(value, bool):
            result.append(form_bool_param(key, value))
        elif isinstance(value, str):
            result.append(form_str_param(key, value))
        elif isinstance(value, list) and check_list_type(value, int):
            result.append(form_list_param(key, value))
        elif isinstance(value, list) and check_list_type(value, str):
            result.append(form_comma_list_param(key, value))
        else:
            raise TypeError(f"Unsupported type for key '{key}': {type(value)}")

    return flatten_list(result)


def check_list_type(values: list, class_or_tuple: type):
    return all(isinstance(item, class_or_tuple) for item in values)


def form_str_param(name: str, value: str) -> str:
    return f"f%5B{name}%5D={encode_value(value)}"
    # [name]=value
    # example: [name]=value


def form_bool_param(name: str, value: bool) -> str:
    return f"f%5B{name}%5D={1 if value else 0}"
    # [name]=value
    # example: [featured]=1


def form_comma_list_param(name: str, values: List[str]) -> str:
    if len(values) == 0:
        return ""

    param = f"f%5B{name}%5D={encode_value(values[0])}"
    # [name]=value
    # example: [games]=1

    if len(values) > 1:
        for value in values[1:]:
            param += f"%2C+{encode_value(value)}"
            # ,+value
            # example: ,+1,+2,+3

    return param


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


def encode_value(value: str) -> str:
    return quote_plus(value, safe=SAFE_CHARS)
