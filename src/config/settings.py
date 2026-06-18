from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration settings for the application."""

    OPENAI_API_KEY: str = Field(validation_alias=("OPENAI_API_KEY"))
    GOOGLE_API_KEY: str = Field(validation_alias=("GOOGLE_API_KEY"))
    LLM_PROVIDER: str = Field(default="gemini")
    MODEL_DEFAULT_OPENAI: str = Field(default="gpt-4o-mini")
    MODEL_DEFAULT_GEMINI: str = Field(default="gemini-1.5-pro")
    TEMPERATURE_DEFAULT: float = Field(default=0.5)

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8"
    )


settings = Settings() # pyright: ignore[reportCallIssue]
