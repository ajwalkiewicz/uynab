from uuid import UUID

from pydantic import BaseModel

from .payee import Payee


class Budget(BaseModel):
    id: UUID
    name: str
    last_modified_on: str
    first_month: str
    last_month: str
    date_format: dict
    currency_format: dict
    accounts: list[dict]
    payees: list[Payee]
    payee_locations: list[dict]
    category_groups: list[dict]
    categories: list[dict]
    months: list[dict]
    transactions: list[dict]
    subtransactions: list[dict]
    scheduled_transactions: list[dict]
    scheduled_subtransactions: list[dict]


class ResponseDataBudget(BaseModel):
    budget: Budget
    server_knowledge: int


class ResponseBudget(BaseModel):
    data: ResponseDataBudget


class ResponseDataBudgets(BaseModel):
    budgets: list[Budget]
    default_budget: Budget


class ResponseBudgets(BaseModel):
    data: ResponseDataBudgets


class BudgetSettings(BaseModel):
    date_format: dict
    currency_format: dict


class ResponseDataBudgetSettings(BaseModel):
    settings: BudgetSettings


class ResponseBudgetSettings(BaseModel):
    data: ResponseDataBudgetSettings
