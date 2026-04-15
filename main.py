from qrispy import Mayar

api = Mayar("YOUR_API_KEY")
# qris = api.create_qris(15000)

# print("Message:", qris.message)
# print("QR URL:", qris.url)
# print("Amount:", qris.amount)

balance = api.balance()

print("Message:", balance.message)
print("Balance:", balance.balance)
print("Balance Pending:", balance.balancePending)
print("Balance Active:", balance.balanceActive)