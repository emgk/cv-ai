import os

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model=os.getenv("CHAT_MODEL_ID"),
    temperature=0,
)
 