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
    campaign as campaign_models,
    message as message_models,
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
            campaign_models.CampaignDoc,
            message_models.MessageDoc,
            user_models.UserDoc,
        ],
    )

    # check for the existence of the "System" user
    gpt4_user = await user_models.UserDoc.find_one({"username": "System"})
    if gpt4_user is None:
        gpt4_user = user_models.UserDoc(
            username="System",
            name="System",
            email="system@chat-rpg.com",
            password="password",
            avatar="hal.png",
            is_system=True,
        )
        await gpt4_user.insert()

    # check for the existence of the "GPT4" user
    gpt4_user = await user_models.UserDoc.find_one({"username": "GPT4"})
    if gpt4_user is None:
        gpt4_user = user_models.UserDoc(
            username="GPT4",
            name="OpenAI GPT-4",
            email="gpt4@openai.com",
            password="password",
            avatar="openai.png",
            is_system=True,
        )
        await gpt4_user.insert()


async def drop_db() -> None:
    """
    Drops the database.
    """
    client = await _get_client()
    database_name = get_config().mongodb_db
    await client.drop_database(database_name)
