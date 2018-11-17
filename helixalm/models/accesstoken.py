"""Model of a AccessToken object."""

from datetime import datetime


class AccessToken:

    def __init__(self, token_type: str, expires_on: str, access_token: str):
        """Contains information about a Helix ALM project."""
        self.token_type = token_type
        self.expires_on = datetime.fromisoformat(expires_on)
        self.access_token = access_token

    # TODO: Create get(@class)/post/update methods where appropriate.
