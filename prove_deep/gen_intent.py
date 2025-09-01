import asyncio
import json
import os
from langchain_openai import ChatOpenAI

os.chdir(os.path.dirname(os.path.abspath(__file__)))

async def a_invoke_model(gpt, msgs):
    return await gpt.ainvoke(msgs)

async def a_gen_instruction_from_url(ui):
    """Generate instructional text from a single test case."""
    with open("system_prompt_intent.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()
    with open("user_prompt_intent.txt", "r", encoding="utf-8") as f:
        user_prompt = f.read()
    with open("schema_intent.json", "r", encoding="utf-8") as f:
        schema = json.load(f)

    gpt = ChatOpenAI(model="gpt-4.1", temperature=0.1).with_structured_output(schema=schema, strict=True)
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt.replace("{json}", json.dumps(ui))}
    ]

    response = await a_invoke_model(gpt, messages)
    return response.get("tests", [])

async def process_file(ui_file):
    with open(os.path.join("outputs", ui_file), "r", encoding="utf-8") as f:
        ui = json.load(f)
    tests = await a_gen_instruction_from_url(ui)
    os.makedirs(os.path.join("outputs", "intents"), exist_ok=True)
    output_file = f"intent_{ui_file}"
    with open(os.path.join("outputs", "intents", output_file), "w", encoding="utf-8") as f:
        json.dump(tests, f, indent=2)
    print(f"Generated instructions saved to {output_file}")

async def main():
    tasks = [
        process_file(f)
        for f in os.listdir("outputs")
        if f.endswith(".json") and f != "full_output_tree.json"
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
