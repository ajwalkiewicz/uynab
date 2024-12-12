from uynab.client import YNABClient


class PayeeService:
    def __init__(self, client: YNABClient, budget_id: str):
        self.client = client
        self.budget_id = budget_id

    def get_all_payees(self):
        """Fetch all payees for the specic budget"""
        return self.client.request("GET", f"budgets/{self.budget_id}/payees")

    def get_payee(self, payee_id: str):
        """Fetch a single payee by its ID"""
        return self.client.request("GET", f"budgets/{self.budget_id}/payees/{payee_id}")

    def update_payee(self, payee_id: str, new_name: str):
        """Update a single payee"""
        return self.client.request(
            "PATCH",
            f"budgets/{self.budget_id}/payees/{payee_id}",
            data={"payee": {"name": str(new_name)}},
        )
