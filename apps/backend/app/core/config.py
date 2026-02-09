from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_env: str = "local"
    database_url: str = "postgresql+psycopg2://arewegoing:arewegoing@localhost:5432/arewegoing"

    class Config:
        env_file = ".env"

settings = Settings()
