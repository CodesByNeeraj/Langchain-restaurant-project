# Restaurant Name Generator
I had real fun building this Restaurant Name Generator app! This web application helps you come up with a creative and catchy name for your restaurant based on the cuisine of your choice. In addition, it suggests a list of menu items that fit the vibe of your restaurant.

The app is built using Streamlit and powered by Langchain, an innovative framework for creating LLM-based (Large Language Model) applications. It generates restaurant names and food items dynamically based on your chosen cuisine.

## Features
Choose a cuisine (Indian, Chinese, British, or Malay) from the sidebar.

![dropdown menu](dropdownmenu.png)

Get a fancy restaurant name suggestion.

Receive a list of menu items based on the restaurant's name.

All results are generated using an AI language model.

Some examples:

![dropdown menu](democuisine.png)
![dropdown menu](democuisine2.png)

## Tools Used
Streamlit: Used to build and deploy the web app.

Langchain: A framework for working with large language models like OpenAI’s GPT to chain multiple prompts and responses.

OpenAI GPT (via Langchain): For generating creative restaurant names and menu items.

Python: Backend language for app logic.

## Requirements
Before running the app locally, you need to have Python and some packages installed. Here’s what you need:

Python 3.x (preferably 3.9+)

Install the necessary Python libraries via requirements.txt.

You will also need your own OpenAI API key to run the app because the app makes use of OpenAI's API to generate the content.

## Steps to run the project 
1. Create a virtual environment (to keep this project's dependencies isolated)

python -m venv venv

This makes a clean Python environment in a folder called venv.

2. Activate it

On MacOS/Linux: source venv/bin/activate

On Windows: venv\Scripts\activate

You'll know it’s activated if your terminal prompt changes (usually it shows (venv) at the start).

3. Install dependencies

pip install -r requirements.txt

This reads the requirements.txt file and installs everything this project needs.

4. Run Main.py

python Main.py


