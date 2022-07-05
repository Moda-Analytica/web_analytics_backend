import pytest

from fastapi import Depends


from app.db.mongodb import AsyncIOMotorClient, get_database


def test_get_subsectors(test_client, monkeypatch):
    test_subsectors_data = [
        {
            "_id": "education_1",
            "metric": "test metric",
            "description": "test desc",
            "sector": "education",
            "value_type": "actual",
            "reference": "test.com",
            "report": "https://test.com"
        },
        {
            "_id": "education_1",
            "metric": "test metric 2",
            "description": "test desc 2",
            "sector": "education",
            "value_type": "actual",
            "reference": "test2.com",
            "report": "https://test2.com"
        },
    ]

    async def mock_get_subsectors(db: AsyncIOMotorClient, sector_id):
        return test_subsectors_data

    monkeypatch.setattr(
        "app.api.api_v1.endpoints.subsectors.get_sub_sectors", mock_get_subsectors)

    response = test_client.get("/sector/education/sub-sectors")
    assert response.status_code == 200
    assert response.json() == test_subsectors_data


def test_metric_for_subsector(test_client, monkeypatch):
    test_metric_data = {
        "_id": "education_1",
        "metric": "test metric",
        "description": "test desc",
        "sector": "education",
        "value_type": "actual",
        "reference": "test.com",
        "report": "https://test.com"
    }

    async def mock_get_metric(db: AsyncIOMotorClient, sector_id, sub_sector_id):
        if sector_id == test_metric_data.get("sector") and sub_sector_id == test_metric_data.get("_id"):
            return test_metric_data

    monkeypatch.setattr(
        "app.api.api_v1.endpoints.subsectors.get_metric_for_sub_sector", mock_get_metric)

    response = test_client.get("/sector/education/education_1")
    assert response.status_code == 200
    assert response.json() == test_metric_data
