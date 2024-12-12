class InvalidAPIToken(Exception):
    def __init__(self, token):
        super().__init__(f"Invalid API token was provided: {token}")
