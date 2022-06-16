import pymongo 


import motor.motor_asyncio

from celery import Celery
from ..config import get_settings
from .webpush_handler import trigger_push_notifications_for_subscriptions


settings = get_settings()

app = Celery(__name__)
app.conf.broker_url = settings.celery_broker_url
app.conf.result_backend = settings.celery_result_backend
app.conf.result_serializer = 'json'

client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)
db = client.stats



my_client = pymongo.MongoClient(settings.mongodb_url, connect=False)
my_db = my_client["stats"]
push_notification_collection = my_db["stats_push_notification"]

@app.task(name='push_notifications')
def celery_push_notifications(title, body):
    subscriptions = push_notification_collection.find()

    results = trigger_push_notifications_for_subscriptions(
        subscriptions, title, body)
    return {"status": results}

