import re

YES_NO_DICT = {"Yes": True, "No": False}


def convert_yes_no(yes_no: str) -> bool:
    return YES_NO_DICT[yes_no]


def extract_number(text: str) -> int:
    return int(re.findall(r"\d+", text)[0])
