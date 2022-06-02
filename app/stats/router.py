from typing import List, Optional

from fastapi import APIRouter, HTTPException
import motor.motor_asyncio


from app.config import get_settings


from .schemas import (SectorSchema,SubSectorSchema, response_model, error_response_model)


settings = get_settings()
client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)
db = client.stats
sector_collection = db["stats_sector"]
sub_sector_collection = db["stats_data"]


router = APIRouter()


@router.get("", response_description="All sectors.",  response_model=List[SectorSchema])
async def get_sectors():
    sectors = await sector_collection.find().to_list(None)
    if sectors is not None and sectors != []:
        return sectors
    raise HTTPException(status_code=404, detail=f"An error occurred.")


@router.get("/{sector_id}/sub-sectors", response_description="Sub sectors for specified sector",
            response_model=List[SubSectorSchema])
async def get_sub_sectors(sector_id: str):
    query = {"sector": sector_id}
    stats = await sub_sector_collection.find(query).to_list(None)
    if stats is not None and stats != []:
        return stats
    raise HTTPException(status_code=404, detail=f"Sub sectors not found for {sector_id} sector.")


@router.get("/{sector_id}/{sub_sector_id}", response_description="Metrics retrieved for sub sector",
            response_model=SubSectorSchema)
async def get_metric_for_sub_sector(sector_id:str, sub_sector_id: str):
    if (stat := await sub_sector_collection.find_one({"_id": sub_sector_id, "sector": sector_id})) is not None:
        return stat
    raise HTTPException(status_code=404, detail=f"Stat {sub_sector_id} was not found under {sector_id}")


@router.get("/search", response_model=List[SubSectorSchema])
async def search_metric(q: Optional[str] = None):
    query = {"$search": q}
    stats = await sub_sector_collection.find({"$text": query}).to_list(None)
    if stats is not None and stats != []:
        return stats
    elif stats == []:
        return []

