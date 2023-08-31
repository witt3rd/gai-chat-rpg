"""
Chat models
"""

# # System # #
from datetime import datetime

# # Packages # #
from beanie import Document, PydanticObjectId
from pydantic import BaseModel, Field

# # Project # #

###

# Define models


class MessageDb(Document):
    """
    Message suitable for the db.
    """

    ts: datetime = Field(default_factory=datetime.now)
    chat_id: PydanticObjectId
    speaker_id: PydanticObjectId
    text: str

    class Settings:
        name = "message"
        indexes = ["chat_id", "speaker_id"]


class MessageIn(BaseModel):
    """
    Message suitable for input.
    """

    ts: datetime | None = None
    speaker_name: str | None = None
    speaker_id: str | None = None
    text: str


class MessageOut(BaseModel):
    """
    Message suitable for output.
    """

    ts: datetime
    speaker_name: str
    text: str
