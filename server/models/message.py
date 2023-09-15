"""
Message Models
"""

# # System # #
import datetime

# # Packages # #
from beanie import Document, PydanticObjectId
from pydantic import BaseModel, Field
from pymongo import IndexModel, ASCENDING

# # Project # #

###


class MessageDoc(Document):
    class Settings:
        collection = "messages"
        indexes = [
            IndexModel([("campaign", ASCENDING)], unique=False),
            IndexModel([("sender", ASCENDING)], unique=False),
            IndexModel([("target", ASCENDING)], unique=False),
        ]

    timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.utcnow,
    )
    campaign: PydanticObjectId
    sender: PydanticObjectId
    target: PydanticObjectId | None
    content: str = Field(..., min_length=1)
    is_private: bool = Field(False)
    is_edited: bool = Field(False)

    @classmethod
    async def create(
        cls,
        campaign: PydanticObjectId,
        sender: PydanticObjectId,
        content: str,
        target: PydanticObjectId | None = None,
        is_edited: bool = False,
    ) -> "MessageDoc":
        """
        Creates a new message with the given campaign, sender, target and content
        """
        message_doc = cls(
            campaign=campaign,
            sender=sender,
            target=target,
            content=content,
            is_edited=is_edited,
        )
        await message_doc.insert()
        return message_doc


class MessageCreate(BaseModel):
    """
    New message data
    """

    campaign: PydanticObjectId
    sender: PydanticObjectId
    target: PydanticObjectId | None = None
    content: str
    is_private: bool = False

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {PydanticObjectId: str}


class MessageUpdate(BaseModel):
    """
    Update of message data
    """

    campaign: PydanticObjectId | None = None
    sender: PydanticObjectId | None = None
    target: PydanticObjectId | None = None
    content: str | None = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {PydanticObjectId: str}


class Message(BaseModel):
    """
    Output of message data
    """

    id: PydanticObjectId = Field(..., alias="_id")
    timestamp: datetime.datetime
    campaign: PydanticObjectId
    sender: PydanticObjectId
    target: PydanticObjectId | None
    content: str
    is_edited: bool

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {PydanticObjectId: str}
