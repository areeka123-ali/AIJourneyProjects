from groq import Groq
import time

# API KEY
client = Groq(api_key="api key")

# =====================
# STREAMING FUNCTION
# =====================
def stream_chat(message, personality="helpful assistant"):
    
    print(f"\n🤖 Bot: ", end="", flush=True)
    
    # Create streaming response
    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": f"You are a {personality}"
            },
            {
                "role": "user",
                "content": message
            }
        ],
        stream=True  # ← THIS enables streaming!
    )
    
    # Print words one by one!
    full_response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content:
            word = chunk.choices[0].delta.content
            print(word, end="", flush=True)
            full_response += word
    
    print()  # new line at end
    return full_response

# =====================
# INTERACTIVE CHATBOT
# =====================
def run_chatbot():
    print("="*50)
    print("🤖 STREAMING CHATBOT")
    print("="*50)
    print("Type 'quit' to exit")
    print("Type 'clear' to clear history")
    print("="*50)
    
    while True:
        user_input = input("\n👤 You: ")
        
        if user_input.lower() == 'quit':
            print("Goodbye! 👋")
            break
            
        if user_input.lower() == 'clear':
            print("Chat cleared! ✅")
            continue
            
        if not user_input.strip():
            continue
            
        stream_chat(user_input)

# =====================
# TEST STREAMING FIRST
# =====================
print("Testing streaming...")
stream_chat("Tell me about Artificial Intelligence in 3 sentences")

print("\n" + "="*50)
print("Now starting interactive chatbot...")
print("="*50)

# Start chatbot
run_chatbot()