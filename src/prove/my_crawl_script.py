import asyncio
from crawl4ai import AsyncWebCrawler
import json
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig

async def main():
    browser_config = BrowserConfig()  # Default browser configuration
    run_config = CrawlerRunConfig()   # Default crawl run configuration

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://www.ryanair.com/en/en",
            #url= "https://docs.ragas.io/en/latest/getstarted/evals/",
            config=run_config
        )
        #print(result.markdown)  # Print clean markdown content
        with open("basic_output1.md", "w", encoding="utf-8") as f:
            f.write(result.markdown)
        if result.extracted_content:
            print("Extracted Structured Content:")
            data = json.loads(result.extracted_content)
            print(data)

        print(result.cleaned_html)         # Raw HTML
        # print(result.cleaned_html) # Cleaned HTML
        #print(result.markdown.raw_markdown) # Raw markdown from cleaned html
        #print(result.markdown.fit_markdown) # Most relevant content in markdown

        # # Check success status
        # print(result.success)      # True if crawl succeeded
        # print(result.status_code)  # HTTP status code (e.g., 200, 404)

        # # Access extracted media and links
        # print(result.media)        # Dictionary of found media (images, videos, audio)
        #print(result.links) 

if __name__ == "__main__":
    asyncio.run(main())
