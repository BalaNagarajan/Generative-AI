# Import the `openai_key` variable from the `constants` module
from constants import openai_key

# Import the `OpenAI` class for interacting with the OpenAI API
from langchain_openai.llms import OpenAI

# Import the `os` module for working with the operating system
import os


# Set OpenAI API key as environment variable
os.environ["OPENAI_API_KEY"] = openai_key

# Define a function to generate a movie name
def generate_movie_name():
  """Generates a movie name using the OpenAI Large Language Model (LLM).

  This function creates an OpenAI LLM object, sends a prompt asking for
  top movie names, and returns the generated response.

  Returns:
      str: The generated movie name (or error message if unsuccessful).
  """

  # Create an OpenAI LLM object with a temperature of 0.7 (controls creativity)
  llm = OpenAI(temperature=0.7)

  # Prompt: Ask the LLM to generate a list of top movie names
  prompt = "Enter the top 5 must-watch movie names"
  temperature=0.7

  # Call the LLM object with the prompt and get the response
  response = llm.invoke(prompt, temperature=temperature)  # Using recommended 'invoke'

  # Extract and return the content of the response (the generated text)
  return response

# Check if the script is run directly (not imported as a module)
if __name__ == "__main__":

  # Call the generate_movie_name function to get a movie name
  movie_name = generate_movie_name()

  # Print the generated movie name in a formatted way
  print(f"Top Must-Watch Movie Name: {movie_name}")