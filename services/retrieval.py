from database import get_connection
from services.embeddings import embeddings
from pgvector.psycopg import register_vector

def search_documents(query:str, limit:int =5):
    query_embedding = embeddings.embed_query(query)

    with get_connection() as conn:
        register_vector(conn)

        with conn.cursor() as cursor:
            cursor.execute(
                """
                    SELECT
                        content,
                        metadata,
                        embedding <=> %s::vector AS distance
                    FROM rag_documents
                    ORDER BY embedding <=> %s::vector
                    LIMIT %s;
                """, 
                (
                    query_embedding,
                    query_embedding,
                    limit
                )
            )

            return cursor.fetchall()