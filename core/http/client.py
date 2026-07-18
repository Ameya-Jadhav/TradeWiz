import requests

from requests.exceptions import (
    ConnectionError,
    HTTPError,
    Timeout,
)

from core.http.exceptions import (
    APIError,
    NetworkError,
)

from core.logger import log


class HTTPClient:
    """
    Generic reusable HTTP client.
    """

    def __init__(
        self,
        base_url: str,
        timeout: int = 30,
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        self.session = requests.Session()

        self.session.headers.update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )

        log.info("HTTP Client initialized")

    def _build_url(self, endpoint: str) -> str:
        return f"{self.base_url}{endpoint}"

    def get(self, endpoint: str, **kwargs):

        url = self._build_url(endpoint)

        log.info(f"GET {url}")

        try:
            response = self.session.get(
                url,
                timeout=self.timeout,
                **kwargs,
            )

            response.raise_for_status()

            return response

        except Timeout as e:
            raise NetworkError("Request timed out") from e

        except ConnectionError as e:
            raise NetworkError("Unable to connect to server") from e

        except HTTPError as e:
            raise APIError(str(e)) from e

    def post(self, endpoint: str, **kwargs):

        url = self._build_url(endpoint)

        log.info(f"POST {url}")
  
        try:
            response = self.session.post(
                url,
                timeout=self.timeout,
                **kwargs,
            )

            response.raise_for_status()

            return response

        except Timeout as e:
            raise NetworkError("Request timed out") from e

        except ConnectionError as e:
            raise NetworkError("Unable to connect to server") from e

        except HTTPError as e:
            raise APIError(str(e)) from e

    def close(self):
        self.session.close()

        log.info("HTTP Session closed")