from pydantic import (
    PostgresDsn,
    computed_field,
)
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    APP_NAME: str = "Cutlet"
    APP_DESCRIPTION: str = "Cutlet: Create short URLs"
    APP_VERSION: str = "0.1.0"
    APP_API_VERSION: str = "v1"
    APP_SHORT_CODE_LENGTH: int = 6
    APP_DEFAULT_REDIRECT_TYPE: int = (
        302  # Temporary redirect which doesn't get cached by browsers
    )
    CONTACT_NAME: str = "Sage"
    CONTACT_EMAIL: str = "your-email@gmail.com"
    LICENSE_NAME: str = "Apache-2.0 License"


class PostgresSettings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB_NAME: str

    @computed_field
    @property
    def DATABASE_URL(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postresql+psycopg2",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB_NAME,
        )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        env_file_encoding="utf-8",
        extra="ignore",
    )
    app: AppSettings = AppSettings()
    postgres: PostgresSettings = PostgresSettings()


settings = Settings()
