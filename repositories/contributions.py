from database import get_connection

def get_contributions():
    query = f"""
        SELECT 
            id,
            date,
            title,
            description,
            url,
            demo_url,
            skills
        FROM contributions
        ORDER BY date DESC
    """

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()