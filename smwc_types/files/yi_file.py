from smwc_types import File

from helper import convert_yes_no, extract_number

LENGTH_UNIT = "level"


class YIFile(File):
    demo: bool
    length: int
    description: str

    def __init__(self, data: dict) -> None:
        super().__init__(data)

        # Set new attributes
        self.demo = convert_yes_no(data.get("demo"))
        self.length = extract_number(data.get("length"))
        self.description = data.get("description")
