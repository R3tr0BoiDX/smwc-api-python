"""
Author: R3tr0BoiDX

Date: 2023-10-18

Description:
    This module contains the File class, which represents a file on SMW Central.
    It contains information about the file, such as its name, authors, rating, etc.
    This class is used to represent a file in a section list, which is returned
    when calling the `get_section_list` function in `api.py`.
    It contains additional information, such as tags, versions, and images
    if called via the `get_file` function in `api.py`.
"""
from typing import List, Union
from smwc_types import User
from smwc_types.version import Version
from smwc_types.fields import Field, SM64, SMW, YI
from smwc_types.section import Section


class File:
    """
    Represents a file on SMW Central.
    It contains information about the file, such as its name, authors, rating, etc.
    This class is used to represent a file in a section list or a direct file request.
    It contains information, such as ID, section, name, authors, etc.
    It also can contains additional information, such as tags, versions, and images
    when requested directly.

    Attributes:
        id: The files ID
        section: The files section
        name: The files name
        time: Time at which the file was added to the section as UNIX timestamp.
        moderated: Whether the file is moderated
        authors: Authors of the file. Users may be unregistered.
        submitter: For waiting files, user who submitted the file. Always `None` for moderated files.
        rating: File rating, if the section allows ratings.
        size: File size in bytes.
        downloads: Number of downloads.
        download_url: URL at which the file can be downloaded. Make a `GET` request to download the file.
        obsoleted_by: If the file is obsolete (i.e. an update has been submitted), the ID of the newest version.
        fields: Section-specific fields. See `smwc_types/fields` for more information.
        extended: Whether the file possesses additional values
        tags: List of tags on the file.
        versions: The full version history of the file, sorted from newest to oldest.
        images: If the section has images, list of URLs for each image on the file.
    """

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
        elif self.section == Section.YI.HACKS:
            self.fields = YI.Hack(data.get("fields"))
        elif self.section == Section.SM64.HACKS:
            self.fields = SM64.Hack(data.get("fields"))

    def add_additional_values(self, data: dict) -> None:
        self.extended = True
        self.tags = data.get("tags")
        self.versions = []
        for version in data.get("versions"):
            self.versions.append(Version(version))
        self.images = data.get("images")
