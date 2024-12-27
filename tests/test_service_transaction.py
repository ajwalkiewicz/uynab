from uuid import UUID

import pytest

from uynab.service.transaction import (
    NewTransaction,
    TransactionDetail,
    TransactionService,
)


@pytest.fixture
def transaction_service(mock_client):
    return TransactionService(mock_client)


@pytest.fixture
def transaction_detail(transaction_detail_data):
    return TransactionDetail(**transaction_detail_data)


@pytest.fixture
def new_transaction(new_transaction_data):
    return NewTransaction(**new_transaction_data)


def test_get_all_transactions(transaction_service, mock_client, transaction_detail):
    budget_id = UUID("12345678-1234-5678-1234-567812345678")

    transaction_1 = transaction_detail
    transaction_1.id = UUID("87654321-4321-8765-4321-876543218765")
    transaction_2 = transaction_detail
    transaction_2.id = UUID("12345678-1234-5678-1234-567812345678")

    mock_response = [transaction_1, transaction_2]
    mock_client.request.return_value = {
        "data": {
            "transactions": mock_response,
            "server_knowledge": 1,
        }
    }

    transactions = transaction_service.get_all_transactions(budget_id)

    assert len(transactions) == 2
    assert transactions[0].id == transaction_1.id
    assert transactions[1].id == transaction_2.id


def test_get_transaction(
    transaction_service, mock_client, transaction_detail, transaction_detail_id
):
    budget_id = UUID("12345678-1234-5678-1234-567812345678")

    mock_client.request.return_value = {"data": {"transaction": transaction_detail}}

    transaction = transaction_service.get_transaction(budget_id, transaction_detail_id)

    assert transaction.id == transaction_detail_id


def test_create_transactions(
    transaction_service, mock_client, new_transaction, transaction_detail
):
    budget_id = UUID("12345678-1234-5678-1234-567812345678")

    mock_client.request.return_value = {
        "data": {
            "transactions": [transaction_detail],
            "server_knowledge": 0,
        },
    }

    created_transaction = transaction_service.create_transactions(
        budget_id, [new_transaction]
    )

    assert created_transaction[0].id == transaction_detail.id


def test_update_transactions(
    transaction_service, mock_client, new_transaction, transaction_detail
):
    budget_id = UUID("12345678-1234-5678-1234-567812345678")

    mock_client.request.return_value = {
        "data": {
            "transaction_ids": [transaction_detail.id],
            "transactions": [transaction_detail],
            "duplicate_import_ids": [],
            "server_knowledge": 0,
        },
    }

    updated_transaction = transaction_service.update_transactions(
        budget_id, [new_transaction]
    )

    assert updated_transaction[0].id == transaction_detail.id


def test_delete_transaction(
    transaction_service, mock_client, transaction_detail, transaction_detail_id
):
    budget_id = UUID("12345678-1234-5678-1234-567812345678")

    mock_client.request.return_value = {"data": {"transaction": transaction_detail}}

    deleted_transaction = transaction_service.delete_transaction(
        budget_id, transaction_detail_id
    )
    assert deleted_transaction.id == transaction_detail_id
