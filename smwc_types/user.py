from typing import Union


class User:
    id: Union[str, None]
    name: str

    def __init__(self, data: dict) -> None:
        self.id = data.get("id")
        self.name = data.get("name")
