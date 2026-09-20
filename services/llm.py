from langchain_openai import ChatOpenAI

import os

llm = ChatOpenAI(
    model=os.getenv('CHAT_MODAL_ID'),
    temperature=0
)