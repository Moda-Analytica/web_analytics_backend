from fastapi import APIRouter, Request
import motor.motor_asyncio


from app.config import get_settings



from .schemas import PushNotificationSchema 
from .celery_worker import celery_push_notifications



settings = get_settings()

client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)
db = client.stats
push_notification_collection = db["stats_push_notification"]


router = APIRouter()


@router.post("/push-notifications/subscribe")
async def create_push_notifications(request: Request):
    data = await request.json()
    subscription = await push_notification_collection.find_one({"subscription_json": data['subscription_json']})
    if subscription is None:
        new_subscription = await push_notification_collection.insert_one({"subscription_json": data['subscription_json']})
    return {"success": "Subscription successful."}


@router.post("/trigger-push-notifications")
def push_notifications(notification: PushNotificationSchema):
    celery_push_notifications.delay(notification.title, notification.body)
    return {"status": "in progress"}

