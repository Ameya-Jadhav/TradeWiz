"""
HDFC Sky Authentication Manager
"""

from config.settings import settings
from core.logger import log


class HDFCAuth:
    """
    Handles authentication with HDFC Sky.
    """

    def __init__(self):
        # Credentials
        self.api_key = settings.HDFC_API_KEY
        self.api_secret = settings.HDFC_API_SECRET
        self.client_code = settings.HDFC_CLIENT_CODE

        # Session
        self.access_token = None

        log.info("Authentication Manager initialized")

    @property
    def is_authenticated(self):
        """
        Returns True if an access token is available.
        """
        return self.access_token is not None

    def get_access_token(self):
        """
        Returns the current access token.
        """
        return self.access_token

    def set_access_token(self, access_token):
        """
        Stores a new access token.
        """
        self.access_token = access_token

    def clear_access_token(self):
        """
        Removes the current access token.
        """
        self.access_token = None

    def get_headers(self):
        """
        Returns HTTP headers for authenticated requests.
        """

        if not self.is_authenticated:
            return {}

        return {
            "Authorization": f"Bearer {self.access_token}"
        }