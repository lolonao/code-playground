import asyncio
from crawlee import Crawler, PlaywrightCrawler

async def search_yahoo_auction(keyword):
  """
  Yahoo!オークションで検索を行う関数

  Args:
    keyword: 検索キーワード

  Returns:
    検索結果のリスト
  """
  crawler = PlaywrightCrawler({
    'headless': False,  # ブラウザウィンドウを表示
  })

  await crawler.start()
  page = await crawler.new_page()
  await page.goto(f"https://auctions.yahoo.co.jp/search/search?p={keyword}")

  items = []
  while True:
    # 検索結果ページをスクレイピング
    for item in await page.querySelectorAll('.auc-item'):
      title = await item.querySelector('h2.auc-item__title').text_content()
      price = await item.querySelector('span.price-label').text_content()
      url = await item.querySelector('a.auc-item__link')['href']

      items.append({
        'title': title,
        'price': price,
        'url': url,
        'source': 'Yahoo!オークション'
      })

    # 次のページに進む
    next_page_button = await page.querySelector('.aucpaging__navi__next')
    if next_page_button is None:
      break

    await next_page_button.click()
    await page.wait_for_navigation()

  await crawler.stop()
  return items

async def search_mercari(keyword):
  """
  メルカリで検索を行う関数

  Args:
    keyword: 検索キーワード

  Returns:
    検索結果のリスト
  """
  crawler = PlaywrightCrawler({
    'headless': False,  # ブラウザウィンドウを表示
  })

  await crawler.start()
  page = await crawler.new_page()
  await page.goto(f"https://www.mercari.com/search/?keyword={keyword}")

  items = []
  while True:
    # 検索結果ページをスクレイピング
    for item in await page.querySelectorAll('.item-info'):
      title = await item.querySelector('h3.item-name').text_content()
      price = await item.querySelector('span.price__num').text_content()
      url = await item.querySelector('a')['href']

      items.append({
        'title': title,
        'price': price,
        'url': url,
        'source': 'メルカリ'
      })

    # 次のページに進む
    next_page_button = await page.querySelector('.item-list__paging--next')
    if next_page_button is None:
      break

    await next_page_button.click()
    await page.wait_for_navigation()

  await crawler.stop()
  return items

async def search_all(keyword):
  """
  Yahoo!オークションとメルカリを横断検索する

  Args:
    keyword: 検索キーワード

  Returns:
    検索結果のリスト
  """
  results = []
  results.extend(await search_yahoo_auction(keyword))
  results.extend(await search_mercari(keyword))

  return results

if __name__ == '__main__':
  keyword = "iPhone 13"  # 検索キーワード
  results = asyncio.run(search_all(keyword))

  for item in results:
    print(f"【{item['source']}】 {item['title']}: {item['price']} {item['url']}")

