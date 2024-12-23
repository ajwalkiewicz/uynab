import uuid
from unittest.mock import MagicMock
from uuid import UUID

import pytest

from uynab.client import YNABClient
from uynab.model.category import Category, CategoryGroup
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


@pytest.fixture
def category_id():
    return UUID("3fa85f64-5717-4562-b3fc-2c963f66afa6")


@pytest.fixture
def category_data(category_id):
    return {
        "id": category_id,
        "category_group_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "category_group_name": "Test  Category Group",
        "name": "Test Category",
        "hidden": True,
        "original_category_group_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "note": "string",
        "budgeted": 0,
        "activity": 0,
        "balance": 0,
        "goal_type": "TB",
        "goal_needs_whole_amount": None,
        "goal_day": 0,
        "goal_cadence": 0,
        "goal_cadence_frequency": 0,
        "goal_creation_month": "2024-12-22",
        "goal_target": 0,
        "goal_target_month": "2024-12-22",
        "goal_percentage_complete": 0,
        "goal_months_to_budget": 0,
        "goal_under_funded": 0,
        "goal_overall_funded": 0,
        "goal_overall_left": 0,
        "deleted": True,
    }


@pytest.fixture
def category(category_data):
    return Category(**category_data)


@pytest.fixture
def category_group_id():
    return UUID("3fa85f64-5717-4562-b3fc-2c963f66afa6")


@pytest.fixture
def category_group_data(category_group_id, category_data):
    category = Category(**category_data)
    return {
        "id": category_group_id,
        "name": "Test Category Group",
        "hidden": True,
        "deleted": True,
        "categories": [category],
    }


@pytest.fixture
def category_group(category_group_data):
    return CategoryGroup(**category_group_data)
