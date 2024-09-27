# model.py

import openai

class ChatbotModel:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def generate_response(self, prompt: str) -> str:
        """Generates a response from the AI model."""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100
            )
            return response['choices'][0]['message']['content']
        except openai.error.RateLimitError:
            return "Error: You have exceeded your rate limit. Please try again later."
        except openai.error.InvalidRequestError as e:
            return f"Error: Invalid request - {str(e)}"
        except Exception as e:
            return f"Error: {str(e)}"
