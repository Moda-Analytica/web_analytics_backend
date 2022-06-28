from functools import lru_cache


from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    mongodb_url: str = Field(..., env="MONGODB_URL")
    vapid_public_key: str = Field(..., env="VAPID_PUBLIC_KEY")
    vapid_private_key: str = Field(..., env="VAPID_PRIVATE_KEY")
    vapid_claim_email: str = Field(..., env="VAPID_CLAIM_EMAIL")
    celery_broker_url: str = Field(env="REDIS_URL")
    # mail_username: str = Field(env="MAIL_USERNAME")
    # mail_password: str = Field(env="MAIL_PASSWORD")
    # mail_from: str = Field(env="MAIL_FROM")
    # mail_port: int = Field(env="MAIL_PORT")
    # mail_server: str = Field(env="MAIL_SERVER")


    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()


