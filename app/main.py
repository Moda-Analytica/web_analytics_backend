from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import motor.motor_asyncio


from app.config import get_settings
from app.stats.router import router as SectorRouter

app = FastAPI()

origins = [
    "https://moda-analytica.netlify.app",
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(SectorRouter, tags=["Sector"], prefix="/sector")
settings = get_settings()
client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)
db = client.stats


@app.get("/")
def hello_world():
    return {"hello": "world"}


