# Qrispy - QRIS Payment SDK

**[English](#english) | [Bahasa Indonesia](#bahasa-indonesia)**

---

## English

# Qrispy

Simple Python SDK for QRIS payment integration in Indonesia.

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
[👉 Sign up at Mayar - https://bit.ly/daftar-mayar](https://bit.ly/daftar-mayar)

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

---

## Bahasa Indonesia

# Qrispy

SDK Python sederhana untuk integrasi pembayaran QRIS di Indonesia.

## Fitur

- Integrasi pembayaran QRIS yang mudah digunakan
- Dukungan untuk membuat kode QRIS
- Cek saldo akun
- Menangani respons sukses dan error dengan elegan

## Instalasi

```bash
pip install qrispy
```

## Mulai dengan Mayar

SDK ini dibangun untuk [Mayar](https://bit.ly/daftar-mayar). Berikut alasan kami merekomendasikan Mayar:

### Mengapa Mayar?
- **Implementasi Mudah**: API yang sederhana dengan setup minimal
- **Verifikasi Personal**: Verifikasi menggunakan KTP pribadi tanpa perlu badan usaha (PT)
- **Proses Cepat**: Mulai dengan cepat dengan proses verifikasi yang sederhana

### Daftar di Mayar
[👉 Daftar di Mayar - https://bit.ly/daftar-mayar](https://bit.ly/daftar-mayar)

Setelah registrasi, Anda akan mendapatkan API Key yang dapat digunakan dengan SDK ini.

## Panduan Cepat

```python
from qrispy import Mayar

# Inisialisasi klien API dengan Mayar API Key Anda
api = Mayar("YOUR_API_KEY")

# Buat kode QRIS
qris = api.create_qris(10000)  # jumlah dalam rupiah
if qris.status_code == 200:
    print(qris.url)  # URL gambar QRIS
else:
    print(f"Error: {qris.message}")

# Cek saldo
balance = api.balance()
if balance.status_code == 200:
    print(f"Saldo: {balance.balance}")
else:
    print(f"Error: {balance.message}")
```

## Format Respons

Semua respons API mengembalikan objek `APIResponse` dengan atribut berikut:

- `status_code`: Kode status HTTP dari API
- `message`: Pesan respons dari API
- `data`: Dictionary berisi data respons
- Atribut dinamis dari respons (misal: `url`, `amount`, `balance`, dll)

## Lisensi

MIT License - lihat file LICENSE untuk detail

## Penulis

Ajang Rahmat (ajangrahmat@gmail.com)
