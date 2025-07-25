# main.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests, os, time
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

# Allow CORS for Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("❌ Missing OPENROUTER_API_KEY in .env")


def query_llm(prompt, model="mistralai/mistral-7b-instruct"):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "LegalBuddy AI"
    }

    system_prompt = "You are a legal assistant. Generate structured and formal legal judgments based on crime details."

    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        time.sleep(2)
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error: {str(e)}"


@app.post("/generate-judgment")
async def generate_judgment(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    if not prompt.strip():
        return {"judgment": "❌ No case description provided."}
    return {"judgment": query_llm(prompt)}

