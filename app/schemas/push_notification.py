from pydantic import BaseModel


class PushNotificationSchema(BaseModel):
    title: str
    body: str
