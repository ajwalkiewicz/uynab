from pprint import pprint

from uynab.client import YNABClient
from uynab.service.budget import BudgetService
from uynab.service.category import CategoryService
from uynab.service.payee import PayeeService

client = YNABClient()

budget_service = BudgetService(client=client)
budget_id = budget_service.get_budget_id("Familly")

category_service = CategoryService(client=client, budget_id=budget_id)
categories = category_service.get_all_categories()

print(categories)

payee_service = PayeeService(client=client, budget_id=budget_id)
payee_service.update_payee("55d50cdc-6817-4cbf-91fd-fddcd87c5a25", "Adam")

payees = payee_service.get_all_payees()
pprint(payees)
