from typing import Optional

from fastapi import HTTPException

from ..db.mongodb import AsyncIOMotorClient
from ..config import get_settings


settings = get_settings()


DATABASE_NAME = settings.database_name
STATS_DATA = "stats_data"

async def get_sub_sectors(conn:AsyncIOMotorClient, sector_id: str):
    query = {"sector": sector_id}
    stats = await conn[DATABASE_NAME][STATS_DATA].find(query).to_list(None)
    if stats is not None and stats != []:
        return stats
    raise HTTPException(
        status_code=404, detail=f"Sub sectors not found for {sector_id} sector.")


async def get_metric_for_sub_sector(conn:AsyncIOMotorClient, sector_id: str, sub_sector_id: str):
    if (stat := await conn[DATABASE_NAME][STATS_DATA].find_one({"_id": sub_sector_id, "sector": sector_id})) is not None:
        return stat
    raise HTTPException(
        status_code=404, detail=f"Stat {sub_sector_id} was not found under {sector_id}")


async def search_metric(conn: AsyncIOMotorClient, q: Optional[str] = None):
    query = {"$search": q}
    stats = await conn[DATABASE_NAME][STATS_DATA].find({"$text": query}).to_list(None)
    if stats is not None and stats != []:
        return stats
    elif stats == []:
        return []
