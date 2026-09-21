from langchain_core.documents import Document

from repositories.contributions import get_contributions


def get_contribution_documents():
    contributions = get_contributions()
    documents = []

    for contribution in contributions:
        (
            contribution_id,
            date,
            title,
            description,
            url,
            demo_url,
            skills,
        ) = contribution

        content = f"""
Project: {title}

Description:
{description}

Period: {date}
"""

        documents.append(
            Document(
                page_content=content.strip(),
                metadata={
                    "type": "contribution",
                    "contribution_id": contribution_id,
                    "date": str(date),
                    "repo_url": url,
                    "preview_url": demo_url,
                    "skills": skills,
                },
            )
        )

    return documents
