import asyncio
from playwright.async_api import async_playwright
from typing import List, Dict, Any

class AuctionCrawler:
    def __init__(self, keyword: str):
        self.keyword = keyword
        self.results: List[Dict[str, Any]] = []

    async def yahoo_auction_route(self, page):
        await page.goto(f"https://auctions.yahoo.co.jp/search/search?p={self.keyword}")
        items = await page.query_selector_all('.Product')
        for item in items[:5]:
            title = await item.query_selector('.Product__title')
            price = await item.query_selector('.Product__priceValue')
            link = await item.query_selector('.Product__titleLink')
            if title and price and link:
                self.results.append({
                    "title": await title.inner_text(),
                    "price": await price.inner_text(),
                    "link": await link.get_attribute('href'),
                    "source": "Yahoo!オークション"
                })

    async def mercari_route(self, page):
        await page.goto(f"https://jp.mercari.com/search?keyword={self.keyword}")
        # ページの読み込みを待つ
        await page.wait_for_load_state('networkidle')
        
        # デバッグ: ページのHTMLを出力
        print("Mercari page HTML:")
        print(await page.content())
        
        items = await page.query_selector_all('li[data-testid="item-cell"]')
        print(f"Found {len(items)} items on Mercari")
        
        for item in items[:5]:
            title_element = await item.query_selector('mer-item-thumbnail a')
            price_element = await item.query_selector('mer-item-thumbnail span[data-testid="price"]')
            
            if title_element and price_element:
                title = await title_element.get_attribute('aria-label')
                price = await price_element.inner_text()
                link = await title_element.get_attribute('href')
                
                self.results.append({
                    "title": title,
                    "price": price,
                    "link": f"https://jp.mercari.com{link}",
                    "source": "メルカリ"
                })
            else:
                print(f"Failed to extract data from item: {await item.inner_html()}")

    async def run(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)  # ヘッドレスモードをオフに
            page = await browser.new_page()

            await self.yahoo_auction_route(page)
            # await self.mercari_route(page)

            await browser.close()

        return sorted(self.results, key=lambda x: x['price'])

async def main():
    keyword = input("検索キーワードを入力してください: ")
    crawler = AuctionCrawler(keyword)
    results = await crawler.run()

    print(f"\n{keyword}の検索結果:")
    for result in results:
        print(f"\n商品名: {result['title']}")
        print(f"価格: {result['price']}")
        print(f"リンク: {result['link']}")
        print(f"出典: {result['source']}")

if __name__ == "__main__":
    asyncio.run(main())







# import asyncio
# from playwright.async_api import async_playwright
# from typing import List, Dict, Any

# class AuctionCrawler:
#     def __init__(self, keyword: str):
#         self.keyword = keyword
#         self.results: List[Dict[str, Any]] = []

#     async def yahoo_auction_route(self, page):
#         await page.goto(f"https://auctions.yahoo.co.jp/search/search?p={self.keyword}")
#         items = await page.query_selector_all('.Product')
#         for item in items[:5]:
#             title = await item.query_selector('.Product__title')
#             price = await item.query_selector('.Product__priceValue')
#             link = await item.query_selector('.Product__titleLink')
#             if title and price and link:
#                 self.results.append({
#                     "title": await title.inner_text(),
#                     "price": await price.inner_text(),
#                     "link": await link.get_attribute('href'),
#                     "source": "Yahoo!オークション"
#                 })

#     async def mercari_route(self, page):
#         await page.goto(f"https://www.mercari.com/jp/search/?keyword={self.keyword}")
#         items = await page.query_selector_all('.items-box')
#         for item in items[:5]:
#             title = await item.query_selector('.items-box-name')
#             price = await item.query_selector('.items-box-price')
#             link = await item.query_selector('a')
#             if title and price and link:
#                 self.results.append({
#                     "title": await title.inner_text(),
#                     "price": await price.inner_text(),
#                     "link": f"https://www.mercari.com{await link.get_attribute('href')}",
#                     "source": "メルカリ"
#                 })

#     async def run(self):
#         async with async_playwright() as p:
#             browser = await p.chromium.launch()
#             page = await browser.new_page()

#             await self.yahoo_auction_route(page)
#             await self.mercari_route(page)

#             await browser.close()

#         return sorted(self.results, key=lambda x: x['price'])

# async def main():
#     keyword = input("検索キーワードを入力してください: ")
#     crawler = AuctionCrawler(keyword)
#     results = await crawler.run()

#     print(f"\n{keyword}の検索結果:")
#     for result in results:
#         print(f"\n商品名: {result['title']}")
#         print(f"価格: {result['price']}")
#         print(f"リンク: {result['link']}")
#         print(f"出典: {result['source']}")

# if __name__ == "__main__":
#     asyncio.run(main())





# from crawlee.playwright import PlaywrightCrawler
# from playwright.async_api import Page
# from typing import List, Dict, Any

# class AuctionCrawler(PlaywrightCrawler):
#     def __init__(self, keyword: str):
#         super().__init__(
#             max_concurrency=2,
#             request_handler_timeout_secs=60
#         )
#         self.keyword = keyword
#         self.results: List[Dict[str, Any]] = []

#     async def yahoo_auction_route(self, page: Page):
#         await page.goto(f"https://auctions.yahoo.co.jp/search/search?p={self.keyword}")
#         items = await page.query_selector_all('.Product')
#         for item in items[:5]:
#             title = await item.query_selector('.Product__title')
#             price = await item.query_selector('.Product__priceValue')
#             link = await item.query_selector('.Product__titleLink')
#             if title and price and link:
#                 self.results.append({
#                     "title": await title.inner_text(),
#                     "price": await price.inner_text(),
#                     "link": await link.get_attribute('href'),
#                     "source": "Yahoo!オークション"
#                 })

#     async def mercari_route(self, page: Page):
#         await page.goto(f"https://www.mercari.com/jp/search/?keyword={self.keyword}")
#         items = await page.query_selector_all('.items-box')
#         for item in items[:5]:
#             title = await item.query_selector('.items-box-name')
#             price = await item.query_selector('.items-box-price')
#             link = await item.query_selector('a')
#             if title and price and link:
#                 self.results.append({
#                     "title": await title.inner_text(),
#                     "price": await price.inner_text(),
#                     "link": f"https://www.mercari.com{await link.get_attribute('href')}",
#                     "source": "メルカリ"
#                 })

#     async def router(self, request):
#         page = await request.loadPage()
#         if 'yahoo' in request.url:
#             await self.yahoo_auction_route(page)
#         elif 'mercari' in request.url:
#             await self.mercari_route(page)

#     async def run(self):
#         await self.addRequests([
#             "https://auctions.yahoo.co.jp",
#             "https://www.mercari.com"
#         ])
#         await super().run()
#         return sorted(self.results, key=lambda x: x['price'])

# async def main():
#     keyword = input("検索キーワードを入力してください: ")
#     crawler = AuctionCrawler(keyword)
#     crawler.router = crawler.router  # ルーターメソッドを設定
#     results = await crawler.run()

#     print(f"\n{keyword}の検索結果:")
#     for result in results:
#         print(f"\n商品名: {result['title']}")
#         print(f"価格: {result['price']}")
#         print(f"リンク: {result['link']}")
#         print(f"出典: {result['source']}")

# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())


