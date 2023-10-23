"""
Author: R3tr0BoiDX

Date: 2023-10-18

Description: Any endpoints for the SMWC API
"""
from enum import Enum
from typing import Optional

import requests

from constants import BASE_URL, TIMEOUT
from smwc_filters import ParamSet
from smwc_types import File, Pagination, SortBy, Token


class Endpoints(Enum):
    """
    All endpoints the SMWC API has to offer
    """

    TOKEN = "token"
    SECTION_LIST = "getsectionlist"
    FILE = "getfile"


def get_token() -> str:
    """
    Gets a user token from the SMWC API.
    Certain authenticated non-GET requests may require a CSRF token.

    Returns:
        str: The user token

    Raises:
        requests.exceptions.HTTPError: If the request failed

    Notes:
        Not really any use for this yet, as the API doesn't require auth
        or provides any way of authentication yet.
    """
    raise NotImplementedError("Not really any use for this yet, as theres no auth.")

    # pylint: disable=unreachable
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
    sort: Optional[SortBy] = None,
    asc: Optional[bool] = None,
    filters: Optional[ParamSet] = None,
) -> Pagination:
    """
    Fetches a list of all files in a section. Supports filtering and sorting.

    This endpoint is completely equivalent to the section list page on the website and uses the same URL parameters.
    Use the `smwc_filters` modules to construct URL filter parameters.

    Args:
        section (str): The section to get the page from
        moderated (bool, optional): Whether the files from the page should be moderated
        page_number (int, optional): The page number to get
        sort (Optional[SortBy], optional): After which value to sort
        asc (Optional[bool], optional): Whether to sort ascending or descending
        filters (Optional[ParamSet], optional): The section filters to apply

    Returns:
        Pagination: A pagination object, containing the files from the page and other information.
        See the Pagination class for more information

    Raises:
        requests.exceptions.HTTPError: If the request failed
    """
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

    if isinstance(filters, ParamSet):
        params[str(filters)] = None

    request_params = _construct_params(params)

    response = requests.get(BASE_URL, params=request_params, timeout=TIMEOUT)

    if response.status_code == 200:
        return Pagination(response.json())

    raise requests.exceptions.HTTPError(
        f"Request failed with status code {response.status_code}"
    )


def get_file(file_id: int) -> File:
    """
    Fetches detailed information about a file. The files returned by this posses additional information
    as compared to those which can be retrieved via the section list.
    See the File class for more information.

    Args:
        file_id (int): The file ID to get

    Returns:
        File: The file object with additional information

    Raises:
        requests.exceptions.HTTPError: If the request failed
    """
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


def _construct_params(params: dict) -> str:
    return "&".join([k if v is None else f"{k}={v}" for k, v in params.items()])
