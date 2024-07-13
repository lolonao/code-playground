
import requests
from pydantic import BaseModel, field_validator
import asyncio

# APIエンドポイントURL
url = "https://api.pro.coins.ph/openapi/v1/ticker/price?symbols=[BTCPHP,DOGEPHP,BONKPHP,SOLPHP]"

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
            formatted_price = f"{price_info.price:,.7f}"
            print(f"{price_info.symbol}: {formatted_price}")

    except Exception as error:
        # エラー処理
        print(f"エラーが発生しました: {error}")

# メイン処理 (非同期)
async def main():
    """
    非同期的に価格取得処理を実行する
    """
    await get_price()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
