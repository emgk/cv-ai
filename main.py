from fastapi import FastAPI
from database import get_connection
from repositories.experience import get_experiences
from services.experience import get_experience_documents
from services.embeddings import embeddings
from services.retrieval import search_documents
from services.rag import ask
from services.skills import get_skill_documents
from services.indexing import index_documents
from services.developer import get_developer_document
from services.contributions import get_contribution_documents
from services.educations import get_education_documents
# from psycopg.types.json import Jsonb
# from pgvector.psycopg import register_vector

app = FastAPI()

@app.get('/')
def root():
    return {"message": "Ask me ddd is rdunning"}

@app.get("/experiences")
def test_db():
    return get_experiences()

@app.get("/get-contributions")
def contribution_document():
    documents = get_contribution_documents();

    return [
        {
            "content": document.page_content,
            "metadata": document.metadata
        }
        for document in documents
    ]
 
@app.get("/developer-document")
def developer_document():
    document = get_developer_document();

    return [
        {
            "content": document.page_content,
            "metadata": document.metadata
        }
    ]

@app.get("/experience-documents")
def experience_documents():
    documents = get_experience_documents()

    return [
        {
            "content": document.page_content,
            "metadata": document.metadata,
        }
        for document in documents
    ]


@app.get('/test-embededding')
def test_embedding():
    vector = embeddings.embed_query(
        'what experience does Govind have with React?'
    )

    return {
        "dimensions": len(vector),
        "first_avalues": vector[:5],
    }

@app.get("/index")
def index():
    count = index_documents()
    return {
        "message": f"Indexed {count} documents"
    }

@app.get("/search")
def search(query: str, limit: int = 5):
    results = search_documents(query,limit)

    return [
        {
            "content":content,
            "metadata":metadata,
            "distance": float(distance),
        }
        for content, metadata, distance in results
    ]

@app.get("/ask")
def ask_question(query:str):
    answer = ask(query)

    return {
        "question": query,
        "answer": answer
    }


@app.get("/skill-documents")
def skill_documents():
    documents = get_skill_documents()

    return [
        {
            "content": document.page_content,
            "metadata": document.metadata
        }
        for document in documents
    ]

@app.get("/get-educations")
def get_educations():
    documents = get_education_documents()

    return [
        {
            "content": document.page_content,
            "metadata": document.metadata
        }
        for document in documents
    ]