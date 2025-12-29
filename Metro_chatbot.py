#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Install dependencies
# pip install streamlit google-genai

import os
import streamlit as st
from google import genai
from google.genai import types

# Streamlit page setup
st.set_page_config(page_title="Metro Rail AI Assistant", page_icon="🚇")
st.title("🚇 Metro Rail Passenger Guidance Bot")
st.write("Ask questions about ticket types, security checks, entry/exit process, and platform rules.")

# User input
user_input = st.text_area("Enter your question:")

# Generate response
if st.button("Get Answer") and user_input.strip():
    try:
        client = genai.Client(
            api_key=("AIzaSyCGgKeUnYtwnPptA_ZwtBJhRGKC0hJM9QY"),
        )

        model = "gemini-3-flash-preview"

        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=user_input)],
            )
        ]

        generate_content_config = types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                thinking_level="HIGH",
            )
        )

        response_text = ""

        with st.spinner("Generating response..."):
            for chunk in client.models.generate_content_stream(
                model=model,
                contents=contents,
                config=generate_content_config,
            ):
                if chunk.text:
                    response_text += chunk.text

        st.subheader("Response")
        st.write(response_text)

    except Exception as e:
        st.error(f"Error: {e}")

# Footer disclaimer
st.caption("ℹ️ This assistant provides general metro passenger guidance only. No ticketing or real-time operations.")

