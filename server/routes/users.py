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
from server.services import (
    users as user_services,
)

###

router = APIRouter()

"""
  - `GET /users` - to retrieve all users. This could be an admin-only route.
  - `GET /users/{user_id}` - to retrieve a particular user's detail. This could be for the user themselves or for an admin.
  - `PUT /users/{user_id}` - to update a particular user's data. This could be for the user themselves for updating their profile info or for an admin for enabling/disabling a user account.
  - `DELETE /users/{user_id}` - to delete a user, potentially for admin purposes.
"""


def user_doc_to_user_out(
    user_doc: user_models.UserDoc,
) -> user_models.UserOut:
    user_dict = user_doc.dict(by_alias=False)
    user_dict["id"] = str(user_dict["id"])
    user_out = user_models.UserOut(**user_dict)
    return user_out


@router.get(
    "/",
    response_model=list[user_models.UserOut],
    status_code=status.HTTP_200_OK,
    description="Get all users.",
    operation_id="get_all_users",
)
async def all_users() -> list[user_models.UserOut]:
    """
    Get all users.
    """
    users = await user_services.all_users()
    users_out = [user_doc_to_user_out(user) for user in users]
    return users_out


@router.post(
    "/",
    response_model=user_models.UserOut,
    status_code=status.HTTP_201_CREATED,
    description="Create a new user.",
    operation_id="create_user",
)
async def create_user(
    user: user_models.UserSignup,
) -> user_models.UserOut:
    """
    Create a new user.
    """
    user_doc = await user_services.create_user(user)
    return user_doc_to_user_out(user_doc)


@router.patch(
    "/{id}",
    response_model=user_models.UserOut,
    status_code=status.HTTP_200_OK,
    description="Update a user.",
    operation_id="update_user",
)
async def update_user(
    id: str,
    user: user_models.UserIn,
) -> user_models.UserOut:
    """
    Update a user.
    """
    try:
        user_id = PydanticObjectId(id)
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user ID.",
        )
    user_doc = await user_services.update_user(
        id=user_id,
        user=user,
    )
    return user_doc_to_user_out(user_doc)


@router.delete(
    "/{id}",
    response_model=user_models.UserOut,
    status_code=status.HTTP_200_OK,
    description="Delete a user.",
    operation_id="delete_user",
)
async def delete_user(
    id: str,
) -> user_models.UserOut:
    """
    Delete a user.
    """
    try:
        user_id = PydanticObjectId(id)
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user ID.",
        )
    user_doc = await user_services.delete_user(
        id=user_id,
    )
    return user_doc_to_user_out(user_doc)
