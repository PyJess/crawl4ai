from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, BrowserConfig
import asyncio
import json
import os
from langchain_openai import ChatOpenAI


os.chdir(os.path.dirname(os.path.abspath(__file__)))

async def main():

    
    async def a_invoke_model(gpt, msgs):
        return await gpt.ainvoke(msgs)


    async with AsyncWebCrawler(config=BrowserConfig()) as crawler:
        run_config = CrawlerRunConfig(
            excluded_tags=["script", "style"],     # Rimuove solo script e style
            remove_forms=False,                    # Non rimuove i form
            keep_data_attributes=True,             # Preserva data-* attributes
            # Evita di escludere header/footer/nav
            # excluded_selector=None,
            # only_text=False,
        )

        result = await crawler.arun(url="https://www.ryanair.com/en/en", config=run_config)

        if result.success:
            url= result.url
            print(f"Successfully crawled {url}")
            html = result.html
            html= "The html of this url:"+ url + "is this:" + html
            #print(cleaned)  # Contiene il DOM completo utile per estrazione UI

        with open("system_prompt.txt", "r") as f:
            system_prompt = f.read()

        with open("user_prompt_ui.txt", "r") as f:
            user_prompt = f.read()

        with open("schema_ui.json", "r") as f:
            schema = json.load(f)


        gpt = ChatOpenAI(model="gpt-4.1", temperature=0.1).with_structured_output(schema, strict=True)

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt.replace("{html}", html)}]
        
        response = await a_invoke_model(gpt, messages)
        print(response)

        with open("output_ui.json", "w") as f:
            json.dump(response, f, indent=2)

asyncio.run(main())


