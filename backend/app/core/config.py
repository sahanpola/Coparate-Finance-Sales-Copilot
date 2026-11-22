from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    """Application settings."""

    app_name: str = "Corporate Finance & Sales Intelligence Copilo "
    app_version: str = "0.1.0"
    environment: str = "development"
    api_prefix: str = "/api/v1"


settings = Settings()

