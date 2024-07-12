import requests
from bs4 import BeautifulSoup
import concurrent.futures

def search_yahoo_auction(keyword):
    url = f"https://auctions.yahoo.co.jp/search/search?p={keyword}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('li', class_='Product')
    
    results = []
    for item in items[:5]:  # 最初の5件のみ取得
        title = item.find('h3', class_='Product__title').text.strip()
        price = item.find('span', class_='Product__priceValue').text.strip()
        link = item.find('a', class_='Product__titleLink')['href']
        results.append({"title": title, "price": price, "link": link, "source": "Yahoo!オークション"})
    
    return results

def search_mercari(keyword):
    keyword = "%E3%82%AC%E3%83%B3%E3%83%80%E3%83%A0"
    url = f"https://jp.mercari.com/search?keyword={keyword}"
    # url = f"https://www.mercari.com/jp/search/?keyword={keyword}"
    # url = f"https://www.mercari.com/jp/search/?keyword={keyword}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('li', class_='items-box')
    
    results = []
    for item in items[:5]:  # 最初の5件のみ取得
        title = item.find('h3', class_='items-box-name').text.strip()
        price = item.find('div', class_='items-box-price').text.strip()
        link = "https://www.mercari.com" + item.find('a')['href']
        results.append({"title": title, "price": price, "link": link, "source": "メルカリ"})
    
    return results

def search_all(keyword):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        yahoo_future = executor.submit(search_yahoo_auction, keyword)
        mercari_future = executor.submit(search_mercari, keyword)
        
        yahoo_results = yahoo_future.result()
        mercari_results = mercari_future.result()
    
    all_results = yahoo_results + mercari_results
    return sorted(all_results, key=lambda x: x['price'])

if __name__ == "__main__":
    keyword = input("検索キーワードを入力してください: ")
    results = search_all(keyword)
    
    print(f"\n{keyword}の検索結果:")
    for result in results:
        print(f"\n商品名: {result['title']}")
        print(f"価格: {result['price']}")
        print(f"リンク: {result['link']}")
        print(f"出典: {result['source']}")
