"""
Author: R3tr0BoiDX

Date: 2023-10-18

Description: Token class for the SMWC API.
"""


class Token:
    """
    Represents a user token from the SMWC API.

    Attributes:
        token: Current CSRF token for the authenticated user. This periodically changes.
    """

    token: str

    def __init__(self, data: dict):
        self.token = data["token"]
