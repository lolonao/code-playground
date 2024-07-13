import requests

# APIエンドポイントURL
symbols: str = 'symbols=[BTCPHP,DOGEPHP,BONKPHP,SOLPHP,SHIBPHP]' 
url = f"https://api.pro.coins.ph/openapi/v1/ticker/price?{symbols}"
# url = "https://api.pro.coins.ph/openapi/v1/ticker/price?symbols=[BTCPHP,DOGEPHP,BONKPHP,SOLPHP]"

# 価格取得関数
async def get_price():
    try:
        # GETリクエスト送信
        response = requests.get(url)
        response.raise_for_status()  # ステータスコードを確認

        # レスポンスデータ取得
        data = response.json()

        # 価格情報を整形して表示
        for item in data:
            symbol = item['symbol']
            price = item['price']

            # 価格をfloat型に変換
            price_float = float(price)

            # フォーマットされた価格とシンボルを結合して表示
            formatted_price = f"{price_float:,.2f}"
            print(f"{symbol}: {formatted_price}")

    except Exception as error:
        # エラー処理
        print(f"エラーが発生しました: {error}")

async def main():
    await get_price()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
