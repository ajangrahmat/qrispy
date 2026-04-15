from qrispy import Mayar

api = Mayar("YOUR_API_KEY")

# 🔹 balance
balance = api.balance()
print("Balance:", balance.data)

# 🔹 create QRIS
qris = api.create_qris(10000)

print("QR URL:", qris.url)
print("Amount:", qris.amount)
print("Message:", qris.message)