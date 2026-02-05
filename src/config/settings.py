from pathlib import Path

from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).resolve().parent.parent.parent


class PostgresSettings(BaseSettings):
    db: str
    host: str
    port: int
    user: str
    password: SecretStr

    @property
    def data_source_name(self) -> str:
        return (
            f"postgresql+asyncpg://{self.user}:{self.password.get_secret_value()}"
            f"@{self.host}:{self.port}/{self.db}"
        )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_prefix="",
        env_nested_delimiter="_",
    )

    postgres: PostgresSettings = Field(default_factory=PostgresSettings)


settings = Settings()
