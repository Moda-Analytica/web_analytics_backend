from fastapi import HTTPException

from app.db.mongodb import AsyncIOMotorClient
from app.config import get_settings


settings = get_settings()



DATABASE_NAME = settings.database_name


async def get_all_infographics(conn: AsyncIOMotorClient):
        
    infographics = await conn[DATABASE_NAME]["stats_infographics"].find().to_list(None)

    if infographics is not None and infographics != []:
        return infographics

    raise HTTPException(status_code=404, detail=f"An error occurred.")
