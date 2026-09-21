from database import get_connection


def get_educations():
    query = """
        SELECT
            e.id AS id,
            e.title AS university_title,
            e.start AS start_date,
            e.end AS end_date,
            d.education_id AS education_id,
            d.title AS degree_title,
            d.description AS degree_description
        FROM education e
        LEFT JOIN education_degrees d ON d.education_id = e.id
    """

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
