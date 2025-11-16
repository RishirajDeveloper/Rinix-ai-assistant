import os
from groq import Groq

# Initialize client with error handling
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("Warning: GROQ_API_KEY environment variable not set. Chatbot functionality will be limited.")
    client = None
else:
    client = Groq(api_key=api_key)

def ChatBot(query):
    """
    Generates a response using Groq's AI model.
    """
    if client is None:
        return "I'm sorry, but I can't access the AI service right now. Please check your API key configuration."

    try:
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful AI assistant. Respond in a friendly, witty manner like Tony Stark's Jarvis."},
                {"role": "user", "content": query}
            ],
            temperature=0.7,
            max_tokens=150,
            top_p=1,
            stream=False,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"
