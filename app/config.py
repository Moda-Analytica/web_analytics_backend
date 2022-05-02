from functools import lru_cache


from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    mongodb_url: str = Field(..., env="MONGODB_URL")

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()


