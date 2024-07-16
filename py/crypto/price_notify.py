import asyncio
import time
from pydantic import BaseModel, field_validator
import requests

import schedule
import datetime as dt

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
        results = []
        for item in data:
            price_info = PriceInfo(**item)  # Pydantic モデルに変換
            if price_info.symbol == "BONKPHP" or "SIHBPHP":
                formatted_price = f"{price_info.price:,.7f}"
            else:
                formatted_price = f"{price_info.price:,.2f}"
            results.append(f"{price_info.symbol}: {formatted_price}")
            # print(f"{price_info.symbol}: {formatted_price}")
        return results

    except Exception as error:
        # エラー処理
        print(f"エラーが発生しました: {error}")

def job():
    print("1分おきに実行します。")
    print(dt.datetime.now())
    # import asyncio
    asyncio.run(main())


#########

# 発行された LINE Notifyトークン
LINE_NOTIFY_TOKEN = "uzGHMbOhqza0RUuNKwdfKXv2kc714DEJCVzFrDUXIMP"

def send_notify(msg):
    """LINE Notifyへメッセージを送信する関数

    Args:
        msg (str): 送信するメッセージ

    """
    try:
        # サーバーに送るパラメータを用意
        url = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': 'Bearer ' + LINE_NOTIFY_TOKEN}
        payload = {'message': msg}

        # requestsモジュールのpost関数を利用してメッセージを送信する
        # ヘッダにトークン情報，パラメータにメッセージを指定する
        requests.post(url, headers=headers, params=payload)

        print('LINE Notifyへメッセージを送信しました:', msg)
    except Exception as e:
        # エラーが発生した場合、エラー内容をLINE Notifyで通知する
        error_msg = f'LINE Notifyへのメッセージ送信中にエラーが発生しました: {e}'
        send_notify(error_msg)
        raise e

# メイン処理 (非同期)
async def main():
    """
    非同期的に価格取得処理を実行する
    """
    results = await get_price()
    print(f"結果:{results}")
    print("---------")



# if __name__ == '__main__':
#     send_notify('暗号資産情報')

if __name__ == "__main__":
    
    # 毎日午前9時にジョブを実行
    # schedule.every().day.at("09:00").do(job)
    # 1分お気に実行
    schedule.every(1).minutes.do(job)

    while True:
        # スケジュールされたジョブを実行
        schedule.run_pending()
        time.sleep(10)
