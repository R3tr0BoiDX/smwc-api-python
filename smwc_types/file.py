from typing import List, Union
from smwc_types import User
from smwc_types.version import Version
from smwc_types.fields import Field, SM64, SMW
from smwc_types.section import Section


class File:
    """Any type of file on SMW Central"""

    id: int
    section: str
    name: str
    time: int
    moderated: bool
    authors: List[User]
    submitter: Union[User, None]
    rating: Union[float, None]
    size: int
    downloads: int
    download_url: str
    obsoleted_by: Union[int, None]
    fields: Field

    # additional values
    extended: bool = False
    tags: List[str]
    versions: List[Version]
    images: List[str]

    def __init__(self, data: dict) -> None:
        self.id = int(data.get("id"))
        self.section = data.get("section")
        self.name = data.get("name")
        self.time = int(data.get("time"))
        self.moderated = bool(data.get("moderated"))
        self.authors = []
        for author in data.get("authors"):
            self.authors.append(User(author))
        self.submitter = User(data.get("submitter")) if data.get("submitter") else None
        self.rating = float(data.get("rating")) if data.get("rating") else None
        self.size = int(data.get("size"))
        self.downloads = int(data.get("downloads"))
        self.download_url = data.get("download_url")
        self.obsoleted_by = (
            int(data.get("obsoleted_by")) if data.get("obsoleted_by") else None
        )

        if self.section == Section.SMW.HACKS:
            self.fields = SMW.Hack(data.get("fields"))
        elif self.section == Section.SM64.HACKS:
            self.fields = SM64.Hack(data.get("fields"))

    def add_additional_values(self, data: dict) -> None:
        self.extended = True
        self.tags = data.get("tags")
        self.versions = []
        for version in data.get("versions"):
            self.versions.append(Version(version))
        self.images = data.get("images")
