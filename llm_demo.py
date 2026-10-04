from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm=OpenAI(model="gpt-3.5-turbo-instruct")

result=llm("Write a poem about a lonely computer")
print(result)
