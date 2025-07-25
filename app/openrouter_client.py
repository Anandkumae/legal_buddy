import os
import time
from openrouter import OpenRouter
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("❌ OPENROUTER_API_KEY is missing from .env")

client = OpenRouter(api_key=api_key)

def query_llm(prompt, model="mistralai/mistral-7b-instruct", role="legal_assistant"):
    system_prompt = "You are a legal assistant. Generate structured and formal legal judgments based on crime details."
    try:
        time.sleep(1)  # Avoid rate limit
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"❌ LLM query failed: {e}")
        return "Judgment generation failed. Please try again later."




