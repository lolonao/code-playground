import requests

# APIエンドポイントURL
url = "https://api.pro.coins.ph/openapi/v1/ticker/price?symbols=[BTCPHP,DOGEPHP,BONKPHP,SOLPHP]"

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
            formatted_price = f"{price:,.2f}"  # 3桁区切りカンマ挿入と小数点2桁表示
            print(f"{symbol}: {formatted_price}")

    except Exception as error:
        # エラー処理
        print(f"エラーが発生しました: {error}")

async def main():
    await get_price()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
