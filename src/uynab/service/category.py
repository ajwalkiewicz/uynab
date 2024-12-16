from uynab.abstract.client import Client


class CategoryService:
    def __init__(self, client: Client):
        self.client = client

    def get_all_categories(self, budget_id: str):
        """Fetch all categories for the specic budget"""
        return self.client.request("GET", f"budgets/{budget_id}/categories")

    def get_category(self, budget_id, category_id: str):
        """Fetch a single budget by ID"""
        return self.client.request(
            "GET", f"budgets/{budget_id}/categories/{category_id}"
        )
