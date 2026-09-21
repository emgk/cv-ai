from pgvector.psycopg import register_vector
from psycopg.types.json import Jsonb

from database import get_connection
from services.contributions import get_contribution_documents
from services.developer import get_developer_document
from services.educations import get_education_documents
from services.embeddings import embeddings

# from services.skills import get_skill_documents
from services.experience import get_experience_documents


def index_documents():
    documents = []

    documents.extend(get_experience_documents())
    documents.extend(get_developer_document())
    documents.extend(get_contribution_documents())
    documents.extend(get_education_documents())

    with get_connection() as conn:
        register_vector(conn)

        with conn.cursor() as cursor:
            for document in documents:
                vector = embeddings.embed_query(document.page_content)

                cursor.execute(
                    """
                    INSERT INTO rag_documents
                    (content,metadata,embedding)
                    VALUES(%s,%s,%s)
                    """,
                    (
                        document.page_content,
                        Jsonb(document.metadata),
                        vector,
                    ),
                )

        conn.commit()

    return len(documents)
