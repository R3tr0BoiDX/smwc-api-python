from typing import List, Union
from smwc_types import User, Section


class File:
    """Any type of file on SMW Central"""

    id: int
    section: Section
    name: str
    time: int
    moderated: bool
    authors: List[User]
    submitter: Union[User, None]
    rating: float
    size: int
    downloads: int
    download_url: str
    obsoleted_by: Union[int, None]
    fields: str

    def __init__(self, data: dict) -> None:
        self.id = int(data.get("id"))
        self.section = Section(data.get("section"))
        self.name = data.get("name")
        self.time = int(data.get("time"))
        self.moderated = bool(data.get("moderated"))
        self.authors = []
        for author in data.get("authors"):
            self.authors.append(User(author))
        self.submitter = User(data.get("submitter")) if data.get("submitter") else None
        self.rating = float(data.get("rating"))
        self.size = int(data.get("size"))
        self.downloads = int(data.get("downloads"))
        self.download_url = data.get("download_url")
        self.obsoleted_by = (
            int(data.get("obsoleted_by")) if data.get("obsoleted_by") else None
        )
        self.fields = data.get("fields")
