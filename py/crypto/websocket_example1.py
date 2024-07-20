import websocket
from websocket import web

import json
import pandas as pd
from sqlmodel import create_engine

engine = create_engine('sqlite:///COINS.db')

endpoint = 'wss://stream.binance.com:9443/ws/!miniTicker@arr'

def on_message(ws, message):
    out = json.loads(message)
    print(out)

# TODO: WebSocketApp というクラスは見つからないので、原因を調査する
ws = websocket.WebSocketApp(endpoint, on_message=on_message)
ws.run_forever()
