from fastapi import FastAPI
import motor.motor_asyncio


from app.config import get_settings
from app.stats.router import router as SectorRouter

app = FastAPI()
app.include_router(SectorRouter, tags=["Sector"], prefix="/sector")
settings = get_settings()
client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)
db = client.stats


@app.get("/")
def hello_world():
    return {"hello": "world"}


