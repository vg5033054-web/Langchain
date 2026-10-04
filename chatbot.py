import os
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

# Get Hugging Face API token from environment
hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

# 1. Initialize the HuggingFaceEndpoint LLM
# Using Qwen/Qwen2.5-72B-Instruct (hosted on free HF Inference API)
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=hf_token,
    max_new_tokens=150,
    temperature=0.7,
)

# 2. Wrap it with ChatHuggingFace
model = ChatHuggingFace(llm=llm)

# 3. Initialize conversation history
chat_history = [
    SystemMessage(content="You are a helpful and polite AI assistant.")
]

print("=" * 55)
print("Hugging Face Chatbot Initialized (Qwen/Qwen2.5-72B)!")
print("Type 'exit' or 'quit' to end the chat.")
print("=" * 55)

while True:
    user_input = input("\nYou: ").strip()
    if not user_input:
        continue
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    # Add user message to history
    chat_history.append(HumanMessage(content=user_input))

    # Invoke model with full history
    response = model.invoke(chat_history)

    # Add AI response to history
    chat_history.append(AIMessage(content=response.content))

    print(f"\nAI: {response.content}")