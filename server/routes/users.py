"""
User administration routes.
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

# from server.services import (
#     user as user_service,
# )

###

router = APIRouter()

"""
  - `GET /users` - to retrieve all users. This could be an admin-only route.
  - `GET /users/{user_id}` - to retrieve a particular user's detail. This could be for the user themselves or for an admin.
  - `PUT /users/{user_id}` - to update a particular user's data. This could be for the user themselves for updating their profile info or for an admin for enabling/disabling a user account.
  - `DELETE /users/{user_id}` - to delete a user, potentially for admin purposes.
"""