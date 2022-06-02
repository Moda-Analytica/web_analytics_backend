from functools import lru_cache


from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    mongodb_url: str = Field(..., env="MONGODB_URL")
    vapid_public_key: str = Field(..., env="VAPID_PUBLIC_KEY")
    vapid_private_key: str = Field(..., env="VAPID_PRIVATE_KEY")
    vapid_claim_email: str = Field(..., env="VAPID_CLAIM_EMAIL")

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()


