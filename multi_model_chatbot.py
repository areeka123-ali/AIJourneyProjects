!pip install groq
!pip install google-generativeai
import groq
import time

# API KEY
GROQ_KEY = "api key"

# Setup client
groq_client = groq.Groq(api_key=GROQ_KEY)

# =====================
# ASK LLAMA FUNCTION
# =====================
def ask_llama(question):
    start = time.time()
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": question}]
    )
    end = time.time()
    return {
        "answer": response.choices[0].message.content,
        "time": round(end - start, 2),
        "tokens": response.usage.total_tokens
    }

# =====================
# ASK MIXTRAL FUNCTION
# =====================
def ask_mixtral(question):
    start = time.time()
    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",  # ← change here!
        messages=[{"role": "user", "content": question}]
    )
    end = time.time()
    return {
        "answer": response.choices[0].message.content,
        "time": round(end - start, 2),
        "tokens": response.usage.total_tokens
    }

# =====================
# COMPARE FUNCTION
# =====================
def compare_models(question):
    print(f"\n{'='*50}")
    print(f"QUESTION: {question}")
    print(f"{'='*50}")

    # Ask LLaMA
    print("\n🤖 MODEL 1 - LLaMA 70B:")
    llama_result = ask_llama(question)
    print(f"Answer: {llama_result['answer']}")
    print(f"⏱️ Time: {llama_result['time']} seconds")
    print(f"🔢 Tokens: {llama_result['tokens']}")

    # Ask Mixtral
    print("\n🤖 MODEL 2 - Mixtral:")
    mixtral_result = ask_mixtral(question)
    print(f"Answer: {mixtral_result['answer']}")
    print(f"⏱️ Time: {mixtral_result['time']} seconds")
    print(f"🔢 Tokens: {mixtral_result['tokens']}")

    # Compare
    print(f"\n{'='*50}")
    if llama_result['time'] < mixtral_result['time']:
        print("⚡ WINNER: LLaMA is FASTER!")
    else:
        print("⚡ WINNER: Mixtral is FASTER!")

    # Token comparison
    if llama_result['tokens'] < mixtral_result['tokens']:
        print("💰 EFFICIENT: LLaMA used LESS tokens!")
    else:
        print("💰 EFFICIENT: Mixtral used LESS tokens!")

# =====================
# TEST IT!
# =====================
compare_models("What is Machine Learning?")
compare_models("What is RAG in AI?")
compare_models("Explain Deep Learning simply")