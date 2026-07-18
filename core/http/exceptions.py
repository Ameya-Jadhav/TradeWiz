class HTTPError(Exception):
    """Base HTTP exception."""
    pass


class NetworkError(HTTPError):
    """Network communication failed."""
    pass


class APIError(HTTPError):
    """Broker API returned an error."""
    pass


class AuthenticationError(APIError):
    """Authentication failed."""
    pass