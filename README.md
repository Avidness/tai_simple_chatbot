# Thoughtful AI Customer Support Chatbot

This project is a **Streamlit-based chatbot** powered by **GPT-4-turbo**. It provides predefined answers to common Thoughtful AI questions and can generate answers dynamically for other queries using GPT-4.

## Features

- **Predefined responses**: Quickly answers common questions about Thoughtful AI.
- **GPT-4 dynamic responses**: Uses GPT-4 for any questions not in the predefined set.
- **Interactive UI**: Built with Streamlit, offering an easy-to-use chat interface.
- **Custom API key input**: Users provide their OpenAI API key to access GPT-4.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/thoughtful-ai-chatbot.git
   cd thoughtful-ai-chatbot
   ```   

1. **Install dependencies**:
```bash
Copy code
pip install -r requirements.txt
```

## Running the Chatbot

Run the following command to launch the app:

```bash
streamlit run tai_ai_agent.py
```

## Usage
1. Enter your OpenAI API key in the sidebar.
2. Ask questions, and the bot will respond:
  * Predefined responses for known Thoughtful AI queries.
  * GPT-4-generated answers for new questions.

## Example Questions
* "What does the eligibility verification agent (EVA) do?"
* "Tell me about Thoughtful AI's agents."

## Core Functionality
* Predefined Q&A: Hardcoded responses for specific questions.
* GPT-4 responses: Dynamically generated answers using OpenAI GPT-4 for other queries.

## License
Open-source under the MIT license.