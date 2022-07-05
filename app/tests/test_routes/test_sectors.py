import pytest

from fastapi import Depends


from app.crud import sectors
from app.db.mongodb import AsyncIOMotorClient, get_database


def test_get_all_sectors(test_app, monkeypatch):
    test_data = [
        {
            "_id": 1,
            "name": "education",
            "description": "Test description"
        },
        {
            "_id": 2,
            "name": "politics",
            "description": "Test description 2"
        }
    ]

    # async def mock_get_sectors(db: AsyncIOMotorClient = Depends(get_database)):
    #     return test_data
    
    # monkeypatch.setattr(sectors, "get_all_sectors", mock_get_sectors)
    response = test_app.get("/sector")
    assert response.status_code == 200
    # assert response.json() == test_data

