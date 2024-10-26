import os
import openai
from dotenv import load_dotenv
from .base import BaseProvider

class OpenAIProvider(BaseProvider):
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def generate_response(self, prompt: str) -> str:
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # Or another available engine
                prompt=prompt,
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.7,
            )
            return response.choices[0].text.strip()
        except openai.error.OpenAIError as e:
            raise Exception(f"OpenAI API error: {str(e)}")