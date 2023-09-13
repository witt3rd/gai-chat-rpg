"""
User administration routes
"""
# # System # #

# # Packages # #
from beanie import PydanticObjectId
from bson.errors import InvalidId
from fastapi import APIRouter, HTTPException, status

# # Project # #
from server.models import (
    user as user_models,
)
from server.services import (
    users as user_services,
)

###

router = APIRouter()


@router.get(
    "/",
    response_model=list[user_models.User],
    status_code=status.HTTP_200_OK,
    description="Get all users",
    operation_id="get_all_users",
)
async def all_users() -> list[user_models.User]:
    """
    Get all users
    """
    users = await user_services.all_users()
    users_out = [user_models.User(**user.dict(by_alias=False)) for user in users]
    return users_out


@router.post(
    "/",
    response_model=user_models.User,
    status_code=status.HTTP_201_CREATED,
    description="Create a new user",
    operation_id="create_user",
)
async def create_user(
    user: user_models.UserCreate,
) -> user_models.User:
    """
    Create a new user
    """
    user_doc = await user_services.create_user(user)
    return user_models.User(**user_doc.dict())


@router.patch(
    "/{id}",
    response_model=user_models.User,
    status_code=status.HTTP_200_OK,
    description="Update a user",
    operation_id="update_user",
)
async def update_user(
    id: str,
    user: user_models.UserUpdate,
) -> user_models.User:
    """
    Update a user
    """
    print(f"\n\nID: {id}\n{user}\n\n")
    try:
        user_id = PydanticObjectId(id)
    except InvalidId as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user ID.",
        ) from exc
    user_doc = await user_services.update_user(
        id=user_id,
        user=user,
    )
    return user_models.User(**user_doc.dict())


@router.delete(
    "/{id}",
    response_model=user_models.User,
    status_code=status.HTTP_200_OK,
    description="Delete a user",
    operation_id="delete_user",
)
async def delete_user(
    id: str,
) -> user_models.User:
    """
    Delete a user
    """
    try:
        user_id = PydanticObjectId(id)
    except InvalidId as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user ID.",
        ) from exc
    user_doc = await user_services.delete_user(
        id=user_id,
    )
    return user_models.User(**user_doc.dict())
