# Personalized AI Chat with Govind

## AI Technical Stack

For the AI part, I’m using Python and FastAPI for the backend, with LangChain to handle the RAG flow. OpenAI is used for generating embeddings and responses, while PostgreSQL with pgvector handles the vector search.

### Flow

```text
PostgreSQL → Documents → Embeddings → pgvector
                                      ↓
User query → Similarity search → Context → LLM → Response
```


#### Demo

<img width="1640" height="1180" alt="ai-demo" src="https://github.com/user-attachments/assets/3013b254-80c2-4b8b-8a00-379fb0945fa8" />

