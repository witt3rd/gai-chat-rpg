"""
Authentication routes for the API.
"""
# # System # #

# # Packages # #
from beanie import PydanticObjectId
from bson.errors import InvalidId
from fastapi import APIRouter, HTTPException, status
from loguru import logger

# # Project # #
from server.config import get_config
from server.models import (
    user as user_models,
)
from server.services import (
    auth as auth_service,
)

###

router = APIRouter()


@router.post("/signup")
async def signup(
    user_signup: user_models.UserSignup,
) -> PydanticObjectId:
    """
    Register a new user.
    """
    if await auth_service.email_exists(user_signup.email):
        raise HTTPException(status_code=400, detail="Email already registered")

    if await auth_service.username_exists(user_signup.username):
        raise HTTPException(status_code=400, detail="Username already registered")

    user = await auth_service.create_user(user_signup)
    return user.id


@router.post("/login")
async def login() -> None:
    """
    TODO: Login a user.
    """
    pass
