import pymongo
import motor.motor_asyncio
from bson.objectid import ObjectId

from app.config import get_settings


settings = get_settings()
client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)
# client = pymongo.MongoClient(settings.mongodb_url)
# print(client.)
db = client.stats

stats_collection = db.get_collection("stats_data")


def stats_helper(stats) -> dict:
    return {
        "id": str(stats["_id"]),
        "metric": stats["metric"],
        "description": stats["description"],
        "sector": stats["sector"],
        "value_type": stats["value_type"],
        "reference": stats["reference"]
    }


async def retrieve_metrics():
    metrics = []
    async for stat in stats_collection.find():
        metrics.append(stats_helper(stat))
    return metrics





