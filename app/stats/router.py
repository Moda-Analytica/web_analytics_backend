from typing import List

from fastapi import APIRouter, HTTPException
import motor.motor_asyncio


from app.config import get_settings


from .schemas import (SubSectorSchema, response_model, error_response_model)


settings = get_settings()
client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)
db = client.stats
collection = db["stats_data"]

router = APIRouter()


@router.get("/{sector_id}/sub-sectors", response_description="Sub sectors for specified sector",
            response_model=List[SubSectorSchema])
async def get_sub_sectors(sector_id: str):
    query = {"sector": sector_id}
    stats = await collection.find(query).to_list(None)
    if stats is not None and stats != []:
        return stats
    raise HTTPException(status_code=404, detail=f"Sub sectors not found for {sector_id} sector.")


@router.get("/{sub_sector_id}", response_description="Metrics retrieved for sub sector", response_model=SubSectorSchema)
async def get_metric_for_sub_sector(sub_sector_id: str):
    if (stat := await collection.find_one({"_id": sub_sector_id})) is not None:
        return stat
    raise HTTPException(status_code=404, detail=f"Stat {sub_sector_id} was not found")
