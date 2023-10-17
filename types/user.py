from typing import Union


class User:
    """
    A user on SMC Central

    - id: number | null
        User ID on SMW Central.
        Some User objects may refer to unregistered users, in which case this is null.
        References to a User will explicitly state whether this is possible.

    - name: string
        Username. If the user is registered, this will be their SMW Central username.
    """

    id: Union[str, None]
    name: str

    def __init__(self, data: dict) -> None:
        self.id = data.get("id")
        self.name = data.get("name")
