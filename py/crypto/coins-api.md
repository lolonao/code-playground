# Coins.ph API


## すべてのペアを表示

> https://api.pro.coins.ph/openapi/v1/ticker/price?symbol

## SYMBOL PRICE TICKER

> https://api.pro.coins.ph/openapi/v1/ticker/price?symbols=[BTCPHP,DOGEPHP,BONKPHP,SOLPHP]

```json
[{
	"symbol": "BTCPHP",
	"price": "3830000"
}, {
	"symbol": "DOGEPHP",
	"price": "6.962"
}, {
	"symbol": "BONKPHP",
	"price": "0.001218"
}, {
	"symbol": "SOLPHP",
	"price": "8112.2"
}]
```

## SYMBOL ORDER BOOK TICKER
[Rest-Api | Coins.ph](https://coins-docs.github.io/rest-api/#symbol-order-book-ticker)

> https://api.pro.coins.ph/openapi/v1/ticker/bookTicker?symbols=[BTCPHP,DOGEPHP,BONKPHP,SOLPHP]

```json
[
    {
        "symbol": "BTCPHP",
        "bidPrice": "3866293.8",
        "bidQty": "0.0006",
        "askPrice": "3871871",
        "askQty": "0.01182"
    },
    {
        "symbol": "DOGEPHP",
        "bidPrice": "7.202",
        "bidQty": "13952",
        "askPrice": "7.243",
        "askQty": "6174"
    },
    {
        "symbol": "BONKPHP",
        "bidPrice": "0.001248",
        "bidQty": "147719962",
        "askPrice": "0.001257",
        "askQty": "20000000"
    },
    {
        "symbol": "SOLPHP",
        "bidPrice": "8060",
        "bidQty": "0.007",
        "askPrice": "8113",
        "askQty": "5"
    }
]
```


## EXCHANGE INFORMATION

> https://api.pro.coins.ph/openapi/v1/exchangeInfo?symbol=BTCPHP

```json
{
	"timezone": "UTC",
	"serverTime": 1718674623393,
	"exchangeFilters": [],
	"symbols": [{
		"symbol": "BTCPHP",
		"status": "trading",
		"baseAsset": "BTC",
		"baseAssetPrecision": 7,
		"quoteAsset": "PHP",
		"quoteAssetPrecision": 8,
		"orderTypes": ["LIMIT", "MARKET", "LIMIT_MAKER", "STOP_LOSS_LIMIT", "STOP_LOSS", "TAKE_PROFIT_LIMIT", "TAKE_PROFIT"],
		"filters": [{
			"filterType": "PRICE_FILTER",
			"minPrice": "0.1",
			"maxPrice": "99999999999.00000000",
			"tickSize": "0.1"
		}, {
			"filterType": "LOT_SIZE",
			"minQty": "0.0000001",
			"maxQty": "99999999999.00000000",
			"stepSize": "0.0000001"
		}, {
			"filterType": "NOTIONAL",
			"minNotional": "50",
			"maxNotional": "6000000"
		}, {
			"filterType": "MIN_NOTIONAL",
			"minNotional": "50"
		}, {
			"filterType": "STATIC_PRICE_RANGE",
			"priceUp": "99999999.00000000",
			"priceDown": "0.10000000"
		}, {
			"filterType": "PERCENT_PRICE_BY_SIDE",
			"bidMultiplierUp": "5.00000000",
			"bidMultiplierDown": "0.20000000",
			"askMultiplierUp": "5.00000000",
			"askMultiplierDown": "0.20000000"
		}, {
			"filterType": "PERCENT_PRICE_INDEX",
			"multiplierUp": "1.10000000",
			"multiplierDown": "0.90000000"
		}, {
			"filterType": "PERCENT_PRICE_ORDER_SIZE",
			"multiplierUp": "1.10000000",
			"multiplierDown": "0.90000000"
		}, {
			"filterType": "MAX_NUM_ORDERS",
			"maxNumOrders": 200
		}, {
			"filterType": "MAX_NUM_ALGO_ORDERS",
			"maxNumAlgoOrders": 5
		}]
	}]
}
```
