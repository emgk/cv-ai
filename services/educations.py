from langchain_core.documents import Document

from repositories.educations import get_educations


def get_education_documents():
    educations = get_educations()
    documents = []

    for education in educations:
        (
            university_id,
            university_title,
            start_date,
            end_date,
            education_id,
            degree_title,
            degree_description,
        ) = education

        content = f"""
University: {university_title}

Degree: {degree_title}

{degree_description}

Period: {start_date} - {end_date}
"""

        documents.append(
            Document(
                page_content=content.strip(),
                metadata={
                    "type": "education",
                    "university_id": university_id,
                    "start_date": str(start_date),
                    "end_date": str(end_date),
                    "education_id": education_id,
                    "university": university_title,
                },
            )
        )

    return documents
