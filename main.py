import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from repositories.experience import get_experiences
from services.contributions import get_contribution_documents
from services.developer import get_developer_document
from services.educations import get_education_documents
from services.embeddings import embeddings
from services.experience import get_experience_documents
from services.indexing import index_documents
from services.rag import ask
from services.retrieval import search_documents
from services.skills import get_skill_documents

load_dotenv()

cors_origins = [o.strip() for o in os.getenv("CORS_ORIGINS", "").split(",") if o.strip()]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "CV Ask API is running"}


@app.get("/experiences")
def experiences():
    return get_experiences()


@app.get("/get-contributions")
def contribution_documents():
    documents = get_contribution_documents()

    return [{"content": doc.page_content, "metadata": doc.metadata} for doc in documents]


@app.get("/developer-document")
def developer_document():
    documents = get_developer_document()

    return [{"content": doc.page_content, "metadata": doc.metadata} for doc in documents]


@app.get("/experience-documents")
def experience_documents():
    documents = get_experience_documents()

    return [{"content": doc.page_content, "metadata": doc.metadata} for doc in documents]


@app.get("/test-embedding")
def test_embedding():
    vector = embeddings.embed_query("what experience does Govind have with React?")

    return {
        "dimensions": len(vector),
        "sample": vector[:5],
    }


@app.get("/index")
def index():
    count = index_documents()
    return {"message": f"Indexed {count} documents"}


@app.get("/search")
def search(query: str, limit: int = 5):
    results = search_documents(query, limit)

    return [
        {
            "content": content,
            "metadata": metadata,
            "distance": float(distance),
        }
        for content, metadata, distance in results
    ]


@app.get("/ask")
def ask_endpoint(query: str):
    answer = ask(query)

    return {
        "question": query,
        "answer": answer,
    }


@app.get("/skill-documents")
def skill_documents():
    documents = get_skill_documents()

    return [{"content": doc.page_content, "metadata": doc.metadata} for doc in documents]


@app.get("/get-educations")
def get_educations():
    documents = get_education_documents()

    return [{"content": doc.page_content, "metadata": doc.metadata} for doc in documents]
