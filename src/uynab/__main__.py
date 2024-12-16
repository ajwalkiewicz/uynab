from pprint import pprint

from uynab.client import YNABClient
from uynab.service.budget import BudgetService
from uynab.service.payee import PayeeService

client = YNABClient()

budget_service = BudgetService(client=client)
budget_id = budget_service._get_budget_id("Familly")

payee_service = PayeeService(client=client)
# payee = payee_service.get_payee("55d50cdc-6817-4cbf-91fd-fddcd87c5a25")
payees = payee_service.get_all_payees(budget_id=budget_id)

pprint(payees)
