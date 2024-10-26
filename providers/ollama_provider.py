import requests
from .base import BaseProvider

class OllamaProvider(BaseProvider):
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url  # Adjust the port if different

    def generate_response(self, prompt: str) -> str:
        try:
            payload = {
                "prompt": prompt,
                "model": "llama2:13b-chat",  # Replace with your specific model name
                #"max_tokens": 150,
                #S"temperature": 0.7,
                "stream": False
            }
            response = requests.post(f"{self.base_url}/api/generate", json=payload)
            response.raise_for_status()
            data = response.json()
            return data.get("response", "").strip()
        except requests.RequestException as e:
            raise Exception(f"Ollama API error: {str(e)}")