import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

# 1. Initialize the HuggingFaceEndpoint LLM
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation",
)

# 2. Wrap it with ChatHuggingFace
model = ChatHuggingFace(llm=llm)

# 3. Invoke the model
result = model.invoke("what is the capital of India?")
print(result.content)
