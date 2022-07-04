from fastapi import HTTPException

from ..db.mongodb import AsyncIOMotorClient
from ..config import get_settings


settings = get_settings()


DATABASE_NAME = settings.database_name


async def get_all_sectors(conn: AsyncIOMotorClient):
    sectors = await conn[DATABASE_NAME]["stats_sector"].find().to_list(None)
    if sectors is not None and sectors != []:
        return sectors
    raise HTTPException(status_code=404, detail=f"An error occurred.")
