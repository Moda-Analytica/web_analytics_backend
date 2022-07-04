from typing import List

from fastapi import APIRouter, Depends


from ....crud.sectors import get_all_sectors, total_stats
from ....db.mongodb import AsyncIOMotorClient, get_database
from ....schemas import sectors, runinstance


router = APIRouter()


@router.get("/", response_description="All sectors.",  response_model=List[sectors.SectorSchema])
async def get_sectors(db: AsyncIOMotorClient = Depends(get_database)):
    return await get_all_sectors(db)

# response_model=runinstance.RunInstanceSchema
@router.get("/total_stats")
async def total_stats_data(db:  AsyncIOMotorClient = Depends(get_database)):
    return await total_stats(db)
