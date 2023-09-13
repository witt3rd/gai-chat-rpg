"""
This module contains the `Settings` dataclass and `get_config` function for
managing configuration settings.

The `Settings` dataclass contains attributes for various settings, such as
the OpenAI API key, datetime format, session directory, transcript directory,
prompts file, and MongoDB URL.

The `get_config` function returns an instance of the `Settings` dataclass with
values populated from environment variables or default values.

Example usage:

    >>> from config import get_config
    >>> config = get_config()
    >>> print(config.openai_api_key)
    'my_secret_api_key'
"""
from dataclasses import dataclass
from functools import lru_cache
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    """
    A dataclass for managing configuration settings.
    """

    openai_api_key: str
    prompts_dir: str
    mongodb_url: str
    mongodb_db: str
    host: str
    port: int


@lru_cache()
def get_config() -> Settings:
    """
    Returns an instance of the `Settings` dataclass with values populated
    from environment variables or default values.

    Returns:
        Settings: An instance of the `Settings` dataclass.

    Example usage:

        >>> from config import get_config
        >>> config = get_config()
        >>> print(config.OPENAI_API_KEY)
        'my_secret_api_key'
    """
    return Settings(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        prompts_dir=os.getenv("PROMPTS_DIR", "./prompts"),
        mongodb_url=os.getenv("MONGODB_URL", "mongodb://localhost:27017/"),
        mongodb_db=os.getenv("MONGODB_DB", "chat-rpg"),
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "8080")),
    )
