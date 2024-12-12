from typing import NoReturn

import requests

from uynab.config import Config


class YNABClient:
    def __init__(
        self, api_token: None | str = None, base_url: None | str = None
    ) -> None:
        self.api_token = api_token or Config.API_TOKEN
        self.base_url = base_url or Config.BASE_URL
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.api_token}"})

    def request(
        self, method: str, endpoint: str, params: dict = None, data: dict = None
    ) -> dict:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.request(method, url, params=params, json=data)
        self._handle_response(response)
        return response.json()

    def _handle_response(self, response: requests.Response) -> NoReturn:
        if not response.ok:
            raise APIClientException(
                response.status_code, response.json().get("error", {})
            )


class APIClientException(Exception):
    def __init__(self, status_code, error) -> None:
        super().__init__(
            f"Error {status_code}: {error.get('name')} - {error.get('detail')}"
        )
