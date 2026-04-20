import streamlit as st
from openai import OpenAI

st.title("🤖 Gen AI Chatbot")
api_key = st.text_input("Enter API Key", type="password")

if api_key:
    client = OpenAI(api_key=api_key)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input("Ask something"):
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages
        )

        reply = response.choices[0].message.content
        st.chat_message("assistant").write(reply)

        st.session_state.messages.append({"role": "assistant", "content": reply})