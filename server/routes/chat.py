# # System # #
from datetime import datetime, timedelta

# # Packages # #
from beanie import PydanticObjectId
from fastapi import APIRouter

# # Project # #

from server.ai import analyze_persona as ai_analyze_persona
from server.config import get_config
from server.models import (
    ChatIn,
    ChatOut,
    PersonaOut,
    MessageDb,
    MessageIn,
    MessageOut,
)
from server.services import chat as chat_service

from .persona import get_narrator_persona

###

router = APIRouter()


@router.post(
    "/",
    response_model=PydanticObjectId,
)
async def add_chat(
    chat_in: ChatIn | None = None,
) -> PydanticObjectId:
    return await chat_service.add_chat(chat_in)


@router.get(
    "/",
    response_model=list[PydanticObjectId],
)
async def get_chats(
    skip: int = 0,
    limit: int = 100,
) -> list[PydanticObjectId]:
    return await chat_service.get_chats(skip, limit)


@router.get(
    "/{chat_id}/personas",
    response_model=list[PersonaOut],
    responses={
        404: {"description": "Chat not found"},
        400: {"description": "Invalid chat ID"},
    },
)
async def get_chat_personas(
    chat_id: str,
    name: str = None,
) -> list[PersonaOut]:
    return await chat_service.get_chat_personas(chat_id, name)


@router.get(
    "/{chat_id}",
    response_model=ChatOut,
    responses={
        404: {"description": "Chat not found"},
        400: {"description": "Invalid chat ID"},
    },
)
async def get_chat(
    chat_id: str,
) -> ChatOut:
    return await chat_service.get_chat(chat_id)


@router.post(
    "/{chat_id}/message",
    response_model=MessageDb,
)
async def add_message(
    chat_id: str,
    persona_id: str,
    text: str,
) -> MessageDb:
    return await chat_service.add_message(
        chat_id,
        persona_id,
        text,
    )


@router.patch(
    "/{chat_id}/message/{message_id}",
    response_model=MessageOut,
)
async def update_message(
    chat_id: str,
    message_id: str,
    message_update: MessageIn,
) -> MessageOut:
    return await chat_service.update_message(
        chat_id,
        message_id,
        message_update,
    )


@router.post(
    "/{chat_id}/narration",
    response_model=MessageOut,
)
async def add_narration(
    chat_id: str,
    text: str,
) -> MessageOut:
    return await chat_service.add_narration(chat_id, text)


@router.get(
    "/{chat_id}/transcript",
    response_model=str,
    responses={
        404: {"description": "Chat not found"},
        400: {"description": "Invalid chat ID"},
    },
)
async def get_transcipt(
    chat_id: str,
) -> str:
    return await chat_service.get_transcript(chat_id)


@router.post(
    "/{chat_id}/persona/{persona_id}/analysis}",
    response_model=str,
    responses={
        404: {"description": "Chat not found"},
        400: {"description": "Invalid chat ID or persona name"},
    },
    tags=["Personas"],
)
async def analyze_chat_persona(
    chat_id: str,
    persona_id: str,
) -> str:
    return await chat_service.analyze_chat_persona(
        chat_id,
        persona_id,
    )
