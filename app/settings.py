from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="allow")

    POSTGRES_USER: str = Field(default="postgres")
    POSTGRES_PASSWORD: str = Field(default="postgres")
    POSTGRES_DB: str = Field(default="db")
    HOST_DB: str = Field(default="localhost")
    PORT_DB: int = Field(default=5432)

    @property
    def dsn_url(self) -> str:
        return (
            f"postgresql://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@{self.HOST_DB}:"
            f"{self.PORT_DB}/{self.POSTGRES_DB}"
        )


conf = Config()
