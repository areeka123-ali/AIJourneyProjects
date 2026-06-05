!pip install groq
from groq import Groq

# API KEY
client = Groq(api_key="api key")

# =====================
# CONTENT GENERATOR
# =====================
def generate_content(content_type, topic, tone, language):
    
    # Different prompts for different content
    prompts = {
        "blog": f"Write a detailed blog post about '{topic}' in {tone} tone in {language} language.",
        "email": f"Write a professional email about '{topic}' in {tone} tone in {language} language.",
        "social": f"Write an engaging social media post about '{topic}' in {tone} tone in {language} language. Include hashtags!",
        "tweet": f"Write a tweet about '{topic}' in {tone} tone in {language} language. Max 280 characters!"
    }
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert content writer. Write engaging and professional content."
            },
            {
                "role": "user",
                "content": prompts[content_type]
            }
        ]
    )
    return response.choices[0].message.content

# =====================
# TEST IT!
# =====================

# Blog post
print("📝 BLOG POST:")
print("="*50)
print(generate_content(
    content_type="blog",
    topic="pakistani women in technology",
    tone="inspirational",
    language="English"
))

print("\n📧 EMAIL:")
print("="*50)
print(generate_content(
    content_type="email",
    topic="Project completion update",
    tone="formal",
    language="English"
))

print("\n📱 SOCIAL MEDIA POST:")
print("="*50)
print(generate_content(
    content_type="social",
    topic="AI journey in UET peshawar",
    tone="casual",
    language="English"
))

print("\n🐦 TWEET:")
print("="*50)
print(generate_content(
    content_type="tweet",
    topic="completed my first ai project",
    tone="enthusiastic",
    language="English"
))