from groq import Groq

# API KEY
client = Groq(api_key="api keys")

# =====================
# CONTEXT CACHE (Memory)
# =====================
conversation_history = [
    {
        "role": "system",
        "content": """You are a helpful AI assistant.
                   Remember everything the user tells you.
                   Use their name when you know it.
                   Reference previous messages naturally."""
    }
]

# =====================
# MEMORY CHAT FUNCTION
# =====================
def memory_chat(user_message):
    
    # Add user message to history
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    # Send FULL history to AI
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history  # ← FULL HISTORY!
    )
    
    # Get AI response
    ai_response = response.choices[0].message.content
    
    # Save AI response to history
    conversation_history.append({
        "role": "assistant",
        "content": ai_response
    })
    
    # Show memory size
    print(f"🧠 Memory: {len(conversation_history)} messages stored")
    
    return ai_response

# =====================
# SHOW MEMORY FUNCTION
# =====================
def show_memory():
    print("\n📝 CONVERSATION HISTORY:")
    print("="*50)
    for i, msg in enumerate(conversation_history):
        if msg["role"] != "system":
            role = "👤 You" if msg["role"] == "user" else "🤖 AI"
            print(f"{role}: {msg['content'][:100]}...")
    print("="*50)

# =====================
# INTERACTIVE CHATBOT
# =====================
def run_memory_chatbot():
    print("="*50)
    print("🧠 MEMORY CHATBOT")
    print("="*50)
    print("Commands:")
    print("'quit'   → Exit")
    print("'memory' → Show conversation history")
    print("'clear'  → Clear memory")
    print("="*50)
    
    while True:
        user_input = input("\n👤 You: ")
        
        if user_input.lower() == 'quit':
            print("Goodbye! 👋")
            break
        
        if user_input.lower() == 'memory':
            show_memory()
            continue
        
        if user_input.lower() == 'clear':
            conversation_history.clear()
            conversation_history.append({
                "role": "system",
                "content": "You are a helpful assistant with memory."
            })
            print("🗑️ Memory cleared!")
            continue
        
        if not user_input.strip():
            continue
        
        response = memory_chat(user_input)
        print(f"\n🤖 AI: {response}")

# =====================
# TEST MEMORY!
# =====================
print("Testing memory...")
print("="*50)

# Test conversation
responses = [
    "My name is Areeka",
    "I study at UET Peshawar",
    "I am learning AI and doing internship",
    "What is my name?",           # Should remember!
    "Where do I study?",          # Should remember!
    "What am I learning?"         # Should remember!
]

for message in responses:
    print(f"\n👤 You: {message}")
    response = memory_chat(message)
    print(f"🤖 AI: {response}")

# Start interactive chatbot
print("\n" + "="*50)
print("Starting interactive memory chatbot!")
run_memory_chatbot()