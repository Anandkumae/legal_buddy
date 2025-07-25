
markdown
Copy
Edit
# ⚖️ LegalBuddy – AI-Powered Legal Judgment Assistant

LegalBuddy is an AI-powered legal assistant that helps lawyers, students, and researchers generate structured legal judgments from textual case descriptions using powerful open-source LLMs via OpenRouter.

## 🚀 Features

- 🧠 **LLM Integration** (via OpenRouter) for smart judgment generation
- 📄 **User Input via Streamlit** frontend
- 🔁 **FastAPI Backend** for processing
- 🔒 **Environment-variable-based API Key security**
- 🌐 **Deployed on Render (Free Tier)**

---

## 🖼️ UI Preview

![LegalBuddy Screenshot](https://your-screenshot-or-gif-url.com) <!-- Optional -->

---

## 🏗️ Tech Stack

| Frontend | Backend | Model API | Deployment |
|----------|---------|-----------|------------|
| Streamlit | FastAPI | OpenRouter (e.g., Mistral, GPT) | Render (Free Tier) |

---

## 🧪 How It Works

1. User submits a case description via Streamlit.
2. The frontend sends the prompt to the FastAPI backend.
3. Backend calls OpenRouter API to generate judgment.
4. Result is shown in a structured format.

---

## 📦 Folder Structure

legalbuddy/
│
├── app/
│ ├── openrouter_client.py # LLM API call logic
│ └── init.py
│
├── main.py # FastAPI backend
├── ui_app.py # Streamlit frontend
├── .env # (ignored) API key
├── requirements.txt
├── render.yaml # Render deployment config
└── README.md

yaml
Copy
Edit

---

## 🛠️ Setup Instructions (Local)

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/legalbuddy.git
cd legalbuddy
2. Create a .env file
env
Copy
Edit
OPENROUTER_API_KEY=sk-or-your-api-key-here
⚠️ Never commit .env or expose your API key.

3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run Backend
bash
Copy
Edit
uvicorn main:app --reload
5. Run Frontend
bash
Copy
Edit
streamlit run ui_app.py
Now go to http://localhost:8501 to use LegalBuddy!

🚀 Deployment on Render
This project uses Render for full-stack deployment.

✅ Backend Deployment
Render automatically detects render.yaml:

yaml
Copy
Edit
services:
  - type: web
    name: legalbuddy-backend
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port 10000
    envVars:
      - key: OPENROUTER_API_KEY
        sync: false
    plan: free
    region: oregon
✅ Add API Key
After creating the service, add this manually on Render dashboard:

Key: OPENROUTER_API_KEY

Value: your OpenRouter key

✅ Frontend Deployment
You can deploy ui_app.py on:

Streamlit Cloud

or host in same repo with streamlit run ui_app.py as service on Render.

📋 Sample Prompt
text
Copy
Edit
In 2014, a murder was reported in the XYZ district. The accused had a history of criminal offenses including theft and assault. The victim was a 45-year-old male, and the motive appeared to be personal enmity.
🧾 Sample Output
text
Copy
Edit
Judgment: Based on the evidence and motive, the accused is found guilty under Section 302 of IPC. Sentenced to life imprisonment...
✅ Future Scope
🔎 PDF Upload & Summarization

🧾 Case law citations from Indian Law APIs

🤖 Telegram bot for lawyers

📈 LLM fine-tuning using real legal datasets

🤝 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss your ideas.

📄 License
MIT License © Anandkumar
