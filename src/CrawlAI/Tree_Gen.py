import asyncio
import os
import json
from collections import defaultdict
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
from crawl4ai.deep_crawling import BestFirstCrawlingStrategy
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from typing import Optional

os.chdir(os.path.dirname(os.path.abspath(__file__)))


async def run_advanced_crawler(start_url: str, max_depth: int):
    config = CrawlerRunConfig(
        deep_crawl_strategy=BestFirstCrawlingStrategy(
            max_depth=max_depth,
            include_external=False
        ),
        scraping_strategy=LXMLWebScrapingStrategy(),
        stream=True,
        verbose=True
    )

    results = []
    nodes_map = {}
    children_map = defaultdict(list)

    async def a_invoke_model(gpt, msgs):
        return await gpt.ainvoke(msgs)
    
    async with AsyncWebCrawler() as crawler:
        async for result in await crawler.arun(start_url, config=config):
            results.append(result)
            score = result.metadata.get("score", 0)
            depth = result.metadata.get("depth", 0)
            parent = result.metadata.get("parent_url")

            if result.success:
                nodes_map[result.url] = {"url": result.url, "depth": depth}
                if parent:
                    children_map[parent].append({"url": result.url, "depth": depth})
            else:
                print(f"❌ Failed to crawl {result.url}")

            print(f"Depth: {depth} | Score: {score:.2f} | {result.url}")

    depth_counts = {}
    for result in results:
        depth = result.metadata.get("depth", 0)
        depth_counts[depth] = depth_counts.get(depth, 0) + 1

    print("Pages crawled by depth:")
    for depth, count in sorted(depth_counts.items()):
        print(f"  Depth {depth}: {count} pages")

    if start_url not in nodes_map:
        nodes_map[start_url] = {"url": start_url, "depth": 0}

    def build_tree(parent_url, visited=set()):
        result = []
        for child_data in children_map.get(parent_url, []):
            child_url = child_data["url"]
            if child_url in visited:
                continue
            visited.add(child_url)
            node = nodes_map[child_url].copy()
            node["children"] = build_tree(child_url, visited)
            result.append(node)
        return result

    # Build the full tree starting from the root
    full_tree = [{"url": start_url, "depth": 0, "children": build_tree(start_url)}]

    gpt = ChatOpenAI(model="gpt-4.1", temperature=0.1)

    async def enrich_with_title(node, gpt):
        url = node["url"]
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Generate a concise, unique, and meaningful title for this URL: {url}. The title should be as specific as possible to the url and not generic. Only return the title, nothing else."}
        ]
        try:
            response = await a_invoke_model(gpt, messages)
            node["title"] = response.content.strip()
        except Exception as e:
            print(f"⚠️ Could not get title for {url}: {e}")
            node["title"] = None

        tasks=[enrich_with_title(child, gpt) for child in node.get("children", [])]
        if tasks:
            await asyncio.gather(*tasks)

    tasks=[enrich_with_title(node, gpt) for node in full_tree]
    await asyncio.gather(*tasks)

    messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"""
You are given this JSON tree: {json.dumps(full_tree, ensure_ascii=False)}.

Task:
- Ensure that every 'title' is unique for each 'url'.
- If duplicates exist, modify the titles to make them unique.
- Return ONLY the full corrected JSON. Do not include explanations, text, or formatting.
"""}
        ]
    response = await a_invoke_model(gpt, messages)
    response = json.loads(response.content)

    return response


if __name__ == "__main__":
    asyncio.run(run_advanced_crawler())