"""
Authentication service.
"""
# # System # #

# # Packages # #
from beanie import PydanticObjectId
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
    doc_data = user_signup.dict()
    user_doc = await user_models.UserDoc.create(**doc_data)
    logger.info(f"Created user {user_doc.name} ({user_doc.id})")
    return user_doc


async def all_users() -> list[user_models.UserDoc]:
    """
    Get all users.
    """
    users = user_models.UserDoc.all()
    return await users.to_list()


async def update_user(
    id: str,
    user: user_models.UserIn,
) -> user_models.UserDoc:
    """
    Updates a user with the given username, email and password.
    """
    user_doc = await user_models.UserDoc.get(id)
    if user_doc is None:
        raise ValueError(f"User with id {id} does not exist")
    await user_doc.set(user.dict())
    logger.info(f"Updated user: {user_doc})")
    return user_doc


async def delete_user(
    id: str,
) -> user_models.UserDoc:
    """
    Deletes a user with the given username, email and password.
    """
    user_doc = await user_models.UserDoc.get(id)
    if user_doc is None:
        raise ValueError(f"User with id {id} does not exist")
    await user_doc.delete()
    logger.info(f"Deleted user: {user_doc})")
    return user_doc
