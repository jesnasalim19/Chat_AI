import streamlit as st
from google import genai
from config import GEMINI_API_KEY

gemini_client = genai.Client(
    api_key=GEMINI_API_KEY
)

st.set_page_config(
    page_icon="💬",
    page_title="Chat_AI"
)

st.title("💬 Chat_AI")
st.write("-----------------")

prompt = st.chat_input(
    placeholder="Ask Anything?..."
)

if prompt:
    with st.spinner("Generating answer..."):
        response = gemini_client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

    st.subheader("Answer")
    st.write("-----------------")
    st.write(response.text)
