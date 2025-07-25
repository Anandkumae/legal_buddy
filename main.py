from fastapi import FastAPI, Request
from app.openrouter_client import query_llm
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "✅ Legal Buddy backend is live!"}

@app.post("/generate-judgment")
async def generate_judgment(request: Request):
    data = await request.json()
    prompt = data.get("prompt")
    if not prompt:
        return {"error": "Prompt is required"}
    judgment = query_llm(prompt)
    return {"judgment": judgment}


