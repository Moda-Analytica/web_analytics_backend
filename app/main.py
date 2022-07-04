from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware

from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
import uvicorn


from .config import get_settings
from .db.mongodb_utils import close_mongo_connection, connect_to_mongo
from .api.api_v1.api import router as api_router


settings = get_settings()

origins = [
    "https://www.statsmetrics.ng",
    "https://moda-analytica.netlify.app",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
app = FastAPI(title=settings.project_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

# conf = ConnectionConfig(
#     MAIL_USERNAME=settings.mail_username,
#     MAIL_PASSWORD=settings.mail_password,
#     MAIL_FROM=settings.mail_from,
#     MAIL_PORT=465,
#     MAIL_SERVER='smtp.gmail.com',
#     MAIL_FROM_NAME=settings.mail_username,
#     MAIL_TLS=False,
#     MAIL_SSL=True,
#     USE_CREDENTIALS=True,
#     MAIL_DEBUG=1
# )

app.include_router(api_router, tags=["Sector"], prefix="/sector")


@app.get("/")
def hello_world():
    return {"hello": "world"}


# @app.post("/contact-us")
# def contact_form(contact: Contact, background_tasks: BackgroundTasks):
#     message = MessageSchema(
#         subject=contact.subject,
#         # List of recipients
#         recipients=['info@modanalytica.com'],
#         body=contact.message,
#         subtype="html"
#     )
#     # fm = FastMail(conf)
#     # background_tasks.add_task(fm.send_message, message)
#     return {"message": "Successfully contact the modanalytical team. We'll be with you shortly.", }
