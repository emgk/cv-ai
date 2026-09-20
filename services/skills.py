from langchain_core.documents import Document

from database import get_connection

def get_skill_documents():
    query = """
        SELECT 
            id,
            name,
            url
        FROM skills
        ORDER BY name;
    """

    documents = []

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)

            for skill_id, name, url in cursor.fetchall():

                documents.append(
                    Document(
                        page_content=f"Skill: {name}",
                        metadata={
                            "type":"skill",
                            "skill_id":skill_id,
                            "name":name,
                            "url":url,
                        },
                    )
                )
    return documents