from groq import Groq

# API KEY
client = Groq(api_key="api key ")

# =====================
# CUSTOMER SERVICE BOT
# =====================
conversation_history = [
    {
        "role": "system",
        "content": """You are a professional customer 
                   service agent for TechStore Pakistan.
                   
                   Store Information:
                   - We sell laptops, phones, tablets
                   - Delivery: 3-5 working days
                   - Return policy: 7 days
                   - Payment: Cash, Card, EasyPaisa
                   - Working hours: 9AM - 9PM
                   
                   Your job:
                   - Remember customer name and details
                   - Handle complaints professionally
                   - Track their orders
                   - Always be polite and helpful
                   - Speak in English or Urdu as needed
                   - End every message with 
                     'Is there anything else I can help?'"""
    }
]

# Customer info tracker
customer_info = {
    "name": None,
    "order_id": None,
    "complaint": None,
    "status": "new"
}

# =====================
# SERVICE FUNCTION
# =====================
def customer_service(message):
    
    conversation_history.append({
        "role": "user",
        "content": message
    })
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history
    )
    
    ai_response = response.choices[0].message.content
    
    conversation_history.append({
        "role": "assistant",
        "content": ai_response
    })
    
    return ai_response

# =====================
# ORDER STATUS FUNCTION
# =====================
def check_order(order_id):
    # Simulate order database
    orders = {
        "ORD001": "Delivered ✅",
        "ORD002": "In Transit 🚚",
        "ORD003": "Processing ⏳",
        "ORD004": "Cancelled ❌"
    }
    
    if order_id in orders:
        return orders[order_id]
    return "Order not found!"

# =====================
# SHOW CONVERSATION
# =====================
def show_conversation():
    print("\n📝 CONVERSATION HISTORY:")
    print("="*50)
    for msg in conversation_history:
        if msg["role"] == "user":
            print(f"👤 Customer: {msg['content']}")
        elif msg["role"] == "assistant":
            print(f"🤖 Agent: {msg['content'][:100]}...")
    print("="*50)

# =====================
# RUN SERVICE BOT
# =====================
def run_customer_service():
    print("="*50)
    print("🛒 TECHSTORE PAKISTAN")
    print("Customer Service Bot")
    print("="*50)
    print("Commands:")
    print("'order [id]'  → Check order status")
    print("'history'     → Show conversation")
    print("'quit'        → Exit")
    print("="*50)
    
    # Welcome message
    welcome = customer_service(
        "Greet the customer professionally!"
    )
    print(f"\n🤖 Agent: {welcome}")
    
    while True:
        user_input = input("\n👤 Customer: ").strip()
        
        if user_input.lower() == 'quit':
            print("Thank you for contacting us! 👋")
            break
        
        elif user_input.lower().startswith('order '):
            order_id = user_input[6:].upper()
            status = check_order(order_id)
            print(f"\n📦 Order {order_id}: {status}")
            response = customer_service(
                f"Customer asked about order {order_id}. "
                f"Status is: {status}"
            )
            print(f"🤖 Agent: {response}")
        
        elif user_input.lower() == 'history':
            show_conversation()
        
        elif not user_input:
            continue
        
        else:
            response = customer_service(user_input)
            print(f"\n🤖 Agent: {response}")

# =====================
# TEST IT!
# =====================
print("Testing Customer Service Bot...")
print("="*50)

# Simulate customer conversation
test_messages = [
    "Hi my name is Areeka",
    "I ordered a laptop but haven't received it",
    "My order ID is ORD002",
    "When will it arrive?",
    "What is your return policy?",
    "Can I pay with EasyPaisa?"
]

for message in test_messages:
    print(f"\n👤 Customer: {message}")
    response = customer_service(message)
    print(f"🤖 Agent: {response}")
    print("-"*50)

# Start interactive
print("\n" + "="*50)
run_customer_service()