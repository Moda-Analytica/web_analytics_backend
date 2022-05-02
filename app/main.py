from fastapi import FastAPI
import motor.motor_asyncio


from app.config import get_settings
from app.stats.router import router as StatsRouter

app = FastAPI()
app.include_router(StatsRouter, tags=["Stats"], prefix="/stats")
settings = get_settings()
client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)
db = client.stats


@app.get("/")
def hello_world():
    return {"hello": "world"}


