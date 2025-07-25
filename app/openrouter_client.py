import os
from dotenv import load_dotenv

# Load .env from root even when running from nested modules
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
env_path = os.path.join(root_dir, ".env")
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise ValueError("❌ OPENROUTER_API_KEY is missing from .env")

import requests

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "HTTP-Referer": "https://yourproject.com",
    "X-Title": "Legal Buddy"
}

def query_llm(prompt, model="mistralai/mistral-7b-instruct"):
    url = "https://openrouter.ai/api/v1/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a legal assistant. Generate detailed and structured judgments."},
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"❌ API call failed: {response.status_code} - {response.text}")



