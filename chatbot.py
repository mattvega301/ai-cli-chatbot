from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [{ "role": "system", "content": "You are a helpful assistant that answers queries like a pirate."}]

print("Chatbot ready. Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        break

    messages.append({ "role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    reply = response.choices[0].message.content
    messages.append({ "role": "assistant", "content": reply})

    print(f"\nAI: {reply}\n")
