from typing import List, Optional


from fastapi import APIRouter, Depends


from app.crud.subsectors import (
    get_sub_sectors, search_metric, get_metric_for_sub_sector)
from app.db.mongodb import AsyncIOMotorClient, get_database
from app.schemas.subsectors import SubSectorSchema


router = APIRouter()


@router.get("/{sector_id}/sub-sectors", response_description="Sub sectors for specified sector",
                         response_model=List[SubSectorSchema])
async def get_subsectors(sector_id: str, db: AsyncIOMotorClient = Depends(get_database)):
    return await get_sub_sectors(db, sector_id)


@router.get("/{sector_id}/{sub_sector_id}", response_description="Metrics retrieved for sub sector",
            response_model=SubSectorSchema)
async def get_metric_for_subsector(sector_id: str, sub_sector_id: str, db: AsyncIOMotorClient = Depends(get_database)):
    return await get_metric_for_sub_sector(db, sector_id, sub_sector_id)
   

@router.get("/search", response_model=List[SubSectorSchema])
async def search_metric_data(q: Optional[str] = None, db: AsyncIOMotorClient = Depends(get_database)):
    return await search_metric(db, q)
