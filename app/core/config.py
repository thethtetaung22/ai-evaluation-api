from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AI Evaluation API"
    environment: str = "development"
    database_url: str
    redis_url: str

    class Config:
        env_file = ".env"


settings = Settings()
