import yfinance as yf
from datetime import datetime, timedelta

def get_usdjpy_data():
    # USDJPY=X のTickerオブジェクトを作成
    usdjpy = yf.Ticker("USDJPY=X")

    # 現在の日時を取得
    end_date = datetime.now()
    # 7日前の日付を取得
    start_date = end_date - timedelta(days=7)

    # 過去7日間のデータを取得
    hist = usdjpy.history(start=start_date, end=end_date)

    # 最新の情報を取得
    latest_data = usdjpy.info

    return hist, latest_data

def display_usdjpy_info(hist, latest_data):
    print("USDJPY（米ドル/日本円）の情報：")
    print(f"現在のレート: {latest_data.get('regularMarketPrice', 'N/A'):.2f}")
    print(f"前日比: {latest_data.get('regularMarketChange', 'N/A'):.2f} ({latest_data.get('regularMarketChangePercent', 'N/A'):.2f}%)")
    print(f"本日の高値: {latest_data.get('dayHigh', 'N/A'):.2f}")
    print(f"本日の安値: {latest_data.get('dayLow', 'N/A'):.2f}")
    
    print("\n過去7日間の終値：")
    for date, row in hist.iterrows():
        print(f"{date.date()}: {row['Close']:.2f}")

def main():
    hist, latest_data = get_usdjpy_data()
    display_usdjpy_info(hist, latest_data)

if __name__ == "__main__":
    main()
