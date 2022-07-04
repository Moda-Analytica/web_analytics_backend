from fastapi import HTTPException

from ..db.mongodb import AsyncIOMotorClient
from ..config import get_settings


settings = get_settings()


DATABASE_NAME = settings.database_name


async def get_sub_sectors(conn:AsyncIOMotorClient, sector_id: str):
    query = {"sector": sector_id}
    stats = await conn[DATABASE_NAME]["stats_data"].find(query).to_list(None)
    if stats is not None and stats != []:
        return stats
    raise HTTPException(
        status_code=404, detail=f"Sub sectors not found for {sector_id} sector.")
