from urllib.request import Request
from fastapi import HTTPException, Request

from ..db.mongodb import AsyncIOMotorClient
from ..config import get_settings
from ..schemas.push_notification import PushNotificationSchema


settings = get_settings()


DATABASE_NAME = settings.database_name

PUSH_NOTIFICATION_COLLECTION = "stats_push_notification"

async def create_subscription(conn: AsyncIOMotorClient, request: Request):
    data = await request.json()
    subscription = await conn[DATABASE_NAME][PUSH_NOTIFICATION_COLLECTION].find_one({"subscription_json": data['subscription_json']})
    if subscription is None:
        new_subscription = await conn[DATABASE_NAME][PUSH_NOTIFICATION_COLLECTION].insert_one({"subscription_json": data['subscription_json']})
    return {"success": "Subscription successful."}


def push_notifications(conn: AsyncIOMotorClient, notification: PushNotificationSchema):
    # celery_push_notifications.delay(notification.title, notification.body)
    return {"status": "in progress"}
