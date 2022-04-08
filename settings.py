import json

with open("config.json", 'r') as f:
    CONFIG = json.load(f)

TOKEN = "5242973422:AAFu0jOA2HObojRxwFrvP_t73bEApBc6uUo"
TG_API = f"https://api.telegram.org/bot{TOKEN}"

STREAMS = '/'.join([f"{pair.lower()}@miniTicker" for pair in CONFIG])
BINANCE_API = f"wss://stream.binance.com:9443/stream?streams={STREAMS}"
