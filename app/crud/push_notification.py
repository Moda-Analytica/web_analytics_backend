from fastapi import Request

from app.config import get_settings
from app.celery_worker import celery_push_notifications
from app.db.mongodb import AsyncIOMotorClient
from app.schemas.push_notification import PushNotificationSchema



settings = get_settings()


DATABASE_NAME = settings.database_name

PUSH_NOTIFICATION_COLLECTION = "stats_push_notification"

async def create_subscription(conn: AsyncIOMotorClient, request: Request):
    data = await request.json()
    subscription = await conn[DATABASE_NAME][PUSH_NOTIFICATION_COLLECTION].find_one({"subscription_json": data['subscription_json']})
    if subscription is None:
        new_subscription = await conn[DATABASE_NAME][PUSH_NOTIFICATION_COLLECTION].insert_one({"subscription_json": data['subscription_json']})
    return {"success": "Subscription successful."}


def push_notifications_to_users(notification: PushNotificationSchema):
    celery_push_notifications.delay(notification.title, notification.body)
    return {"status": "in progress"}
