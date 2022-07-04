import pymongo

from celery import Celery
from .config import get_settings
from .core.utils import trigger_push_notifications_for_subscriptions


settings = get_settings()

app = Celery(__name__)
app.conf.broker_url = settings.celery_broker_url
app.conf.result_backend = settings.celery_broker_url


DATABASE_NAME = settings.database_name



@app.task(name='push_notifications')
def celery_push_notifications(title, body):
    my_client = pymongo.MongoClient(settings.mongodb_url, connect=False)
    subscriptions = my_client[DATABASE_NAME]["stats_push_notification"].find()
    results = trigger_push_notifications_for_subscriptions(
        subscriptions, title, body)
    return {"status": results}
