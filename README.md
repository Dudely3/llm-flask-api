# llm-flask-api
API for communicating with an llm provider


Can call either ollama or openAI models. 


Create a .env file with these lines:

OPENAI_API_KEY=your-openai-api-key-here

MODEL_PROVIDER=ollama # Change to 'openai' to use chatgpt

OLLAMA_BASE_URL=http://localhost:11434  # Adjust if different
