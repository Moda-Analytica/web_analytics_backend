from motor.motor_asyncio import AsyncIOMotorClient

from .mongodb import db
from ..config import get_settings

settings = get_settings()


async def connect_to_mongo():
    db.client = AsyncIOMotorClient(str(settings.mongodb_url))


async def close_mongo_connection():
    db.client.close()
