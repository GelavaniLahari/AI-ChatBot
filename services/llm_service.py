import os
from openai import OpenAI
from dotenv import load_dotenv


from utils.helpers import manage_history
from utils.logger import logger

from prompts.system_prompt import SYSTEM_PROMPT
from prompts.chat_prompt import build_prompt


load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


async def get_llm_response(question: str):

    try:
        user_prompt = build_prompt(question)
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        history = manage_history("user", user_prompt)
        messages.extend(history)

        response = client.chat.completions.create(
            model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
            messages=messages,
            max_tokens=500,
            temperature=0.3)

        reply = response.choices[0].message.content
        manage_history("assistant", reply)

        logger.info("Response generated successfully")

        return reply

    except Exception as e:
        logger.error(f"llm error {str(e)}")
        return f"error:{str(e)}"

async def stream_response(question:str):
    stream=client.chat.completions.create(
            model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
            messages=[{
                "role":"user",
                "content":question
            }],
            stream=True
    )
    for chunk in stream:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content    