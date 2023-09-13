"""
User services
"""
# # System # #

# # Packages # #
from beanie import PydanticObjectId
from loguru import logger

# # Project # #
from server.models import (
    campaign as campaign_models,
    message as message_models,
    user as user_models,
)


###


async def create_message(
    campaign: PydanticObjectId,
    message_create: message_models.MessageCreate,
) -> message_models.MessageDoc:
    """
    Creates a new message with the given campaign, sender, target and content
    """
    # Note: MongoDB does not enforce foreign key constraints, so we need to
    # check that the campaign, sender and target exist before creating the
    # message to ensure referential integrity.

    # Ensure the campaign exists
    campaign_doc = await campaign_models.CampaignDoc.get(campaign)
    if campaign_doc is None:
        raise ValueError(f"Campaign with id {campaign} does not exist")

    # Ensure the sender exists
    sender_doc = await user_models.UserDoc.get(message_create.sender)
    if sender_doc is None:
        raise ValueError(f"User with id {message_create.sender} does not exist")

    # Ensure the target exists
    if message_create.target is not None:
        target_doc = await user_models.UserDoc.get(message_create.target)
        if target_doc is None:
            raise ValueError(f"User with id {message_create.target} does not exist")

    # Create the message
    message_doc = await message_models.MessageDoc.create(
        campaign=campaign,
        sender=message_create.sender,
        target=message_create.target,
        content=message_create.content,
    )
    logger.info(f"Created message {message_doc.id}")
    return message_doc


async def get_campaign_messages(
    campaign: PydanticObjectId,
    skip: int = 0,
    limit: int = 100,
) -> list[message_models.MessageDoc]:
    """
    Get all messages for a campaign
    """
    messages = await message_models.MessageDoc.find(
        message_models.MessageDoc.campaign == campaign,
        sort=[("timestamp", 1)],
        skip=skip,
        limit=limit,
    ).to_list()
    logger.info(f"Got {len(messages)} messages for campaign {campaign}")
    return messages


async def update_message(
    id: PydanticObjectId,
    message: message_models.MessageUpdate,
) -> message_models.MessageDoc:
    """
    Updates a message with the given campaign, sender, target and content
    """
    message_doc = await message_models.MessageDoc.get(id)
    if message_doc is None:
        raise ValueError(f"Message with id {id} does not exist")
    await message_doc.set(message.dict())
    logger.info(f"Updated message: {message_doc})")
    return message_doc


async def delete_message(
    id: PydanticObjectId,
) -> message_models.MessageDoc:
    """
    Deletes a message
    """
    message_doc = await message_models.MessageDoc.get(id)
    if message_doc is None:
        raise ValueError(f"Message with id {id} does not exist")
    await message_doc.delete()
    logger.info(f"Deleted message: {message_doc})")
    return message_doc
