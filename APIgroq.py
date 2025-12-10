from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

class Agent():
    def __init__(self):
        self.groqclient = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def ask(self,message):
        chat_completion = self.groqclient.chat.completions.create(
        messages=[
            # Set an optional system message. This sets the behavior of the
            # assistant and can be used to provide specific instructions for
            # how it should behave throughout the conversation.
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            # Set a user message for the assistant to respond to.
            {
                "role": "user",
                "content": message,
            }
        ],

            # The language model which will generate the completion.
            model="llama-3.3-70b-versatile"
        )

        # Print the completion returned by the LLM.
        return chat_completion.choices[0].message.content




