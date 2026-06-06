from groq import Groq

# API KEY
client = Groq(api_key="api key")

# =====================
# PERSONALITIES
# =====================
personalities = {
    "teacher": """You are a friendly teacher.
                Explain everything simply.
                Use examples and analogies.
                Always encourage learning.""",
    
    "doctor": """You are a professional doctor.
               Give health advice carefully.
               Always recommend consulting
               a real doctor for serious issues.""",
    
    "comedian": """You are a funny comedian.
                 Make every answer humorous.
                 Use jokes and puns.
                 Keep it light and fun!""",
    
    "motivator": """You are an energetic life coach.
                  Always motivate and encourage.
                  Use powerful positive words.
                  Make people feel unstoppable!""",
    
    "developer": """You are an expert software developer.
                  Answer everything related to coding.
                  Give code examples when needed.
                  Use technical terms properly.""",
    
    "einstein": """You are Albert Einstein.
                 Speak like a genius scientist.
                 Relate everything to physics
                 and science. Use deep thinking."""
}

# =====================
# PERSONALITY CHAT
# =====================
def personality_chat(message, personality_type):
    
    if personality_type not in personalities:
        return "Invalid personality type!"
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": personalities[personality_type]
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )
    return response.choices[0].message.content

# =====================
# INTERACTIVE CHATBOT
# =====================
def run_personality_chatbot():
    print("="*50)
    print("🎭 PERSONALITY CHATBOT")
    print("="*50)
    print("Available personalities:")
    print("1. teacher")
    print("2. doctor")
    print("3. comedian")
    print("4. motivator")
    print("5. developer")
    print("6. einstein")
    print("="*50)
    
    # Choose personality
    personality = input("Choose personality: ").lower()
    
    if personality not in personalities:
        print("Invalid! Using teacher as default!")
        personality = "teacher"
    
    print(f"\n✅ Chatting with: {personality.upper()}")
    print("Type 'quit' to exit")
    print("Type 'switch' to change personality")
    print("="*50)
    
    while True:
        user_input = input("\n👤 You: ")
        
        if user_input.lower() == 'quit':
            print("Goodbye! 👋")
            break
        
        if user_input.lower() == 'switch':
            personality = input("Choose new personality: ").lower()
            print(f"✅ Switched to: {personality.upper()}")
            continue
        
        if not user_input.strip():
            continue
        
        response = personality_chat(user_input, personality)
        print(f"\n🤖 {personality.upper()}: {response}")

# =====================
# TEST ALL PERSONALITIES
# =====================
question = "What is Artificial Intelligence?"

print("Testing all personalities with same question!")
print(f"Question: {question}\n")

for personality in personalities:
    print(f"\n{'='*50}")
    print(f"🎭 {personality.upper()}:")
    print("="*50)
    response = personality_chat(question, personality)
    print(response)

# Start interactive chatbot
print("\n" + "="*50)
run_personality_chatbot()