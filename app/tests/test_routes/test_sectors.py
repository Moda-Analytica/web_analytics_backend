import pytest

from fastapi import Depends


from app.crud import sectors
from app.db.mongodb import AsyncIOMotorClient, get_database


def test_get_all_sectors(test_client, monkeypatch):
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

    async def mock_get_sectors(db: AsyncIOMotorClient = Depends(get_database)):
        return test_data

    monkeypatch.setattr(
        "app.api.api_v1.endpoints.sectors.get_all_sectors", mock_get_sectors)

    response = test_client.get("/sector")
    assert response.status_code == 200
    assert response.json() == test_data


def test_total_stats(test_client, monkeypatch):
    test_data = {
        "_id": 10,
        "start_run_time": "2022-07-04 22:29:05.954507",
        "total_metrics": 10,
        "total_sectors": 5,
        "metrics_added": 0,
        "sectors_added": 0
    }

    async def mock_total_stats(db: AsyncIOMotorClient = Depends(get_database)):
        return test_data

    monkeypatch.setattr('app.api.api_v1.endpoints.sectors.total_stats',
                        mock_total_stats)

    response = test_client.get("/sector/total_stats")
    assert response.status_code == 200
    assert response.json() == test_data
