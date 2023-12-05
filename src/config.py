from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    service_name: str = "Sentiment Analizer"
    k_revision: str = "Local"
    log_level: str = "DEBUG"
    # openai_key: str
    # model: GPTModel = GPTModel.gpt_3_5_turbo

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()