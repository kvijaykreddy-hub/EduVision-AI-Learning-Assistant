from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    """Application configuration."""

    MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "gemini")

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")

    HUGGINGFACEHUB_API_TOKEN = os.getenv(
        "HUGGINGFACEHUB_API_TOKEN",
        "",
    )
    GEMINI_MODEL = os.getenv(
        "GEMINI_MODEL",
        "gemini-3.5-flash",
    )