import asyncio
import json
import os
from langchain_openai import ChatOpenAI

os.chdir(os.path.dirname(os.path.abspath(__file__)))

async def a_invoke_model(gpt, msgs):
        return await gpt.ainvoke(msgs)


async def a_gen_instruction_from_url( ):
    """Generate instructional text from a single test case."""
    
    with open("output_ui.json", "r") as f:
        ui = json.load(f)

    with open("system_prompt_intent.txt", "r") as f:
        system_prompt = f.read()

    with open("user_prompt_intent.txt", "r") as f:
        user_prompt = f.read()

    with open("schema_intent.json", "r") as f:
        schema = json.load(f)

    
    gpt = ChatOpenAI(model="gpt-4.1", temperature=0.1).with_structured_output(schema=schema, strict=True)
    messages = [{"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt.replace("{json}", json.dumps(ui))}]
    
    response = await a_invoke_model(gpt, messages)
    return response.get("tests", [])


async def main():
     tests= await a_gen_instruction_from_url()
     with open("output_intent.json", "w") as f:
            json.dump(tests, f, indent= 2)

if __name__ == "__main__":
    asyncio.run(main())