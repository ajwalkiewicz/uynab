from unittest.mock import Mock, patch

import pytest
import requests

from uynab.client import APIClientException, YNABClient
from uynab.service.budget import BudgetService
from uynab.service.category import CategoryService
from uynab.service.payee import PayeeService
from uynab.service.transaction import TransactionService


@pytest.fixture
def client():
    return YNABClient(
        api_token="test_token", base_url="https://api.youneedabudget.com/v1"
    )


def test_client_initialization(client):
    assert client.api_token == "test_token"
    assert client.base_url == "https://api.youneedabudget.com/v1"
    assert isinstance(client.session, requests.Session)
    assert client.session.headers["Authorization"] == "Bearer test_token"
    assert isinstance(client.budget, BudgetService)
    assert isinstance(client.category, CategoryService)
    assert isinstance(client.payee, PayeeService)
    assert isinstance(client.transaction, TransactionService)


@patch("uynab.client.requests.Session.request")
def test_client_request_success(mock_request, client):
    mock_response = Mock()
    mock_response.ok = True
    mock_response.json.return_value = {"data": "test"}
    mock_request.return_value = mock_response

    response = client.request("GET", "test_endpoint")

    assert response == {"data": "test"}
    mock_request.assert_called_once_with(
        "GET", "https://api.youneedabudget.com/v1/test_endpoint", params=None, json=None
    )


@patch("uynab.client.requests.Session.request")
def test_client_request_failure(mock_request, client):
    mock_response = Mock()
    mock_response.ok = False
    mock_response.json.return_value = {
        "error": {"name": "TestError", "detail": "Test detail"}
    }
    mock_response.status_code = 404

    mock_request.return_value = mock_response

    with pytest.raises(APIClientException) as excinfo:
        client.request("GET", "test_endpoint")

    assert str(excinfo.value) == "Error 404: TestError - Test detail"
    mock_request.assert_called_once_with(
        "GET", "https://api.youneedabudget.com/v1/test_endpoint", params=None, json=None
    )


@patch("uynab.client.requests.Session.request")
def test_client_request_failure_unknown_error(mock_request, client):
    mock_response = Mock()
    mock_response.ok = False
    mock_response.json.return_value = {}
    mock_response.status_code = 500

    mock_request.return_value = mock_response

    with pytest.raises(APIClientException) as excinfo:
        client.request("GET", "test_endpoint")

    assert str(excinfo.value) == "Error 500: Unknown name - No details"
    mock_request.assert_called_once_with(
        "GET", "https://api.youneedabudget.com/v1/test_endpoint", params=None, json=None
    )
