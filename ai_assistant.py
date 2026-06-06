from groq import Groq

# API KEY
client = Groq(api_key="api key ")

# =====================
# STUDY ASSISTANT MEMORY
# =====================
study_history = [
    {
        "role": "system",
        "content": """You are an expert AI study assistant.
                   Remember everything the student studies.
                   Track their progress carefully.
                   When asked, quiz them on weak topics.
                   Always encourage and motivate them.
                   Keep track of topics they have covered.
                   Suggest what to study next."""
    }
]

# Track studied topics
studied_topics = []
quiz_scores = {}

# =====================
# STUDY CHAT FUNCTION
# =====================
def study_chat(message):
    
    study_history.append({
        "role": "user",
        "content": message
    })
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=study_history
    )
    
    ai_response = response.choices[0].message.content
    
    study_history.append({
        "role": "assistant",
        "content": ai_response
    })
    
    return ai_response

# =====================
# ADD TOPIC FUNCTION
# =====================
def add_topic(topic):
    studied_topics.append(topic)
    response = study_chat(
        f"I just studied '{topic}'. "
        f"Please acknowledge and give me "
        f"a brief summary of key points!"
    )
    print(f"\n📚 Topic Added: {topic}")
    print(f"🤖 Assistant: {response}")

# =====================
# QUIZ FUNCTION
# =====================
def take_quiz(topic):
    print(f"\n📝 QUIZ on: {topic}")
    print("="*50)
    
    # Get quiz question
    question = study_chat(
        f"Give me ONE quiz question about '{topic}'. "
        f"Just the question, nothing else!"
    )
    print(f"Question: {question}")
    
    # Get student answer
    answer = input("\nYour answer: ")
    
    # Check answer
    result = study_chat(
        f"My answer was: '{answer}'. "
        f"Is this correct? Give feedback!"
    )
    print(f"\n🤖 Feedback: {result}")

# =====================
# SHOW PROGRESS
# =====================
def show_progress():
    print("\n📊 YOUR STUDY PROGRESS:")
    print("="*50)
    if studied_topics:
        print("Topics studied:")
        for i, topic in enumerate(studied_topics, 1):
            print(f"{i}. ✅ {topic}")
    else:
        print("No topics studied yet!")
    print(f"\nTotal topics: {len(studied_topics)}")
    print("="*50)

# =====================
# INTERACTIVE ASSISTANT
# =====================
def run_study_assistant():
    print("="*50)
    print("🎓 AI STUDY ASSISTANT")
    print("="*50)
    print("Commands:")
    print("'add [topic]'  → Add studied topic")
    print("'quiz [topic]' → Take a quiz")
    print("'progress'     → Show progress")
    print("'help'         → Get study help")
    print("'quit'         → Exit")
    print("="*50)
    
    while True:
        user_input = input("\n👤 You: ").strip()
        
        if user_input.lower() == 'quit':
            print("Keep studying! Goodbye! 👋")
            break
        
        elif user_input.lower().startswith('add '):
            topic = user_input[4:]
            add_topic(topic)
        
        elif user_input.lower().startswith('quiz '):
            topic = user_input[5:]
            take_quiz(topic)
        
        elif user_input.lower() == 'progress':
            show_progress()
        
        elif not user_input:
            continue
        
        else:
            response = study_chat(user_input)
            print(f"\n🤖 Assistant: {response}")

# =====================
# TEST IT!
# =====================
print("Testing Study Assistant...")
print("="*50)

# Add some topics
add_topic("Machine Learning")
add_topic("RAG Systems")
add_topic("API Development")

# Show progress
show_progress()

# Take a quiz
take_quiz("Machine Learning")

# Start interactive
print("\n" + "="*50)
run_study_assistant()