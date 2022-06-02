from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import motor.motor_asyncio

from app.config import get_settings
from app.stats.router import router as SectorRouter
from app.push_notification.router import router as NotificationRouter

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
app.include_router(NotificationRouter, tags=["Push Notification"], prefix="")


@app.get("/")
def hello_world():
    return {"hello": "world"}

















