from langchain_openai import OpenAIEmbeddings

import os

embeddings = OpenAIEmbeddings(
    model=os.getenv('EMBEDDING_MODEL_ID')
)