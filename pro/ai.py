from openai import OpenAI

# Read API key from file
with open("openai_key.txt", "r") as f:
    key = f.read().strip()

# Initialize client
client = OpenAI(api_key=key)

# Message history
messages = []

def completion(user_message):
    global messages
    
    messages.append({"role": "user", "content": user_message})
    
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    assistant_reply = chat_completion.choices[0].message.content
    
    messages.append({"role": "assistant", "content": assistant_reply})
    
    print("Jarvis:", assistant_reply)

if __name__ == "__main__":
    user_question = input("Hello, my name is Jarvis. How may I help you? ")
    completion(user_question)
