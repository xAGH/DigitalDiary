from pydantic import BaseSettings
from typing import Type


class Settings(BaseSettings):
    API_VERSION: str
    SECRET_KEY: str
    SQLALCHEMY_DATABASE_URI: str
    ALLOWED_CORS_LIST: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 1  # == 1 day
    TOKEN_TYPE: str = "Bearer"

    @property
    def ALLOWED_CORS(self) -> list[str]:
        return self.ALLOWED_CORS_LIST.split(';')

    class Config:
        env_file: str = "./.env"
        env_file_encoding: str = "utf-8"


settings: Type[Settings] = Settings()  # type: ignore
