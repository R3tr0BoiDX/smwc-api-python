from smwc_types import File

from helper import convert_yes_no, extract_number

LENGTH_UNIT = "level"


class SM64File(File):
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
