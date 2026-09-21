from langchain_core.documents import Document

from repositories.experience import get_experiences


def get_experience_documents():
    experiences = get_experiences()
    documents = []

    for experience in experiences:
        (
            job_id,
            company,
            job_title,
            job_start,
            job_end,
            role_id,
            role_title,
            role_description,
            responsibility,
        ) = experience

        content = f"""
Company: {company}
Role: {role_title or job_title}
Period: {job_start} - {job_end or "Present"}

Description:
{role_description or ""}

Responsibilities:
{responsibility or ""}
"""

        documents.append(
            Document(
                page_content=content.strip(),
                metadata={
                    "type": "experience",
                    "job_id": job_id,
                    "role_id": role_id,
                    "company": company,
                },
            )
        )

    return documents
