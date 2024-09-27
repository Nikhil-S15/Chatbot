# app.py

import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from pricing import PricingModel
from model import ChatbotModel
from textblob import TextBlob

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Initialize the pricing model and chatbot model
pricing_model = PricingModel(base_price=100)
openai_api_key = os.getenv("OPENAI_API_KEY")  # Fetch the API key from environment variables
chatbot_model = ChatbotModel(api_key=openai_api_key)

class UserOffer(BaseModel):
    price: float
    user_message: str

def analyze_sentiment(user_message: str) -> float:
    """Analyze the sentiment of the user's message."""
    sentiment = TextBlob(user_message).sentiment
    return sentiment.polarity  # Polarity: -1 (negative) to 1 (positive)

@app.post("/start_negotiation")
async def start_negotiation():
    """Starts the negotiation and returns the initial price."""
    initial_price = pricing_model.base_price
    bot_message = chatbot_model.generate_response(f"The product price is ${initial_price}.")
    return {"bot_message": bot_message, "price": initial_price}

@app.post("/negotiate")
async def negotiate(user_offer: UserOffer):
    """Handles negotiation based on user's offer."""
    user_price = user_offer.price
    sentiment_score = analyze_sentiment(user_offer.user_message)

    # Adjust discount based on sentiment (politeness)
    pricing_model.max_discount = 0.40 if sentiment_score > 0.5 else 0.30

    result, bot_price = pricing_model.accept_or_counter(user_price)

    if result == "accepted":
        return {"bot_message": f"Offer accepted at ${bot_price}.", "final_price": bot_price}

    # Generate a response from the bot based on the negotiation
    bot_message = chatbot_model.generate_response(
        f"The user offered ${user_price}, but the current price is ${bot_price}."
    )
    return {"bot_message": bot_message, "counter_offer": bot_price}
