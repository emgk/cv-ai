from langchain_core.documents import Document
from database import get_connection

def get_developer_document():
    query = """
    SELECT 
        id,
        name,
        about,
        skills
    FROM developer_info
    LIMIT 1;
    """

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchone()

    if not row:
        return None

    developer_id, name, about, skills = row

    content = f"""
Name: {name}

Profile:
{skills}

About:
{about}
"""

    return [Document(
        page_content=content.strip(),
        metadata={
            "type":"developer",
            "developer_id":developer_id,
        }
    )]