import asyncio
import json
from langchain_openai import ChatOpenAI


async def a_invoke_model(gpt, msgs):
        return await gpt.ainvoke(msgs)


async def a_gen_instruction_from_url( ):
    """Generate instructional text from a single test case."""
    
    with open("output.json", "r") as f:
        ui = json.load(f)

    with open("system_prompt_intent.txt", "r") as f:
        system_prompt = f.read()

    with open("schema_intent.json", "r") as f:
        schema = json.load(f)
    system_prompt = system_prompt.replace("{json}", json.dumps(ui))
    
    gpt = ChatOpenAI(model="gpt-4.1", temperature=0.1).with_structured_output(schema=schema, strict=True)
    messages = [{"role": "system", "content": system_prompt}]
    
    response = await a_invoke_model(gpt, messages)
    return response.get("tests", [])


async def main():
     tests= await a_gen_instruction_from_url()
     with open("outout_intent.json", "w") as f:
            json.dump(tests, f, indent= 2)

if __name__ == "__main__":
    asyncio.run(main())