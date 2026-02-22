import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 1. FIX: Switch to v1beta to support system_instruction properly
client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(api_version="v1beta")
)

# 2. Production-Grade System Prompt
SYSTEM_PROMPT = """
You are a professional, conservative Financial Advisor AI. 
Provide educational information on budgeting, saving, and general investment concepts.

CONSTRAINTS:
1. NEVER provide specific stock or crypto "buy" or "sell" recommendations.
2. ALWAYS include this disclaimer in your first message: 
   "I am an AI, not a certified financial professional."
3. Keep responses structured with bullet points for readability.
"""

def initialize_chat():
    """Starts a chat session with the correct configuration."""
    return client.chats.create(
        model="gemini-2.5-flash", 
        config=types.GenerateContentConfig(
            # FIX: Must be snake_case in the Python SDK
            system_instruction=SYSTEM_PROMPT, 
            temperature=0.7,
        )
    )

def get_chat_response_stream(chat_session, user_input):
    """Generates a streaming response."""
    try:
        # Proper streaming method for the modern SDK
        return chat_session.send_message_stream(user_input)
    except Exception as e:
        return f"⚠️ Financial Engine Error: {str(e)}"