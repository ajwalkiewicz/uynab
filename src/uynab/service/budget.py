from uynab.abstract.client import Client


class BudgetService:
    def __init__(self, client: Client):
        self.client = client

    def get_all_budgets(self):
        """Fetch all budgets"""
        return self.client.request("GET", "budgets")

    def get_budget(self, budget_id: str):
        """Fetch a single budget by ID"""
        return self.client.request("GET", f"budgets/{budget_id}")

    def get_budget_settings(self, budget_id: str):
        """Fetch settings of a single budget"""
        return self.client.request("GET", f"budgets/{budget_id}/settings")

    # Not standard methods

    def _get_budget_by_name(self, budget_name: str):
        all_budgets: list[dict] = self.get_all_budgets()["data"]["budgets"]
        for budget in all_budgets:
            if budget.get("name") == budget_name:
                return budget
        return {}

    def _get_budget_id(self, budgate_name: str):
        budget = self._get_budget_by_name(budgate_name)
        return budget.get("id")
