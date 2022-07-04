import json

from pywebpush import webpush, WebPushException


from ..config import get_settings




settings = get_settings()


def trigger_push_notification(push_subscription, title, body):
    try:
        response = webpush(
            subscription_info=json.loads(
                push_subscription.get('subscription_json')),
            data=json.dumps({"title": title, "body": body}),
            vapid_private_key=settings.vapid_private_key,
            vapid_claims={
                "sub": "mailto:{}".format(settings.vapid_claim_email)
            }
        )
        return response.ok
    except WebPushException as ex:
        if ex.response and ex.response.json():
            extra = ex.response.json()
            print("Remote service replied with a {}:{}, {}",
                  extra.code,
                  extra.errno,
                  extra.message)
        return False


def trigger_push_notifications_for_subscriptions(subscriptions, title, body):
    return [trigger_push_notification(subscription, title, body) for subscription in subscriptions]
