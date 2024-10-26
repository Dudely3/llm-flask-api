import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

from providers.openai_provider import OpenAIProvider
from providers.ollama_provider import OllamaProvider
from providers.base import BaseProvider

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

def get_provider() -> BaseProvider:
    provider_name = os.getenv("MODEL_PROVIDER", "openai").lower()
    if provider_name == "ollama":
        base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        return OllamaProvider(base_url=base_url)
    else:
        return OpenAIProvider()

# Initialize the provider
provider = get_provider()

@app.route('/api/query', methods=['POST'])
def query_model():
    try:
        data = request.get_json()
        if not data or 'prompt' not in data:
            return jsonify({"error": "Missing 'prompt' in request body"}), 400
        
        prompt = data['prompt']
        response = provider.generate_response(prompt)
        return jsonify({"response": response}), 200

    except Exception as e:
        # Log the error as needed
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "LLM Flask API is running."}), 200

if __name__ == '__main__':
    # For development only; use Gunicorn in production
    app.run(host='0.0.0.0', port=5000, debug=True)