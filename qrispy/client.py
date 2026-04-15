import requests
from .response import APIResponse
from .exceptions import QrispyError


class Mayar:
    def __init__(self, api_key: str):
        self.base_url = "https://api.mayar.id/hl/v1"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def _request(self, method, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"

        try:
            if method == "GET":
                res = requests.get(url, headers=self.headers, timeout=10)
            else:
                res = requests.post(url, json=payload, headers=self.headers, timeout=10)

            data = res.json()
            return APIResponse(data)

        except requests.RequestException as e:
            raise QrispyError(str(e))

    # 🔹 Balance
    def balance(self):
        return self._request("GET", "/balance")

    # 🔹 Create QRIS
    def create_qris(self, amount: int):
        return self._request("POST", "/qrcode/create", {
            "amount": amount
        })