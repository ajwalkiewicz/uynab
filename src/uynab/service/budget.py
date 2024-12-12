from uynab.client import YNABClient


class BudgetService:
    def __init__(self, client: YNABClient):
        self.client = client

    def get_all_budgets(self):
        """Fetch all budgets"""
        return self.client.request("GET", "budgets")

    def get_budget_by_id(self, budget_id: str):
        """Fetch a single budget by ID"""
        return self.client.request("GET", f"budgets/{budget_id}")

    def get_budget_by_name(self, budget_name: str):
        all_budgets: list[dict] = self.get_all_budgets()["data"]["budgets"]
        for budget in all_budgets:
            if budget.get("name") == budget_name:
                return budget
        return {}

    def get_budget_id(self, budgate_name: str):
        budget = self.get_budget_by_name(budgate_name)
        return budget.get("id")

    def get_budget_settings(self, budget_id: str):
        """Fetch settings of a single budget"""
        return self.client.request("GET", f"budgets/{budget_id}/settings")
