COLORS = {"openai": "🟢", "gemini": "🔵"}

PROVIDER_LABELS = ["Gemini", "OpenAI"]

PROVIDER_MODELS = {
    "openai": ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"],
    "gemini": ["gemini-2.5-pro", "gemini-2.5-flash-lite", "gemini-2.5-flash"],
}

SYSTEM_PROMPT = """You are a helpful assistant AI. You will be provided
with \
the chat history and the current user message. Use this information to 
generate \
a relevant and helpful response.

Chat History: {chat_history}

Should be a response that is appropiate for the user's message: {messages} 
"""