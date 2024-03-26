# Lang Chain Basics

Project Setup:
===============
1. You can use any package manager , I have used Conda for packet management. 	Conda is an open-source package management system and environment management system for installing multiple versions of software packages and their dependencies and managing different environments within which to run them. It is particularly popular in the Python ecosystem but can be used for other languages as well. Conda allows users to easily install, uninstall, and update packages and create isolated environments with specific sets of packages and versions.
2. Install Conda - **pip install conda**
3. Virtual Environment : The reason we need to create the virtual environment to have dependency isolation (To isolate each project dependencies to different project) and clean development environment (clean state for your project dependencies and you don’t install any dependency packages globally.
Create a empty folder and go to the folder and execute the command “**conda create -p venv python=<Python_VERSION> -y**” (Here venv is the virtual environment for the project).
4. Activate the project - **conda activate venv/**
5. Let’s create a new file “requirements.txt” to add all the dependencies / libraries required
6. **pip install -r requirements.txt**  (Command is used in Python to install dependencies listed in a requirements file) . ‘-r’ – This flag tells pip to read package names and their versions from requirements file.

**Examples:**
• **Basic text search **
1. **constants.py** - You can store the OPEN API key in this file and import in your modules. This is not a recommended approach, just for your local development purpose.
2. **movie_list_llm_search.py** (Without Prompt Template) - Generates top movie names list using the OpenAI Large Language Model (LLM)
           a. **Dependencies** : `OpenAI` class for interacting with the OpenAI API | `os` module for working with the operating system | `openai_key` variable from the `constants` module
•**Basic text search using Prompt Template**
3. **movie_list_search_using_template.py** (Using Prompt Template) - creates an OpenAI LLM object, uses a prompt template to influence  the output, and returns the generated response.
          a. **Dependencies : ** `OpenAI` class for interacting with the OpenAI API | `os` module for working with the operating system | `openai_key` variable from the `constants` module | `PromptTemplate` from 
               `langchain.prompts` (for creating structured prompts) | `LLMChain` from `langchain.chains` (for building LLM workflows).
 Execute : **python movie_list_llm_search.py | python movie_list_search_using_template.py**

•**Basic text search using Prompt Template + Streamlit (Web-based)**   
4. **movie_list_search_streamlit.py** : Performing the same movie search through simple web interface  using streamlit
          a.  **Dependencies** : `OpenAI` class for interacting with the OpenAI API | `os` module for working with the operating system | `openai_key` variable from the `constants` module | `PromptTemplate` from 
               `langchain.prompts` (for creating structured prompts) | `LLMChain` from `langchain.chains` (for building LLM workflows) | Streamlit for building a web app interface
     Execute  :   **streamlit run movie_list_search_streamlit.py**   

