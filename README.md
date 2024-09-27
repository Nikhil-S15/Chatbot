# Chatbot# Chatbot
# Negotiation Chatbot

This project implements a negotiation chatbot using FastAPI and the OpenAI API. The chatbot simulates a negotiation process between a customer and a supplier, allowing the user to propose offers and receive responses based on the negotiation logic and AI model.

## Features

- Basic conversation flow for negotiation.
- Pricing logic that includes counteroffers and discounts.
- Integration with OpenAI's ChatGPT for conversation handling.
- Optional sentiment analysis to adjust negotiation strategies.

## Requirements

- Python 3.7 or higher
- FastAPI
- OpenAI Python client
- Pydantic
- TextBlob
- Python-dotenv

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/negotiation_chatbot.git
2.Navigate to the project directory:
cd negotiation_chatbot
3.Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
4.Install the required dependencies:
pip install -r requirements.txt
5.Setup
Create a .env file in the project root directory.
6.Add your OpenAI API key to the .env file:
OPENAI_API_KEY=your_openai_api_key_here
7.Start the FastAPI application:
uvicorn app:app --reload

