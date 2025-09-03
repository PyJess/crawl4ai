import asyncio
import os
import json
from collections import defaultdict
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
from crawl4ai.deep_crawling import BestFirstCrawlingStrategy

os.chdir(os.path.dirname(os.path.abspath(__file__)))

async def run_advanced_crawler():
    config = CrawlerRunConfig(
        deep_crawl_strategy=BestFirstCrawlingStrategy(
            max_depth=3,
            include_external=False
        ),
        scraping_strategy=LXMLWebScrapingStrategy(),
        stream=True,
        verbose=True
    )

    results = []
    nodes_map = {}
    children_map = defaultdict(list)

    async with AsyncWebCrawler() as crawler:
        async for result in await crawler.arun("https://www.ryanair.com/en/en", config=config):
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

    # Initialize root node
    root_url = "https://www.ryanair.com/en/en"
    if root_url not in nodes_map:
        nodes_map[root_url] = {"url": root_url, "depth": 0}

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
    full_tree = [{"url": root_url, "depth": 0, "children": build_tree(root_url)}]

    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    tree_file = os.path.join(output_dir, "full_output_tree.json")
    with open(tree_file, "w", encoding="utf-8") as f:
        json.dump(full_tree, f, indent=2)
    print(f"Tree with depth and relationships saved in {tree_file}")

if __name__ == "__main__":
    asyncio.run(run_advanced_crawler())