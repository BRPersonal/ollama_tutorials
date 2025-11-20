from pydantic_settings import BaseSettings
from typing import Optional
import os
from pathlib import Path


class Settings(BaseSettings):

    GROQ_API_KEY: str
    USE_LOCAL: bool

    model_config = {"env_file": ".env"}


# Global singleton instance
settings = Settings()

# Ensure the environment variable is set for libraries that might need it
os.environ["GROQ_API_KEY"] = settings.GROQ_API_KEY

if __name__ == "__main__":
    print(f"groq key={settings.GROQ_API_KEY}")
    print(f"use local={settings.USE_LOCAL}")
