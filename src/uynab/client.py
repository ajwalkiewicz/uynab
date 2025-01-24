import requests

from uynab.abstract.client import Client
from uynab.config import Config
from uynab.service.account import AccountService
from uynab.service.budget import BudgetService
from uynab.service.category import CategoryService
from uynab.service.payee import PayeeService
from uynab.service.transaction import TransactionService


class YNABClient(Client):
    """
    A client for interacting with the YNAB (You Need A Budget) API.

    Attributes:
        api_token (str): The API token for authenticating requests.
        base_url (str): The base URL for the YNAB API.
        session (requests.Session): The session object for making HTTP requests.

    Methods:
        request(method, endpoint, params=None, data=None):
            Makes an HTTP request to the YNAB API.

    Properties:
        account (AccountService): Returns the account service.
        budget (BudgetService): Returns the budget service.
        category (CategoryService): Returns the category service.
        payee (PayeeService): Returns the payee service.
        transaction (TransactionService): Returns the transaction service.
    """

    def __init__(
        self, api_token: None | str = None, base_url: None | str = None
    ) -> None:
        self.api_token = api_token or Config.API_TOKEN
        self.base_url = base_url or Config.BASE_URL
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.api_token}"})
        self._account = AccountService(self)
        self._budget = BudgetService(self)
        self._category = CategoryService(self)
        self._payee = PayeeService(self)
        self._transaction = TransactionService(self)
        self._verbose = Config.VERBOSE

    def request(
        self,
        method: str,
        endpoint: str,
        params: dict | None = None,
        data: dict | None = None,
    ) -> dict:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.request(method, url, params=params, json=data)
        self._handle_response(response)
        return response.json()

    def _handle_response(self, response: requests.Response) -> None:
        if not response.ok:
            raise APIClientException(
                response.status_code, response.json().get("error", {})
            )

    @property
    def account(self) -> AccountService:
        return self._account

    @property
    def budget(self) -> BudgetService:
        return self._budget

    @property
    def category(self) -> CategoryService:
        return self._category

    @property
    def payee(self) -> PayeeService:
        return self._payee

    @property
    def transaction(self) -> TransactionService:
        return self._transaction


class APIClientException(Exception):
    def __init__(self, status_code: int, error: dict) -> None:
        name = error.get("name") or "Unknown name"
        details = error.get("detail") or "No details"
        super().__init__(f"Error {status_code}: {name} - {details}")
