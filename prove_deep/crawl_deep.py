import asyncio
import json
import os
import re
import shutil
import stat
from collections import defaultdict

from langchain_openai import ChatOpenAI
from crawl4ai import (
    AsyncWebCrawler,
    CrawlerRunConfig,
    BFSDeepCrawlStrategy,
    LXMLWebScrapingStrategy,
    BrowserConfig,
)

# Imposta la directory corrente allo script
os.chdir(os.path.dirname(os.path.abspath(__file__)))


async def main():
    # Configurazione crawl
    run_config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(max_depth=2, include_external=False),
        scraping_strategy=LXMLWebScrapingStrategy(),
        excluded_tags=["script", "style"],
        remove_forms=True,
        keep_data_attributes=False,
        verbose=True
    )

    # Funzione helper per chiamare GPT
    async def a_invoke_model(gpt, msgs):
        return await gpt.ainvoke(msgs)

    # Carica prompt e schema
    with open("system_prompt.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()
    with open("user_prompt_ui.txt", "r", encoding="utf-8") as f:
        user_prompt = f.read()
    with open("schema_ui.json", "r", encoding="utf-8") as f:
        schema = json.load(f)

    gpt = ChatOpenAI(model="gpt-4.1", temperature=0.1).with_structured_output(schema, strict=True)

    # Crawl asincrono
    async with AsyncWebCrawler(config=BrowserConfig()) as crawler:
        results = await crawler.arun("https://www.ryanair.com/en/en", config=run_config)
        print(f"\nCrawled {len(results)} pages in total\n")

        nodes_map = {}
        children_map = defaultdict(list)
        tasks = []

        for result in results:
            url = result.url
            depth = result.metadata.get("depth")
            parent = result.metadata.get("parent_url")
            parent_str = parent if parent else "ROOT"

            if not result.success:
                print(f"❌ Failed to crawl {url}")
                continue

            print(f"The depth is: {depth}, and the parent url is: {parent}")
            html = f"The parent url is this: {parent_str} and the html of this url: {url} is this: {result.html}"

            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt.replace("{html}", html)}
            ]

            async def process_page(url, messages, depth, parent):
                try:
                    response = await a_invoke_model(gpt, messages)
                    print(f"✅ Done: {url}")
                    if response and "page" in response:
                        response["page"]["parent_url"] = parent
                        response["page"]["depth"] = depth
                    return {"url": url, "response": response, "parent_url": parent, "depth": depth}
                except Exception as e:
                    print(f"⚠️ Error processing {url}: {e}")
                    return {"url": url, "error": str(e)}

            tasks.append(process_page(url, messages, depth, parent))
            children_map[parent].append(url)

        all_results = await asyncio.gather(*tasks)

        # Pulizia cartella output
        output_dir = "outputs"
        if os.path.exists(output_dir):
            shutil.rmtree(
                output_dir,
                onerror=lambda func, path, excinfo: os.chmod(path, stat.S_IWRITE) or func(path)
            )
        os.makedirs(output_dir, exist_ok=True)

        # Salvataggio singole pagine
        for i, r in enumerate(all_results, start=1):
            url = r["url"]
            nodes_map[url] = r
            if "response" in r:
                safe_name = re.sub(r'[\\/*?:"<>|]', "_", url)
                filepath = os.path.join(output_dir, f"{safe_name}_{i}.json")
                with open(filepath, "w", encoding="utf-8") as f:
                    json.dump(r, f, indent=2)

        # Costruzione albero ricorsivo
        def build_tree(parent_url, visited=None):
            if visited is None:
                visited = set()
            result = []
            for child_url in children_map.get(parent_url, []):
                if child_url in visited:
                    result.append({"url": child_url, "note": "già visitato", "children": []})
                    continue
                visited.add(child_url)
                node = nodes_map[child_url].copy()
                node["children"] = build_tree(child_url, visited)
                result.append(node)
            return result

        full_tree = build_tree(None)
        tree_file = os.path.join(output_dir, "full_output_tree.json")
        with open(tree_file, "w", encoding="utf-8") as f:
            json.dump(full_tree, f, indent=2)

        # Creazione coppie parent-child
        with open(tree_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        counter = [1]

        def process_node(node, parent_depth=1, counter_ref=None):
            if counter_ref is None:
                counter_ref = [1]

            parent_info = {
                "url": node.get("url"),
                "title": node.get("response", {}).get("page", {}).get("title"),
                "components": node.get("response", {}).get("page", {}).get("components", []),
                "depth": parent_depth
            }

            for child in node.get("children", []):
                child_info = {
                    "url": child.get("url"),
                    "title": child.get("response", {}).get("page", {}).get("title"),
                    "components": child.get("response", {}).get("page", {}).get("components", []),
                    "depth": parent_depth + 1
                }
                pair = {"parent": parent_info, "child": child_info}
                filename = f"{output_dir}/pair_{counter_ref[0]}.json"
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(pair, f, indent=2, ensure_ascii=False)
                print(f"Saved {filename}")
                counter_ref[0] += 1
                if child.get("children"):
                    process_node(child, parent_depth + 1, counter_ref)

        for root in data:
            process_node(root, counter_ref=counter)

        print(f"✅ Done! Created {counter[0]-1} JSON files inside 'outputs/' directory.")


if __name__ == "__main__":
    asyncio.run(main())
