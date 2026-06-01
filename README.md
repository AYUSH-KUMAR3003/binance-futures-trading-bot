# Binance Futures Testnet Trading Bot

## Features
- Market Orders
- Limit Orders
- BUY / SELL
- Input Validation
- Logging
- Error Handling

## Setup

pip install -r requirements.txt

Create .env

API_KEY=xxxxxxxxxxxxxxxx
API_SECRET=xxxxxxxxxxxxxxxx

## Run

python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001

python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 120000

## Assumptions

- Binance Futures Testnet account is active.
- API credentials are available.
- Internet connection is available.
- Only MARKET and LIMIT orders are supported.

## Project Structure

trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
└── .env