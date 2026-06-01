from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

def get_client():
    client = Client(
        os.getenv("API_KEY"),
        os.getenv("API_SECRET")
    )

    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    client.timestamp_offset = (
        client.get_server_time()["serverTime"]
        - int(__import__("time").time() * 1000)
    )

    return client
