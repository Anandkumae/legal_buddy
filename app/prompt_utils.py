# app/prompt_utils.py

import requests

API_KEY = "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"  # 🔁 Replace this with your real key from openrouter.ai

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "HTTP-Referer": "https://yourproject.com",  # 🔁 Optional: Replace with your site URL
    "X-Title": "Legal Buddy"
}

def generate_judgment(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    payload = {
        "model": "mistralai/mixtral-8x7b",  # 🔁 You can change the model as needed
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



