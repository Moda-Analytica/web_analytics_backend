from fastapi import APIRouter, Request, Depends

from ....crud.push_notification import create_subscription, push_notifications_to_users

from ....db.mongodb import AsyncIOMotorClient, get_database
from ....schemas.push_notification import PushNotificationSchema


router = APIRouter()


@router.post("/push-notifications/subscribe")
async def create_push_notification_subscription(request: Request, db: AsyncIOMotorClient = Depends(get_database)):
    return await create_subscription(db, request)


@router.post("/trigger-push-notifications")
def push_notifications(notification: PushNotificationSchema):
    return push_notifications_to_users(notification)
