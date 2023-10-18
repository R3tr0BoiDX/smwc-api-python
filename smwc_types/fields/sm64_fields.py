from ._base_field import Field

from helper import convert_yes_no, extract_number

LENGTH_UNIT = "level"


class SM64:
    class Hack(Field):
        demo: bool
        length: int
        description: str

        def __init__(self, data: dict) -> None:
            self.demo = convert_yes_no(data.get("demo"))
            self.length = extract_number(data.get("length"))
            self.description = data.get("description")
            # todo: there are more fields
