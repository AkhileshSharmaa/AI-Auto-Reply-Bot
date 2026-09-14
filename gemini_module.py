from google import genai
from config import API_KEY, GEMINI_MODEL

client = genai.Client(
    api_key=API_KEY
)

def generate_reply(chat_history):
    """
    Sends the chat history to Gemini
    and returns a natural reply.
    """

    prompt = f"""
    You are helping me write a reply to a personal chat.

    Read the conversation and write the next natural reply.

    Rules:

    - Reply like a normal person texting.
    - Keep the response short and natural.
    - Match the tone of the conversation.
    - Use casual language when appropriate.
    - Do not write long explanations.
    - Do not mention AI.
    - Do not mention Gemini.
    - Do not explain what you are doing.
    - Do not use quotation marks.
    - Output ONLY the message that should be sent.

    Conversation:

    {chat_history}
                  """
    
    try:

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        if response.text:
            return response.text.strip()

        return "Sorry, I couldn't generate a reply."

    except Exception as e:
        print("Gemini Error:", e)

        return None