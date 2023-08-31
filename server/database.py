"""
Database initialization and management.
"""
# # System # #

# # Packages # #
from beanie import init_beanie
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

# # Project # #
from server.config import get_config
from server.models import (
    user as user_models,
)

###


async def _get_client() -> AsyncIOMotorClient:
    """
    Returns a new MongoDB client instance.

    Returns:
        AsyncIOMotorClient: A new MongoDB client instance.
    """
    host = get_config().mongodb_url
    logger.info(f"Connecting to MongoDB at {host}...")
    client = AsyncIOMotorClient(host)

    logger.info(f"Mongo version: {client.version}")

    return client


async def init_db() -> None:
    """
    Initializes the database connection and registers the document models.
    """
    client = await _get_client()
    database_name = get_config().mongodb_db
    logger.info(f"Initializing Beanie for database {database_name}...")
    await init_beanie(
        database=AsyncIOMotorDatabase(client, database_name),
        document_models=[
            user_models.UserDoc,
        ],
    )


async def drop_db() -> None:
    """
    Drops the database.
    """
    client = await _get_client()
    database_name = get_config().mongodb_db
    await client.drop_database(database_name)
