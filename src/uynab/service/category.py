from uynab.client import YNABClient


class CategoryService:
    def __init__(self, client: YNABClient, budget_id: str):
        self.client = client
        self.budget_id = budget_id

    def get_all_categories(self):
        """Fetch all categories for the specic budget"""
        return self.client.request("GET", f"budgets/{self.budget_id}/categories")

    def get_category(self, category_id: str):
        """Fetch a single budget by ID"""
        return self.client.request(
            "GET", f"budgets/{self.budget_id}/categories/{category_id}"
        )
