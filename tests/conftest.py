import uuid
from unittest.mock import MagicMock

import pytest

from uynab.client import YNABClient
from uynab.model.payee import Payee


@pytest.fixture
def ynab_client():
    return YNABClient(
        api_token="test_token", base_url="https://api.youneedabudget.com/v1"
    )


@pytest.fixture
def mock_client():
    return MagicMock(spec=YNABClient)


@pytest.fixture
def payee():
    payee_data = {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "name": "Test Payee",
        "transfer_account_id": None,
        "deleted": False,
    }
    return Payee(**payee_data)


@pytest.fixture
def budget_id():
    return uuid.uuid4()
