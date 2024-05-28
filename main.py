import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize the Groq client with the API key
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def ai_tutor(prompt):
    """
    Generates a response to the user's question using the Groq API.
    """
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("Welcome to the AI Tutor. Type your questions below. Type 'exit' to end the session.")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            print("Exiting the AI Tutor. Goodbye!")
            break
        response = ai_tutor(user_input)
        print("AI Tutor:", response)
