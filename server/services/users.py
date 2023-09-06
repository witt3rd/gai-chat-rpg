"""
Authentication service.
"""
# # System # #

# # Packages # #
from loguru import logger

# # Project # #

# from server.config import get_config
from server.models import (
    user as user_models,
)


###


async def name_exists(name: str) -> bool:
    """
    Checks if a user with the given username exists.
    """
    return await user_models.UserDoc.find({"name": name}).count() > 0


async def email_exists(email: str) -> bool:
    """
    Checks if a user with the given email exists.
    """
    return await user_models.UserDoc.find({"email": email}).count() > 0


async def create_user(
    user_signup: user_models.UserSignup,
) -> user_models.UserDoc:
    """
    Creates a new user with the given username, email and password.
    """
    doc_data = user_signup.model_dump()
    user_doc = await user_models.UserDoc.create(**doc_data)
    logger.info(f"Created user {user_doc.name} ({user_doc.id})")
    return user_doc


async def get_all_users() -> list[user_models.UserDoc]:
    """
    Get all users.
    """
    users = user_models.UserDoc.all()
    return await users.to_list()
