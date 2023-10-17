class Token:
    """Docstring for Token."""

    token: str

    def __init__(self, data: dict):
        self.token = data["token"]
