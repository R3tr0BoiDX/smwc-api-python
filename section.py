from enum import Enum
from typing import List, Tuple, Union

import requests

from smwc_types import Pagination

BASE_URL = "https://www.smwcentral.net/ajax.php"
TIMEOUT = 10


class Section(Enum):
    smw = "smwhacks"
    yi = "yihacks"
    sm64 = "sm64hacks"


class SortBy(Enum):
    ANY = "any"  # for section-dependent sorting
    DATE = "date"
    NAME = "name"
    FILESIZE = "filesize"
    DOWNLOADS = "downloads"


def get_section(
    section: Section,
    moderated: bool = True,
    page_number: int = 0,
    sort: SortBy = SortBy.ANY,
    asc: Union[bool, None] = None,
    filters: Union[List[Tuple[str, str]], None] = None,
) -> Pagination:
    params = {"a": "getsectionlist", "s": section.value, "u": 0 if moderated else 1}

    if page_number > 0:
        params["n"] = page_number

    if sort != SortBy.ANY:
        params["o"] = sort.value

    if isinstance(asc, bool):
        params["d"] = "asc" if asc else "desc"

    if isinstance(filters, list):
        for f in filters:
            print(f)

    response = requests.get(BASE_URL, params=params, timeout=TIMEOUT)

    if response.status_code == 200:
        return Pagination(response.json())

    raise requests.exceptions.HTTPError(
        f"Request failed with status code {response.status_code}"
    )
