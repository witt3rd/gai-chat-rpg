"""
Mesaging routes
"""
# # System # #

# # Packages # #
from beanie import PydanticObjectId
from bson.errors import InvalidId
from fastapi import APIRouter, HTTPException, status

# # Project # #
from server.models import (
    message as message_models,
)
from server.services import (
    messages as message_services,
)

###

router = APIRouter()


@router.post(
    "/{campaign}",
    response_model=message_models.Message,
    status_code=status.HTTP_201_CREATED,
    description="Create a new message.",
    operation_id="send_message",
)
async def send_message(
    campaign: str,
    message: message_models.MessageCreate,
) -> message_models.Message:
    """
    Create a new message
    """
    message_doc = await message_services.create_message(
        campaign,
        message,
    )
    return message_models.Message(**message_doc.dict())


@router.get(
    "/{campaign}",
    response_model=list[message_models.Message],
    status_code=status.HTTP_200_OK,
    description="Get all messages for a campaign",
    operation_id="get_campaign_messages",
)
async def get_campaign_messages(
    campaign: PydanticObjectId,
    skip: int = 0,
    limit: int = 100,
) -> list[message_models.Message]:
    """
    Get all messages for a campaign
    """
    messages = await message_services.get_campaign_messages(
        campaign=campaign,
        skip=skip,
        limit=limit,
    )
    return [message_models.Message(**message.dict()) for message in messages]


@router.patch(
    "/{id}",
    response_model=message_models.Message,
    status_code=status.HTTP_200_OK,
    description="Update a message.",
    operation_id="update_message",
)
async def update_message(
    id: str,
    message: message_models.MessageUpdate,
) -> message_models.Message:
    """
    Update a message
    """
    print(f"\n\nID: {id}\n{message}\n\n")
    try:
        message_id = PydanticObjectId(id)
    except InvalidId as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid message ID.",
        ) from exc

    message_doc = await message_services.update_message(
        id=message_id,
        message=message,
    )
    return message_models.Message(**message_doc.dict())


@router.delete(
    "/{id}",
    response_model=message_models.Message,
    status_code=status.HTTP_200_OK,
    description="Delete a message",
    operation_id="delete_message",
)
async def delete_message(
    id: str,
) -> message_models.Message:
    """
    Delete a message
    """
    try:
        message_id = PydanticObjectId(id)
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid message ID.",
        )
    message_doc = await message_services.delete_message(
        id=message_id,
    )
    return message_models.Message(**message_doc.dict())
