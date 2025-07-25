# ui_app.py

import streamlit as st
import requests

BACKEND_URL = "https://legal-buddy-2.onrender.com/generate-judgment"
response = requests.post(BACKEND_URL, json={"prompt": user_input})

st.set_page_config(page_title="LegalBuddy AI", layout="centered")

st.title("⚖️ LegalBuddy AI")
st.write("Enter a case description, and the assistant will generate a legal judgment.")

case_description = st.text_area("📝 Case Description", height=200)

if st.button("Generate Judgment"):
    if not case_description.strip():
        st.warning("Please enter a case description.")
    else:
        with st.spinner("Generating judgment..."):
            try:
                response = requests.post(
                    "http://localhost:8000/generate-judgment",
                    json={"prompt": case_description}
                )
                result = response.json()
                st.success("✅ Judgment Generated:")
                st.write(result.get("judgment", "No response received."))

            except Exception as e:
                st.error(f"❌ Failed to connect to backend: {e}")
                

