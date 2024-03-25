# Import the `os` module for working with the operating system (not strictly necessary here)
import os

# Import the `OpenAI` class for interacting with the OpenAI API
from langchain_openai.llms import OpenAI

# Import the `openai_key` variable from the `constants` module
# (Assuming `constants.py` holds your OpenAI API key securely)
from constants import openai_key

# Import `PromptTemplate` from `langchain.prompts` (for creating structured prompts)
from langchain.prompts import PromptTemplate

# Import `LLMChain` from `langchain.chains` (for building LLM workflows)
from langchain.chains import LLMChain

# Import Streamlit for building a web app interface
import streamlit as st

# Set OpenAI API key as environment variable (security note: consider env variables)
os.environ["OPENAI_API_KEY"] = openai_key

# Create a Streamlit app title
st.title("Langchain Demo: Movie Search")

# Text input field for user to search by movie type
movie_type = st.text_input("Search Movie Type (e.g., Horror, Comedy)")

# Text input field for user to specify movie year (optional)
movie_year = st.text_input("Enter Movie Year (Optional)")  # Allow empty input

# Define a function to generate movie names based on user input
def generate_movie_names(movie_type, year):
  """Generates movie names using the OpenAI Large Language Model (LLM).

  This function creates an OpenAI LLM object, uses a prompt template to influence
  the output based on movie type and year (if provided), and returns the generated response.

  Args:
      movie_type (str): The type of movie to search for.
      year (str, optional): The year the movie was released (optional).

  Returns:
      dict: A dictionary containing the generated movie name(s) under the key "text".
  """

  # Create an OpenAI LLM object with a temperature of 0.7 (controls creativity)
  llm = OpenAI(temperature=0.7)

  # Define a prompt template with placeholders for 'movie_type' and 'year' (optional)
  prompt_template_name = PromptTemplate(input_variables=['movie_type', 'year'],
                                         template="Top must watch {movie_type} movies came in {year}")

  # Create an LLMChain that combines the LLM object, prompt template, and specifies output key
  movie_name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="text")

  # Call the LLMChain with user-provided movie type and year (if entered)
  response = movie_name_chain({'movie_type': movie_type, 'year': year})

  # Return the generated response (dictionary containing the movie name(s))
  return response

# Check if the script is run directly (not needed in Streamlit, commented out)
# if __name__ == "__main__":
#   pass  # Removed as Streamlit handles execution flow

# Call the generate_movie_names function based on user input
movie_obj = generate_movie_names(movie_type, movie_year)

# Display the generated movie name(s) from the response dictionary
st.write(movie_obj['text'])
