import requests
from bs4 import BeautifulSoup

def search_ec_sites(query, num_pages=1):
  """
  ECサイトで商品を検索するサンプルコード。

  Args:
    query: 検索する商品名
    num_pages: 検索結果のページ数

  Returns:
    検索結果のリスト
  """

  results = []
  for page in range(1, num_pages + 1):
    # 各ECサイトの検索URLを定義
    search_urls = {
      "楽天市場": f"https://search.rakuten.co.jp/search/mall/{query}?p={page}",
      "Yahoo!ショッピング": f"https://shopping.yahoo.co.jp/search?p={page}&tab_ex=commerce&oq={query}&ei=UTF-8",
      "Amazon": f"https://www.amazon.co.jp/s?k={query}&page={page}",
    }

    for site_name, url in search_urls.items():
      response = requests.get(url)
      response.raise_for_status()  # ステータスコードが200以外の場合、例外を発生させる

      soup = BeautifulSoup(response.content, 'html.parser')

      # 各ECサイトの検索結果の要素を特定する
      if site_name == "楽天市場":
        items = soup.find_all('div', class_='search-result-item')
      elif site_name == "Yahoo!ショッピング":
        items = soup.find_all('li', class_='sc-item')
      elif site_name == "Amazon":
        items = soup.find_all('div', class_='s-result-item')

      for item in items:
        # 商品名、価格、URLなどを取得
        title = item.find('a', class_='product-name')
        title = title.text.strip() if title else "N/A"  # Handle None case
        price = item.find('span', class_='product-price__price')
        price = price.text.strip() if price else "N/A"  # Handle None case
        # url = item.find('a', class_='product-name')['href'] if site_name == "楽天市場" else item.find('a', class_='sc-item__link')['href'] if site_name == "Yahoo!ショッピング" else item.find('a', class_='a-link-normal s-no-outline')['href']

        if site_name == "楽天市場":
            url = item.find('a', class_='product-name')['href']
        elif site_name == "Yahoo!ショッピング":
            url = item.find('a', class_='sc-item__link')['href']
        else:
            url = item.find('a', class_='a-link-normal s-no-outline')['href']


        results.append({
          "site": site_name,
          "title": title,
          "price": price,
          "url": url,
        })

  return results

# 検索する商品名
query = "iPhone 14"

# 検索結果を取得
results = search_ec_sites(query, num_pages=2)

# 結果を表示
for result in results:
  print(f"サイト: {result['site']}")
  print(f"商品名: {result['title']}")
  print(f"価格: {result['price']}")
  print(f"URL: {result['url']}")
  print("-" * 20)


# import requests
# from bs4 import BeautifulSoup

# def search_ec_sites(query, num_pages=1):
#   """
#   ECサイトで商品を検索するサンプルコード。

#   Args:
#     query: 検索する商品名
#     num_pages: 検索結果のページ数

#   Returns:
#     検索結果のリスト
#   """

#   results = []
#   for page in range(1, num_pages + 1):
#     # 各ECサイトの検索URLを定義
#     search_urls = {
#       "楽天市場": f"https://search.rakuten.co.jp/search/mall/{query}?p={page}",
#       "Yahoo!ショッピング": f"https://shopping.yahoo.co.jp/search?p={page}&tab_ex=commerce&oq={query}&ei=UTF-8",
#       "Amazon": f"https://www.amazon.co.jp/s?k={query}&page={page}",
#     }

#     for site_name, url in search_urls.items():
#       response = requests.get(url)
#       response.raise_for_status()  # ステータスコードが200以外の場合、例外を発生させる

#       soup = BeautifulSoup(response.content, 'html.parser')

#       # 各ECサイトの検索結果の要素を特定する
#       if site_name == "楽天市場":
#         items = soup.find_all('div', class_='search-result-item')
#       elif site_name == "Yahoo!ショッピング":
#         items = soup.find_all('li', class_='sc-item')
#       elif site_name == "Amazon":
#         items = soup.find_all('div', class_='s-result-item')

#       for item in items:
#         # 商品名、価格、URLなどを取得
#         title = item.find('a', class_='product-name').text.strip() if site_name == "楽天市場" else item.find('h2', class_='sc-item__title').text.strip() if site_name == "Yahoo!ショッピング" else item.find('h2', class_='a-size-medium a-color-base a-text-normal').text.strip()
#         price = item.find('span', class_='product-price__price').text.strip() if site_name == "楽天市場" else item.find('span', class_='sc-item__price').text.strip() if site_name == "Yahoo!ショッピング" else item.find('span', class_='a-price-whole').text.strip()
#         url = item.find('a', class_='product-name')['href'] if site_name == "楽天市場" else item.find('a', class_='sc-item__link')['href'] if site_name == "Yahoo!ショッピング" else item.find('a', class_='a-link-normal s-no-outline')['href']

#         results.append({
#           "site": site_name,
#           "title": title,
#           "price": price,
#           "url": url,
#         })

#   return results

# # 検索する商品名
# query = "iPhone 14"

# # 検索結果を取得
# results = search_ec_sites(query, num_pages=2)

# # 結果を表示
# for result in results:
#   print(f"サイト: {result['site']}")
#   print(f"商品名: {result['title']}")
#   print(f"価格: {result['price']}")
#   print(f"URL: {result['url']}")
#   print("-" * 20)
