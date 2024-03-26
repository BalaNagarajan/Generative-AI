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
