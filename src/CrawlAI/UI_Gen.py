import asyncio
import json
import os
import re
import shutil
import stat
from collections import defaultdict
import traceback

from langchain_openai import ChatOpenAI
from crawl4ai import (
    AsyncWebCrawler,
    CrawlerRunConfig,
    BFSDeepCrawlStrategy,
    LXMLWebScrapingStrategy,
    BrowserConfig,
)
from crawl4ai.deep_crawling.filters import FilterChain, URLPatternFilter 

# Imposta la directory corrente allo script
os.chdir(os.path.dirname(os.path.abspath(__file__)))
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__) ,".."))
print(f"src path {src_dir} ")


def clear_folder(folder_path):
    """Delete all files in the specified folder."""
    if not os.path.exists(folder_path):
        return
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.chmod(file_path, stat.S_IWRITE)  
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path, onerror=lambda func, path, excinfo: os.chmod(path, stat.S_IWRITE) or func(path))
        except Exception as e:
            print(f"Warning: impossible to delete {file_path}. Reason: {e}")
            traceback.print_exc()

async def deep_crawl(url: list[str], mode: str):
#async def deep_crawl(url: list[str]):
    if len(url) != 1 and mode== "pair":

        depth= 2
        parent_url = url[0]
        print(f"Parent URL: {parent_url}")
        selected_child_urls = url[1:]
        print(f"Selected Child URLs: {selected_child_urls}")
        # filtro URL: solo questi due verranno accettati dal crawler
        url_filter = URLPatternFilter(patterns=[parent_url] + selected_child_urls)
        filter_chain = FilterChain([url_filter])

        # Configurazione crawl
        run_config = CrawlerRunConfig(
            deep_crawl_strategy=BFSDeepCrawlStrategy(
                max_depth=depth,
                include_external=False,
                filter_chain=filter_chain  # filtro URL
            ),
            scraping_strategy=LXMLWebScrapingStrategy(),
            excluded_tags=["script", "style"],
            remove_forms=True,
            keep_data_attributes=False,
            verbose=True
        )
    elif len(url) !=1 and mode== "single":
        print("ciao")
        # ....
    elif len(url) == 1 and mode== "single":
        parent_url = url[0]
        depth= 0
        run_config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(
            max_depth=depth, 
            include_external=False
        ),
        scraping_strategy=LXMLWebScrapingStrategy(),
        excluded_tags=["script", "style"],
        remove_forms=True,
        keep_data_attributes=False,
        verbose=True
    )
    else:
        raise ValueError("Per la modalità 'pair' fornire almeno due URL (uno parent e almeno uno child). Per la modalità 'single' fornire un solo URL.")

    # Funzione helper per chiamare GPT
    async def a_invoke_model(gpt, msgs):
        return await gpt.ainvoke(msgs)

    # Carica prompt e schema
    with open(os.path.join("prompts", "system_prompt.txt"), "r", encoding="utf-8") as f:
        system_prompt = f.read()
    with open(os.path.join("prompts","user_prompt_ui.txt"), "r", encoding="utf-8") as f:
        user_prompt = f.read()
    with open(os.path.join("prompts","schema_ui.json"), "r", encoding="utf-8") as f:
        schema = json.load(f)

    gpt = ChatOpenAI(model="gpt-4.1", temperature=0.1).with_structured_output(schema, strict=True)

    # Crawl asincrono
    async with AsyncWebCrawler(config=BrowserConfig()) as crawler:
        results = await crawler.arun(parent_url, config=run_config)  # punto di partenza = parent_url
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
        output_dir = os.path.join(src_dir,"outputs", "UI_gen")
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
    asyncio.run(deep_crawl(["https://www.ryanair.com/ie/en/cookie-policy"]))
