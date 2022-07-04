from fastapi import APIRouter, Request

from .schemas import PushNotificationSchema 
from .celery_worker import celery_push_notifications




router = APIRouter()


@router.post("/push-notifications/subscribe")
async def create_push_notifications(request: Request):
    pass


@router.post("/trigger-push-notifications")
def push_notifications(notification: PushNotificationSchema):
    celery_push_notifications.delay(notification.title, notification.body)
    return {"status": "in progress"}

