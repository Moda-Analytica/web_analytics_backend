from fastapi import HTTPException

from app.db.mongodb import AsyncIOMotorClient
from app.config import get_settings


settings = get_settings()


DATABASE_NAME = settings.database_name


async def get_all_sectors(conn: AsyncIOMotorClient):
    sectors = await conn[DATABASE_NAME]["stats_sector"].find().to_list(None)
    if sectors is not None and sectors != []:
        return sectors
    raise HTTPException(status_code=404, detail=f"An error occurred.")


async def total_stats(conn: AsyncIOMotorClient):

    info = await conn[DATABASE_NAME]["run_instance"].find().limit(1).sort([('$natural', -1)]).to_list(None)

    if info and info != []:
        return info[0]
    raise HTTPException(status_code=404, detail=f"An error occurred.")
