import os
import streamlit as st
from google import genai
from google.genai import types
st.set_page_config(page_title="Metro Rail AI Assistant", page_icon="🚇")
st.title("🚇 Metro Rail Passenger Guidance Bot")
st.write("Ask questions about ticket types, security checks, entry/exit process, and platform rules.")
SYSTEM_PROMPT = """
You are a Metro Rail Passenger Guidance AI.
Your role is to provide simple, clear explanations about metro travel procedures such as ticket types, entry and exit gates, security checks, and platform rules.
You are limited to informational guidance only.
You must not sell tickets, provide real-time train schedules, perform operational actions, or collect personal data.
If a request is outside scope, politely refuse and direct the user to official metro staff.
Use a friendly, calm, and public-service tone. Keep responses short and easy to understand.
you should answer only  only queries related to Metro Rail Passenger Guidance. you should not answer any other questions unrelated to Metro Rail Passenger Guidance.
"""

# User input
user_prompt = st.text_area("Enter your question:")

# Button
if st.button("Get Answer") and user_prompt.strip():
    try:
        # Create Gemini client
        client = genai.Client(
            api_key=("AIzaSyCGgKeUnYtwnPptA_ZwtBJhRGKC0hJM9QY")
        )

        # Combine system + user prompt
        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(
                        text=SYSTEM_PROMPT + "\nUser Question: " + user_prompt
                    )
                ]
            )
        ]

        with st.spinner("Generating response..."):
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=contents,
            )

        # Display response
        st.subheader("Response")
        st.write(response.text)

    except Exception as e:
        st.error(f"Error: {e}")

# Footer disclaimer
st.caption(
    "ℹ️ This assistant provides general metro passenger guidance only. "
    "No ticketing or real-time metro operations."
)
