from helper import convert_yes_no, extract_number

from ._base_field import Field

LENGTH_UNIT = "level"


class YI:
    class Hack(Field):
        demo: bool
        length: int
        description: str

        def __init__(self, data: dict) -> None:
            super().__init__(data)

            # Set new attributes
            fields = data.get("fields")
            self.demo = convert_yes_no(fields.get("demo"))
            self.length = extract_number(fields.get("length"))
            self.description = fields.get("description")
