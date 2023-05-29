import os
from functools import lru_cache
from typing import List

from pydantic import BaseSettings, Field


def get_env_file():
    stage = os.environ.get('ENV') or 'dev'
    return f'{stage}.env'


class Settings(BaseSettings):
    DEBUG: bool = False

    APP_NAME: str = "The Endings"
    HTTPS: bool = False
    HOST: str = "localhost"

    SECRET_KEY: str = "06ba4b55244d992e091cb1a6f638bf313a1118812d0dde12a17e7afb02fc1868"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    DB_DATABASE: str = "eshop"
    DB_URL: str = "mongodb://127.0.0.1:27017/eshop?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.9.1"

    ORIGINS: List[str] = Field(
        ["http://localhost:8000", "http://localhost:3000"], env='ORIGINS')
    ALLOWED_HOSTS: List[str] = ["127.0.0.1", "localhost"]

    GOOGLE_CLIENT_ID: str = "91652870902-64it1v2a7okerm7jrlcnojtlt3f8hipo.apps.googleusercontent.com"
    GOOGLE_CLIENT_SECRET: str = "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"
    GOOGLE_CALLBACK_URL: str = "localhost:3000/"

    GITHUB_CLIENT_ID: str = None
    GITHUB_CLIENT_SECRET: str = None
    GITHUB_CALLBACK_URL: str = None

    KAKAO_CLIENT_ID: str = None
    KAKAO_CLIENT_SECRET: str = None
    KAKAO_CALLBACK_URL: str = None

    NAVER_CLIENT_ID: str = None
    NAVER_CLIENT_SECRET: str = None
    NAVER_CALLBACK_URL: str = None

    class Config:
        env_file = get_env_file()

    @property
    def URL(self) -> str:
        protocol = 'https' if self.HTTPS else 'http'
        return f'{protocol}://{self.HOST}'


Configs = Settings()

print('Configs:\n', Configs)


@lru_cache()
def get_settings():
    return Configs
