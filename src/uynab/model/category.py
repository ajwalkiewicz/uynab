"""
# Model category module.

This module defines models for representing financial categories and category groups within a budgeting application.

Classes:
    Category: Represents a financial category with various attributes such as id, name, budgeted amount, and goal details.
    ResponseDataCategory: Represents the response data for a single category.
    ResponseCategory: Represents the response structure for a category.
    CategoryGroup: Represents a group of categories with attributes such as id, name, and a list of categories.
    ResponseDataCategoryGroup: Represents the response data for a category group, including server knowledge.
    ResponseCategoryGroup: Represents the response structure for a category group.

Each class uses Pydantic's BaseModel to enforce type validation and provide serialization/deserialization capabilities.
"""

from typing import Literal, Optional
from uuid import UUID

from pydantic import BaseModel


class Category(BaseModel):
    """
    Represents a financial category within a budgeting application.

    Attributes:
        id (UUID): Unique identifier for the category.
        category_group_id (UUID): Identifier for the group this category belongs to.
        category_group_name (str): Name of the group this category belongs to.
        name (str): Name of the category.
        hidden (bool): Indicates if the category is hidden.
        original_category_group_id (UUID): Original identifier for the group this category belongs to.
        note (str): Additional notes about the category.
        budgeted (int): Amount budgeted for this category.
        activity (int): Amount of activity (transactions) in this category.
        balance (int): Current balance of the category.
        goal_type (str): Type of goal associated with the category. Default is "TB".
        goal_needs_whole_amount (Optional[bool]): Indicates if the goal needs the whole amount.
        goal_day (int): Day of the month associated with the goal.
        goal_cadence (int): Cadence of the goal.
        goal_cadence_frequency (int): Frequency of the goal cadence.
        goal_creation_month (str): Month when the goal was created.
        goal_target (int): Target amount for the goal.
        goal_target_month (str): Target month for the goal.
        goal_percentage_complete (int): Percentage of the goal that has been completed.
        goal_months_to_budget (int): Number of months to budget for the goal.
        goal_under_funded (int): Amount underfunded for the goal.
        goal_overall_funded (int): Overall amount funded for the goal.
        goal_overall_left (int): Overall amount left to fund for the goal.
        deleted (bool): Indicates if the category has been deleted.
    """

    id: UUID
    category_group_id: UUID
    category_group_name: str
    name: str
    hidden: bool
    original_category_group_id: Optional[UUID]
    note: Optional[str]
    budgeted: int
    activity: int
    balance: int
    goal_type: Optional[Literal["TB", "TBD", "MF", "NEED", "DEBT"]]
    goal_needs_whole_amount: Optional[bool]
    goal_day: Optional[int]
    goal_cadence: Optional[int]
    goal_cadence_frequency: Optional[int]
    goal_creation_month: Optional[str]
    goal_target: Optional[int]
    goal_target_month: Optional[str]
    goal_percentage_complete: Optional[int]
    goal_months_to_budget: Optional[int]
    goal_under_funded: Optional[int]
    goal_overall_funded: Optional[int]
    goal_overall_left: Optional[int]
    deleted: bool


class ResponseDataCategory(BaseModel):
    """
    ResponseDataCategory is a model that represents the response data for a category.

    Attributes:
        category (Category): The category object associated with the response.
    """

    category: Category


class ResponseCategory(BaseModel):
    """
    ResponseCategory is a model representing the response structure for a category.

    Attributes:
        data (ResponseDataCategory): The data attribute containing the category details.
    """

    data: ResponseDataCategory


class CategoryGroup(BaseModel):
    """
    Represents a group of categories in the budgeting application.

    Attributes:
        id (UUID): The unique identifier of the category group.
        name (str): The name of the category group.
        hidden (bool): Indicates whether the category group is hidden.
        deleted (bool): Indicates whether the category group is deleted.
        categories (list[Category]): A list of categories that belong to this group.
    """

    id: UUID
    name: str
    hidden: bool
    deleted: bool
    categories: list[Category]


class ResponseDataCategoryGroup(BaseModel):
    """
    ResponseDataCategoryGroup represents the response data for a category group.

    Attributes:
        category_groups (list[CategoryGroup]): A list of category groups.
        server_knowledge (int): The server knowledge value.
    """

    category_groups: list[CategoryGroup]
    server_knowledge: int


class ResponseCategoryGroup(BaseModel):
    """
    ResponseCategoryGroup represents a category group in the response model.

    Attributes:
        data (ResponseDataCategoryGroup): The data associated with the category group.
    """

    data: ResponseDataCategoryGroup
