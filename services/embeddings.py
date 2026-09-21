import os

from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model=os.getenv("EMBEDDING_MODEL_ID"))
