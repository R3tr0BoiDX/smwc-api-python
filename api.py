from enum import Enum
from typing import List, Tuple, Union

import requests

from smwc_types import Pagination, SortBy, Token, File

BASE_URL = "https://www.smwcentral.net/ajax.php"
TIMEOUT = 10


class Endpoints(Enum):
    TOKEN = "token"
    SECTION_LIST = "getsectionlist"
    FILE = "getfile"


def get_token() -> str:
    raise NotImplementedError("Not really any use for this yet, as theres no auth.")

    response = requests.get(
        BASE_URL, params={"a": Endpoints.TOKEN.value}, timeout=TIMEOUT
    )

    if response.status_code == 200:
        return Token(response.json())

    raise requests.exceptions.HTTPError(
        f"Request failed with status code {response.status_code}"
    )


def get_section_list(
    section: str,
    moderated: bool = True,
    page_number: int = 0,
    sort: Union[SortBy, None] = None,
    asc: Union[bool, None] = None,
    filters: Union[List[Tuple[str, str]], None] = None,
) -> Pagination:
    params = {
        "a": Endpoints.SECTION_LIST.value,
        "s": section,
        "u": 0 if moderated else 1,
    }

    if page_number > 0:
        params["n"] = page_number

    if sort:
        params["o"] = sort.value

    if isinstance(asc, bool):
        params["d"] = "asc" if asc else "desc"

    if isinstance(filters, list):
        for f in filters:
            print(f)

    # todo: construct url on our own
    response = requests.get(BASE_URL, params=params, timeout=TIMEOUT)

    if response.status_code == 200:
        return Pagination(response.json())

    raise requests.exceptions.HTTPError(
        f"Request failed with status code {response.status_code}"
    )


def get_file(file_id: int) -> str:
    params = {
        "a": Endpoints.FILE.value,
        "v": 2,
        "id": file_id,
    }

    response = requests.get(BASE_URL, params=params, timeout=TIMEOUT)

    if response.status_code == 200:
        data = response.json()
        file = File(data)
        file.add_additional_values(data)
        return file

    raise requests.exceptions.HTTPError(
        f"Request failed with status code {response.status_code}"
    )
