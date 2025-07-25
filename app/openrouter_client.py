import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("❌ OPENROUTER_API_KEY is missing from .env")

# Function to query the OpenRouter API
def query_llm(prompt, model="mistralai/mistral-7b-instruct"):
    import json
    url = "https://openrouter.ai/api/v1/chat/completions"
    api_key = os.getenv("OPENROUTER_API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",  # Add your domain here if deployed
        "X-Title": "Legal Buddy"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a legal assistant. Generate structured and formal legal judgments based on crime details."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        print("✅ Response:", json.dumps(result, indent=2))  # Debug line
        return result['choices'][0]['message']['content']
    except Exception as e:
        print(f"❌ Exception: {e}")
        if 'response' in locals():
            print(f"❌ Response Text: {response.text}")
        return "Judgment generation failed. Please try again later."
