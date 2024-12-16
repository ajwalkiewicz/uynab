from uynab.abstract.client import Client


class TransactionService:
    def __init__(self, client: Client):
        self.client = client
