import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai


# Load environment variables from .env file
load_dotenv()

# Configure your API key
genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))


# Iterate over the list of models
for mod in genai.list_models():
    # Check if the model supports content generation
    if 'generateContent' in mod.supported_generation_methods:
        # Display the model
        st.write(mod)




