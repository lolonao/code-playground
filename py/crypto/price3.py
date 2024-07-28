import datetime as dt
import time
import json
import asyncio
import requests
from pydantic import BaseModel, field_validator
import schedule


def get_usd_jpy():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = json.loads(response.content)
    exchange_rate = data['rates']['JPY']
    print("USD/PHP exchange rate: ", data['rates']['PHP'])
    return exchange_rate


def get_php_jpy():
    url = 'https://api.exchangerate-api.com/v4/latest/PHP'
    response = requests.get(url)
    data = json.loads(response.content)
    exchange_rate = data['rates']['JPY']
    return exchange_rate


# APIエンドポイントURL
# pairs: str = "symbols=[BTCPHP,SOLPHP,BONKPHP,TRUMPPHP,DOGEPHP]"
# pairs: str = "symbols=[SOLPHP,BONKPHP,TRUMPPHP,SHIBPHP]"
pairs: str = "symbols=[USDTPHP,BTCPHP,SOLPHP,BONKPHP,TRUMPPHP,SHIBPHP]"
url: str = f"https://api.pro.coins.ph/openapi/v1/ticker/price?{pairs}"

# 価格情報モデル
class PriceInfo(BaseModel):
    """
    価格情報を表すモデル

    Attributes:
        symbol (str): シンボル名
        price (float): 価格
    """
    symbol: str
    price: float

    @field_validator("price")
    def validate_price(cls, v):
        """
        price属性の値を検証する

        Args:
            v (float): 価格

        Raises:
            ValueError: priceがfloat型ではない場合、または非負ではない場合
        """
        if not isinstance(v, float):
            raise ValueError("price must be a float")
        if v < 0:
            raise ValueError("price must be non-negative")
        return v

# 価格取得関数 (非同期)
async def get_price():
    """
    APIから価格情報を取得し、フォーマットして表示する

    Raises:
        Exception: エラーが発生した場合
    """
    try:
        # GETリクエスト送信
        response = requests.get(url)
        response.raise_for_status()  # ステータスコードを確認

        # レスポンスデータ取得
        data = response.json()

        # 価格情報を整形して表示
        for item in data:
            price_info = PriceInfo(**item)  # Pydantic モデルに変換
            if price_info.symbol == "BONKPHP" or "SIHBPHP":
                formatted_price = f"{price_info.price:,.7f}"
            else:
                formatted_price = f"{price_info.price:,.2f}"
            print(f"{price_info.symbol}: {formatted_price}")

    except Exception as error:
        # エラー処理
        print(f"エラーが発生しました: {error}")

def job():
    print("1分おきに実行します。")
    print(dt.datetime.now())
    import asyncio
    asyncio.run(main())

# メイン処理 (非同期)
async def main():
    """
    非同期的に価格取得処理を実行する
    """
    usd_jpy = get_usd_jpy()
    print("USD/JPY exchange rate: ", usd_jpy)
    php_jpy = get_php_jpy()
    print("PHP/JPY exchange rate: ", php_jpy)
    print()
    await get_price()
    print("---------")


if __name__ == "__main__":
    import asyncio

    # 毎日午前9時にジョブを実行
    # schedule.every().day.at("09:00").do(job)
    # 1分お気に実行
    schedule.every(1).minutes.do(job)

    while True:
        # スケジュールされたジョブを実行
        schedule.run_pending()
        time.sleep(10)

"""
    url = 'https://api.exchangerate-api.com/v4/latest/PHP'

"""
