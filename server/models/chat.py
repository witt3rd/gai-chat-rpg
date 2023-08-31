"""
Chat models
"""

# # System # #

# # Packages # #
from beanie import Document
from pydantic import BaseModel

# # Project # #
from .persona import PersonaIn, PersonaOut
from .message import MessageIn, MessageOut

###

# Define models


class ChatDb(Document):
    """
    Chat suitable for the db.
    """

    # id only

    class Settings:
        name = "chat"


class ChatIn(BaseModel):
    """
    Chat suitable for input.
    """

    personas: list[PersonaIn] | None = None
    messages: list[MessageIn] | None = None


class ChatOut(BaseModel):
    """
    Chat suitable for output.
    """

    personas: list[PersonaOut] | None = None
    messages: list[MessageOut] | None = None
