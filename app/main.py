from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware

from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from .config import get_settings
from .push_notification.router import router as NotificationRouter
from .stats.router import router as SectorRouter

from .schemas import ContactSchema as Contact

app = FastAPI()
settings = get_settings()

origins = [
    "https://www.statsmetrics.ng",
    "https://moda-analytica.netlify.app",
    "http://localhost:3000",
    "http://127.0.0.1:3000",


]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

conf = ConnectionConfig(
    MAIL_USERNAME=settings.mail_username,
    MAIL_PASSWORD=settings.mail_password,
    MAIL_FROM=settings.mail_from,
    MAIL_PORT=465,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_FROM_NAME=settings.mail_username,
    MAIL_TLS=False,
    MAIL_SSL=True,
    USE_CREDENTIALS=True,
    MAIL_DEBUG=1
)

app.include_router(SectorRouter, tags=["Sector"], prefix="/sector")
app.include_router(NotificationRouter, tags=["Push Notification"], prefix="")


@app.get("/")
def hello_world():
    return {"hello": "world"}


@app.post("/contact-us")
def contact_form(contact: Contact, background_tasks: BackgroundTasks):
    message = MessageSchema(
        subject=contact.subject,
        # List of recipients
        recipients=['info@modanalytica.com'],
        body=contact.message,
        subtype="html"
    )
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)
    return {"message": "Successfully contact the modanalytical team. We'll be with you shortly.", }
