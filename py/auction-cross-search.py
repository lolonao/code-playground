from crawlee import PlaywrightCrawler, Configuration
from crawlee.playwright import PlaywrightCrawlerContext
from typing import List, Dict, Any

class AuctionCrawler(PlaywrightCrawler):
    def __init__(self, keyword: str):
        super().__init__(
            Configuration(
                max_concurrent_requests=2,
                max_requests_per_minute=20
            )
        )
        self.keyword = keyword
        self.results: List[Dict[str, Any]] = []

    async def yahoo_auction_route(self, context: PlaywrightCrawlerContext):
        page = context.page
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

    async def mercari_route(self, context: PlaywrightCrawlerContext):
        page = context.page
        await page.goto(f"https://www.mercari.com/jp/search/?keyword={self.keyword}")
        items = await page.query_selector_all('.items-box')
        for item in items[:5]:
            title = await item.query_selector('.items-box-name')
            price = await item.query_selector('.items-box-price')
            link = await item.query_selector('a')
            if title and price and link:
                self.results.append({
                    "title": await title.inner_text(),
                    "price": await price.inner_text(),
                    "link": f"https://www.mercari.com{await link.get_attribute('href')}",
                    "source": "メルカリ"
                })

    async def run(self):
        await self.run_multiple([
            lambda ctx: self.yahoo_auction_route(ctx),
            lambda ctx: self.mercari_route(ctx)
        ])
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
    import asyncio
    asyncio.run(main())
