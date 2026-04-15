# Qrispy

Simple Python SDK for QRIS payments in Indonesia.

## Features

- Easy to use QRIS payment integration
- Support for creating QRIS codes
- Check account balance
- Handles both success and error responses gracefully

## Installation

```bash
pip install qrispy
```

## Getting Started with Mayar

This SDK is built for [Mayar](https://bit.ly/daftar-mayar). Here's why we recommend Mayar:

### Why Mayar?
- **Easy Implementation**: Straightforward API integration with minimal setup
- **Personal Verification**: Verify using personal KTP without needing a business entity (PT)
- **Fast Onboarding**: Get started quickly with simple verification process

### Register for Mayar
[👉 Daftar di Mayar - https://bit.ly/daftar-mayar](https://bit.ly/daftar-mayar)

After registration, you'll receive your API Key which you can use with this SDK.

## Quick Start

```python
from qrispy import Mayar

# Initialize the API client with your Mayar API Key
api = Mayar("YOUR_API_KEY")

# Create a QRIS code
qris = api.create_qris(10000)  # amount in rupiah
if qris.status_code == 200:
    print(qris.url)  # QRIS image URL
else:
    print(f"Error: {qris.message}")

# Check balance
balance = api.balance()
if balance.status_code == 200:
    print(f"Balance: {balance.balance}")
else:
    print(f"Error: {balance.message}")
```

## Response Format

All API responses return an `APIResponse` object with the following attributes:

- `status_code`: HTTP status code from the API
- `message`: Response message from the API
- `data`: Dictionary containing the response data
- Dynamic attributes from the response (e.g., `url`, `amount`, `balance`, etc.)

## License

MIT License - see LICENSE file for details

## Author

Ajang Rahmat (ajangrahmat@gmail.com)
