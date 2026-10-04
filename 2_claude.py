from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()
model=ChatAnthropic("claude-3-5-sonnet-v1")

result=model.invoke("Write a poem about a lonely computer")
print(result.content)
