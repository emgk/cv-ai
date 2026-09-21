from database import get_connection


def get_experiences():
    query = """
        SELECT
            j.id AS job_id,
            j.company AS company,
            j.title AS job_title,
            j.start AS job_start,
            j.end AS job_end,
            r.id AS role_id,
            r.title AS role_title,
            r.description AS role_description,
            r.responsibility
        FROM jobs j
        LEFT JOIN roles r ON r.job_id = j.id
        ORDER BY j.start DESC;
    """

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
