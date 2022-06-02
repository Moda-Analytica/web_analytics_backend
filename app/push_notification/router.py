from fastapi import APIRouter, Request
import motor.motor_asyncio


from app.config import get_settings
from .webpush_handler import trigger_push_notifications_for_subscriptions

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
async def push_notifications(request: Request):
    data = await request.json()
    subscriptions = await push_notification_collection.find().to_list(None)
    results = trigger_push_notifications_for_subscriptions(subscriptions, data.get('title'), data.get('body'))

    return {"status": "success", "result": results}

