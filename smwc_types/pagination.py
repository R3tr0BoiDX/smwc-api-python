from typing import List, Union

from smwc_types import File, Token, User


class Pagination:
    total: int
    per_page: int
    current_page: int
    last_page: int
    first_page_url: str
    last_page_url: str
    next_page_url: Union[str, None]
    prev_page_url: Union[str, None]
    index_from: int
    index_to: int
    data: List[Union[User, File, Token]]

    def __init__(self, data: dict) -> None:
        self.total = int(data.get("total"))
        self.per_page = int(data.get("per_page"))
        self.current_page = int(data.get("per_page"))
        self.last_page = int(data.get("last_page"))
        self.first_page_url = data.get("first_page_url")
        self.last_page_url = data.get("last_page_url")
        self.next_page_url = data.get("next_page_url")
        self.prev_page_url = data.get("prev_page_url")
        self.index_from = int(data.get("from"))
        self.index_to = int(data.get("to"))

        self.data = []
        for item in data.get("data"):
            self.data.append(File(item))
