class Version:
    id: int
    name: str
    obsolete: bool

    def __init__(self, data: dict) -> None:
        self.id = int(data.get("id"))
        self.name = data.get("name")
        self.obsolete = bool(data.get("obsolete"))
