import ccxt
import pandas as pd
import pprint as pp
import colorama

# print(ccxt.exchanges)  # 取引先一覧

coinsph = ccxt.coinsph()
market_coinsph = coinsph.load_markets()

last_bonk: float = coinsph.fetch_ticker('BONK/PHP')['last']
print(f"positioin: 0.001840 last: {last_bonk} 利益: {(last_bonk - 0.001840) * 648979}")

last_sol: float = coinsph.fetch_ticker('SOL/PHP')['last']
print(f"positioin: 0.001840 last: {last_sol} 利益: {(last_sol - 0.001840) * 648979}")
