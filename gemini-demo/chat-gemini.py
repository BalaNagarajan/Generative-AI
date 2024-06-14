import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def chat_with_gemini():
    # Assign the model you want to use - best text understanding model
    model = genai.GenerativeModel("gemini-pro")
    # Generate the content
    response = model.generate_content("List all popular movies 2023 ?")
    # Display the content
    st.write(response.text)


if __name__ == "__main__":
    chat_with_gemini()
