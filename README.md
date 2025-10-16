# AI_Auto_Reply
An AI-powered virtual assistant that interacts with users via chat applications or interfaces. It combines OpenAI’s GPT model, PyAutoGUI, and clipboard automation to read chats, analyze messages, and automatically respond — mimicking human-like conversational behavior.

## Features

+   AI-Powered Conversations: Uses OpenAI GPT model for smart, bilingual responses (Hindi + English).
+   Auto Message Detection: Monitors chat logs and detects when specific users send messages.
+   Automated Reply System: Copies new messages, generates a reply, and sends it automatically.
+   Cursor Tracker Utility: Helps identify precise screen coordinates for automation.
+   Custom Personalities: You can easily modify the assistant’s behavior or personality (like Pikachu, Squirtle, etc.).

## Requirements
pyautogui
openai

## Setup

1. Clone or download the repository:

git clone https://github.com/yourusername/AI_Voice_Assistant.git
cd AI_Voice_Assistant

2. Create a virtual environment (optional but recommended):

python -m venv .venv
.venv\Scripts\activate    # On Windows
source .venv/bin/activate # On Linux/Mac

3. Add your OpenAI API key:

Open both bot.py and openai.py, and replace this line with your actual key:

client = OpenAI(api_key = "<Your Key Here>")
