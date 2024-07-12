import requests
from bs4 import BeautifulSoup

def search_yahoo_auction(keyword):
  """
  Yahoo!オークションで検索を行う関数

  Args:
    keyword: 検索キーワード

  Returns:
    検索結果のリスト
  """
  url = f"https://auctions.yahoo.co.jp/search/search?p={keyword}"
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'lxml')

  items = []
  for item in soup.find_all('li', class_='auc-item'):
    title = item.find('h2', class_='auc-item__title').text
    price = item.find('span', class_='price-label').text
    url = item.find('a', class_='auc-item__link')['href']

    items.append({
      'title': title,
      'price': price,
      'url': url,
      'source': 'Yahoo!オークション'
    })

  return items

def search_mercari(keyword):
  """
  メルカリで検索を行う関数

  Args:
    keyword: 検索キーワード

  Returns:
    検索結果のリスト
  """
  url = f"https://www.mercari.com/search/?keyword={keyword}"
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'lxml')

  items = []
  for item in soup.find_all('section', class_='item-info'):
    title = item.find('h3', class_='item-name').text
    price = item.find('span', class_='price__num').text
    url = item.find('a')['href']

    items.append({
      'title': title,
      'price': price,
      'url': url,
      'source': 'メルカリ'
    })

  return items

def search_all(keyword):
  """
  Yahoo!オークションとメルカリを横断検索する

  Args:
    keyword: 検索キーワード

  Returns:
    検索結果のリスト
  """
  results = []
  results.extend(search_yahoo_auction(keyword))
  results.extend(search_mercari(keyword))

  return results

if __name__ == '__main__':
  keyword = "ガンダム"  # 検索キーワード
  results = search_all(keyword)

  for item in results:
    print(f"【{item['source']}】 {item['title']}: {item['price']} {item['url']}")

