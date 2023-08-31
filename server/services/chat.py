# # System # #
from datetime import datetime, timedelta

# # Packages # #
from beanie import PydanticObjectId
from beanie.exceptions import DocumentNotFound
from beanie.operators import In
from bson.errors import InvalidId
from loguru import logger

# # Project # #

from server.ai import analyze_persona as ai_analyze_persona
from server.config import get_config
from server.models import (
    ChatDb,
    ChatIn,
    ChatOut,
    PersonaDb,
    PersonaIn,
    PersonaOut,
    MessageDb,
    MessageIn,
    MessageOut,
)

from .persona import get_narrator_persona

###


async def add_chat(
    chat_in: ChatIn | None = None,
) -> PydanticObjectId:
    # Create the chat in the database
    chat_db = ChatDb()  # id only
    await chat_db.insert()

    # The chat may have been created with a list of personas
    personas_db = []
    if chat_in.personas:
        non_narrator_personas = [
            persona
            for persona in chat_in.personas
            if persona.name != get_config().narrator
        ]
        for persona in non_narrator_personas:
            personas_db.append(
                PersonaDb(
                    name=persona.name,
                    traits=persona.traits,
                    story=persona.story,
                )
            )
        res = await PersonaDb.insert_many(personas_db)
        for i, p in enumerate(personas_db):
            p.id = res.inserted_ids[i]

    # If there aren't any messages, we're done
    if not chat_in.messages:
        return chat_db.id

    # If there aren't any personas, we need to infer them from the messages
    if not personas_db:
        # Personas could be names or ids (or both)
        persona_names = {u.speaker_name for u in chat_in.messages if u.speaker_name}
        for name in persona_names:
            personas_db.append(
                PersonaDb(
                    name=name,
                    traits="",
                    story="",
                )
            )
        res = await PersonaDb.insert_many(personas_db)
        for i, p in enumerate(personas_db):
            p.id = res.inserted_ids[i]
        persona_ids = {u.speaker_id for u in chat_in.messages if u.speaker_id}
        personas_db.append(
            await PersonaDb.find(In(PersonaDb.id, persona_ids)).to_list()
        )

    # Add the narrator persona if it's not already there
    if not any(p.name == get_config().narrator for p in personas_db):
        personas_db.append(await get_narrator_persona())

    # Map persona names to ids
    persona_dict = {p.name: p.id for p in personas_db}

    cur_ts = datetime.now()
    messages_db = []
    for message in chat_in.messages:
        pid = (
            message.speaker_id
            if message.speaker_id
            else persona_dict.get(message.speaker_name)
        )
        messages_db.append(
            MessageDb(
                ts=message.ts if message.ts else cur_ts,
                chat_id=chat_db.id,
                speaker_id=pid,
                text=message.text,
            )
        )
        cur_ts += timedelta(seconds=len(message.text.split(" ")))

    await MessageDb.insert_many(messages_db)
    return chat_db.id


async def get_chats(
    skip: int = 0,
    limit: int = 100,
) -> list[PydanticObjectId]:
    chats_db = await ChatDb.find_all(
        skip=skip,
        limit=limit,
    ).to_list()
    return [chat.id for chat in chats_db]


async def get_chat_personas(
    chat_id: str,
    name: str | None = None,
) -> list[PersonaDb]:
    # Get the personas for this chat
    query = PersonaDb.chat_id == chat_id
    if name:
        query &= PersonaDb.name == name
    personas_db = await PersonaDb.find(query).to_list()
    return personas_db


async def get_chat(
    chat_id: str,
) -> ChatOut:
    # Get the chat
    cid = PydanticObjectId(chat_id)
    chat_db = await ChatDb.get(cid)
    if not chat_db:
        raise DocumentNotFound("Chat not found")

    # Get the messages for this chat
    messages_db = await MessageDb.find(MessageDb.chat_id == chat_db.id).to_list()

    # Get the personas for this chat
    persona_ids = {u.speaker_id for u in messages_db}
    personas_db = await PersonaDb.find(In(PersonaDb.id, persona_ids)).to_list()

    persona_dict = {p.id: p for p in personas_db}
    messages_out = []
    for msg in messages_db:
        messages_out.append(
            MessageOut(
                ts=msg.ts,
                speaker_name=persona_dict[msg.speaker_id].name,
                text=msg.text,
            )
        )
    chat_out = ChatOut(
        personas=personas_db,
        messages=messages_out,
    )
    return chat_out


async def add_message(
    chat_id: str,
    persona_id: str,
    text: str,
) -> MessageDb:
    cid = PydanticObjectId(chat_id)
    pid = PydanticObjectId(persona_id)
    message_db = MessageDb(
        chat_id=cid,
        speaker_id=pid,
        text=text,
    )
    await message_db.insert()
    return message_db


async def update_message(
    chat_id: str,
    message_id: str,
    message_update: MessageIn,
) -> MessageOut:
    # Get the message
    mid = PydanticObjectId(message_id)
    message_db = await MessageDb.get(mid)
    if not message_db:
        raise DocumentNotFound("Message not found")

    # Validate that chat matches
    cid = PydanticObjectId(chat_id)
    if message_db.chat_id != cid:
        raise Exception("Message does not belong to chat")

    # Update the message
    if message_update.text:
        message_db.text = message_update.text
    if message_update.speaker_id:
        sid = PydanticObjectId(message_update.speaker_id)
        speaker_db = await PersonaDb.get(sid)
        if not speaker_db:
            raise DocumentNotFound("Speaker not found")
        message_db.speaker_id = sid
    if message_update.speaker_name:
        # TODO:
        pass

    await message_db.save()
    return message_db


async def add_narration(
    chat_id: str,
    text: str,
) -> MessageDb:
    cid = PydanticObjectId(chat_id)
    narrator_db = await get_narrator_persona()
    message_db = MessageDb(
        chat_id=cid,
        speaker_id=narrator_db.id,
        text=text,
    )
    await message_db.insert()
    return message_db


def _get_transcript_from_chat(
    chat_out: ChatOut,
) -> str:
    transcript = ""
    for msg in chat_out.messages:
        transcript += f"{msg.speaker_name}: {msg.text}\n"
    return transcript


async def get_transcript(
    chat_id: str,
) -> str:
    chat_out = await get_chat(chat_id)
    transcript = _get_transcript_from_chat(chat_out)
    return transcript


async def analyze_chat_persona(
    chat_id: str,
    persona_id: str,
) -> str:
    chat_out = await get_chat(chat_id)
    persona_db = await PersonaDb.get(persona_id)
    transcript = _get_transcript_from_chat(chat_out)
    analysis = ai_analyze_persona(
        transcript,
        persona_db.name,
        persona_db.story,
    )
    return analysis
