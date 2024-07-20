import ccxt
import pandas as pd
import pprint as pp

# print(ccxt.exchanges)  # 取引先一覧

coinsph = ccxt.coinsph()
market_coinsph = coinsph.load_markets()
# print(market_coinsph)  # 非常にたくさんの情報が表示されてしまう。
# items = list(market_coinsph.items())[:1]
# pp.pprint(items)

# pp.pprint(market_coinsph.keys())

# symbols = [item for item in market_coinsph if item.endswith('PHP')]
# pp.pprint(symbols)

# df = pd.DataFrame(market_coinsph)
# print(df)


# pp.pprint(coinsph.fetch_tickers())
# pp.pprint(coinsph.fetch_ticker('BONK/PHP')['last'])


last = coinsph.fetch_ticker('BONK/PHP')['last']
print(f"positioin: 0.001840 last: {last} 利益: {(last - 0.001840) * 648979}")
# print((last - 0.001840) * 379561)
# print(379561)
