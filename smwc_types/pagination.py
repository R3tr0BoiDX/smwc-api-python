"""
Author: R3tr0BoiDX

Date: 2023-10-18

Description:
    This module contains the Pagination class, which represents a pagination object from the SMWC API.
    Such a pagination object is returned when requesting a list of files from the API.
    It contains information about the current page, the total amount of pages, the amount of files per page, etc.
    In some sense, this is another representation of a section list page on SMWC.
"""
from typing import List, Union

from smwc_types import File, Token, User


class Pagination:
    """
    Represents a pagination object from the SMWC API.
    Such a pagination object is returned when requesting a list of files from the API.
    It contains information about the current page, the total amount of pages, the amount of files per page, etc.

    Attributes:
        total: Total records in the entire result set.
        per_page: Number of records per page. Usually, there is no way to change this.
        current_page: Page number returned in the current response.
        last_page: Number of the last page.
        first_page_url: URL of the first page. Make a request to this URL to get the first page of the results.
        last_page_url: URL of the last page.
        next_page_url: URL of the next page, or `None` if this response is the last page.
        prev_page_url: URL of the previous page, or `None` if this response is the first page.
        index_from: Index (starting at 1) of the first record in this response. For the first page, this is 1.
        index_to: Index (starting at 1) of the last record in this response. For the last page, this is `total`.
        data: Results, see the specific endpoint for information.
    """

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
