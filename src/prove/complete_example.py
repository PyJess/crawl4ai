from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonXPathExtractionStrategy

async def main():
    schema = {
        "name": "Flight Details",
        "baseSelector": "//div[contains(@class, 'flight-item')]",
        "fields": [
            {"name": "Flight Title", "selector": ".//h2[contains(@class, 'flight-title')]/text()", "type": "text"},
            {"name": "Flight Price", "selector": ".//span[contains(@class, 'flight-price')]/text()", "type": "text"}
        ]
    }
    url = "https://www.ryanair.com/en/en"

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=url,
            config=CrawlerRunConfig(
                cache_mode=CacheMode.BYPASS,
                extraction_strategy=JsonXPathExtractionStrategy(schema)
            )
        )
        data = result.extracted_content
        print(data)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
