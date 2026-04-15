class APIResponse:
    def __init__(self, raw: dict):
        self.raw = raw
        self.status_code = raw.get("statusCode")
        self.message = raw.get("messages")
        self.data = raw.get("data", {})

        # dot-access magic - set attributes from data
        for k, v in self.data.items():
            setattr(self, k, v)

        # also set top-level attributes that aren't already set
        for k, v in raw.items():
            if k not in ("statusCode", "messages", "data"):
                setattr(self, k, v)

    def __getattr__(self, key):
        # Return None if attribute doesn't exist (safe access)
        return None

    def get(self, key, default=None):
        return self.data.get(key, default)