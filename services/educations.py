from langchain_core.documents import Document
from repositories.educations import get_educations

def get_education_documents():
    educations = get_educations()
    documents = []

    for education in educations:
        (
            id,
            university_title,
            start_date,
            end_date,
            education_id,
            degree_title,
            degree_description,
        ) = education

        print(education)

        content = f"""
University: 
{university_title}

Degree: 
{degree_title}

Degree Description (What did I do?): 
{degree_description}

Period: {start_date} - {end_date}
"""
        documents.append(
            Document(
                page_content=content.strip(),
                metadata={
                    "type":"educations",
                    "university_id": id,
                    "start_date": str(start_date),
                    "end_date": str(end_date),
                    "education_id":education_id,
                    "university": university_title
                }
            )
        )

        print(documents)

    return documents