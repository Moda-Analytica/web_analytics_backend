import pytest 

from fastapi import Depends

from app.db.mongodb import AsyncIOMotorClient, get_database


def test_get_infographics(test_client, monkeypatch):
    test_infographic_data = [
        {
            "sector": "education",
            "title": "test title",
            "description": "info desc.",
            "report": "https://www.zzz.com"
        },

        {
            "sector": "politics",
            "title": "test title",
            "description": "ggg desc.",
            "report": "https://www.ggg.com"
        },
    ]

    async def mock_get_all_infographics(db: AsyncIOMotorClient = Depends(get_database)):
        print("Came here, Moyosore")
        return test_infographic_data

    monkeypatch.setattr(
        "app.api.api_v1.endpoints.infographics.get_all_infographics", mock_get_all_infographics)

    response = test_client.get("/sector/infographics")
    assert response.status_code == 200
    assert response.json() == test_infographic_data
