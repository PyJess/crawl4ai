
import asyncio
import json
from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

def element_to_dict(element):
    if element.name is None:
        text = element.strip()
        return text if text else None
    return {
        "tag": element.name,
        "attributes": dict(element.attrs),
        "children": list(filter(None, (element_to_dict(child) for child in element.children)))
    }

async def main():
    browser_config = BrowserConfig(headless=True, verbose=False)
    run_config = CrawlerRunConfig(remove_overlay_elements=True)

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://www.ryanair.com/en/en",
            config=run_config
        )
        html = result.html  # Intero DOM in HTML
    soup = BeautifulSoup(html, "html.parser")
    dom_json = element_to_dict(soup)
    with open("pagina.json", "w", encoding="utf-8") as f:
        json.dump(dom_json, f, ensure_ascii=False, indent=2)
    print("Salvato DOM completo in JSON: pagina.json")

if __name__ == "__main__":
    asyncio.run(main())

 