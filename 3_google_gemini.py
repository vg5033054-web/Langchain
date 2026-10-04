from langchain_google_genai import ChatGoogleGemini, ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-1.5-turbo",temperature='0.5',max_tokens=10)

result=model.invoke("where is the capital of india")
print(result.content)