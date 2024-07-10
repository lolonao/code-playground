import requests
from bs4 import BeautifulSoup

# 検索対象サイト
sites = [
    "https://auctions.yahoo.co.jp/",
    "https://fril.jp/",
    "https://jp.mercari.com/",
]

# 検索ワード
keyword = "煙管"

# 各サイトの検索結果を格納するリスト
results = []

for site in sites:
    # 検索ページURLを生成
    url = site + "search?q=" + keyword

    # リクエスト送信
    response = requests.get(url)

    # レスポンスを確認
    if response.status_code == 200:
        # BeautifulSoupでパース
        soup = BeautifulSoup(response.content, "lxml")

        # 検索結果の要素を取得
        items = soup.find_all("item")  # ここは各サイトによって調整が必要

        # 各商品情報をリストに追加
        for item in items:
            # 商品名、価格、URLなどを取得
            title = item.find("title").text
            price = item.find("price").text
            link = item.find("link").text

            # 結果をリストに格納
            results.append({
                "site": site,
                "title": title,
                "price": price,
                "link": link,
            })

# 検索結果を表示
for result in results:
    print(f"[**{result['site']}**]({result['link']})")
    print(f"{result['title']}")
    print(f"{result['price']}")
    print("-" * 30)


