from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from .category import Category


class Account(BaseModel):
    """
    Account model representing a financial account.

    Attributes:
        id (UUID): Unique identifier for the account.
        name (str): Name of the account.
        type (str): Type of the account (e.g., checking, savings).
        on_budget (bool): Indicates if the account is on budget.
        closed (bool): Indicates if the account is closed.
        note (Optional[str]): Additional notes about the account.
        balance (int): Current balance of the account.
        cleared_balance (int): Cleared balance of the account.
        uncleared_balance (int): Uncleared balance of the account.
        transfer_payee_id (UUID): Identifier for the transfer payee.
        direct_import_linked (bool): Indicates if the account is linked for direct import.
        direct_import_in_error (bool): Indicates if there is an error with direct import.
        last_reconciled_at (Optional[str]): Timestamp of the last reconciliation.
        debt_original_balance (Optional[int]): Original balance of the debt.
        debt_interest_rates (dict[datetime, int]): Interest rates of the debt over time.
        debt_minimum_payments (dict[datetime, int]): Minimum payments of the debt over time.
        debt_escrow_amounts (dict[datetime, int]): Escrow amounts of the debt over time.
        deleted (bool): Indicates if the account is deleted.
    """

    id: UUID
    name: str
    type: str
    on_budget: bool
    closed: bool
    note: Optional[str]
    balance: int
    cleared_balance: int
    uncleared_balance: int
    transfer_payee_id: UUID
    direct_import_linked: bool
    direct_import_in_error: bool
    last_reconciled_at: Optional[str]
    debt_original_balance: Optional[int]
    debt_interest_rates: dict[datetime, int]
    debt_minimum_payments: dict[datetime, int]
    debt_escrow_amounts: dict[datetime, int]
    deleted: bool


class DateFormat(BaseModel):
    """A class used to represent a Date Format.

    Attributes:
        format (str): A string representing the date format.
    """

    format: str


class CurrencyFormat(BaseModel):
    """
    CurrencyFormat is a model that represents the formatting details for a specific currency.

    Attributes:
        iso_code (str): The ISO 4217 code for the currency (e.g., 'USD' for US Dollar).
        example_format (str): An example of how the currency is formatted (e.g., '$1,234.56').
        decimal_digits (int): The number of decimal digits used in the currency (e.g., 2 for USD).
        decimal_separator (str): The character used to separate the integer part from the fractional part (e.g., '.' for USD).
        symbol_first (bool): Indicates whether the currency symbol appears before the amount (True) or after (False).
        group_separator (str): The character used to separate groups of thousands (e.g., ',' for USD).
        currency_symbol (str): The symbol used to represent the currency (e.g., '$' for USD).
        display_symbol (bool): Indicates whether the currency symbol should be displayed (True) or not (False).
    """

    iso_code: str
    example_format: str
    decimal_digits: int
    decimal_separator: str
    symbol_first: bool
    group_separator: str
    currency_symbol: str
    display_symbol: bool


class Month(BaseModel):
    """
    Represents a financial month with various attributes.

    Attributes:
        month (datetime): The month this instance represents.
        note (Optional[str]): An optional note for the month.
        income (int): The total income for the month.
        budgeted (int): The total amount budgeted for the month.
        activity (int): The total financial activity for the month.
        to_be_budgeted (int): The amount left to be budgeted for the month.
        age_of_money (int): The age of money in days.
        deleted (bool): Indicates if the month record is deleted.
        categories (list[Category]): A list of categories associated with the month.
    """

    month: datetime
    note: Optional[str]
    income: int
    budgeted: int
    activity: int
    to_be_budgeted: int
    age_of_money: int
    deleted: bool
    categories: list[Category]
