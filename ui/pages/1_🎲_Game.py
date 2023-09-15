"""
Game page
"""
# # # System # # #
import asyncio
from datetime import datetime
import locale
import os
import random
from typing import NoReturn

# # # Packages # # #
import chat_rpg_client as client
from PIL import Image
from pydantic import BaseModel
import streamlit as st
from streamlit.elements.image import AtomicImage


# import websockets
# import aiohttp

# # # Project # # #
import ui.ai as ai
from ui.sidebar import show_sidebar

#

st.set_page_config(
    page_title="Game",
    page_icon="🎲",
    layout="wide",
    initial_sidebar_state="expanded",
)
show_sidebar()

#
# Websockets
#


# if "socket_task" not in st.session_state:

#     async def socket_task(
#         server_socket,
#         status,
#     ) -> None:
#         # async with websockets.connect(
#         #     server_socket,
#         # ) as websocket:
#         #     status.success(f"Connected to socket: {server_socket}")
#         #     while True:
#         #         response = await websocket.recv()
#         #         status.write(response)
#         async with aiohttp.ClientSession(trust_env=True) as session:
#             status.subheader("Connecting...")
#             async with session.ws_connect(server_socket) as ws:
#                 status.subheader("Connected!")
#                 while True:
#                     response = await ws.receive()
#                     status.subheader(response.data)


#
# Helpers
#


@st.cache_data()
def _get_user(
    user_id: str,
) -> client.User | None:
    for user in st.session_state.users:
        if user.id == user_id:
            return user


@st.cache_data()
def _get_user_by_username(
    username: str,
) -> client.User | None:
    for user in st.session_state.users:
        if user.username == username:
            return user


@st.cache_data()
def _get_user_name(
    user_id: str,
) -> str | None:
    """
    Get the name of a user
    """
    if not user_id:
        return "all"

    user = _get_user(user_id)
    return user.username if user else None


@st.cache_data()
def _get_user_avatar(
    user_id: str,
) -> AtomicImage | None:
    """
    Get the avatar of a user
    """
    if not user_id:
        return None

    user = _get_user(user_id)
    if not user:
        return None
    image_file = os.path.join(os.path.dirname(__file__), "..", "static", user.avatar)
    return Image.open(image_file)


#
# Commands
#


class CmdResult(BaseModel):
    sender_id: str
    target_id: str | None
    content: str


def _cmd_roll(
    details: str | None,
) -> CmdResult:
    if not details:
        content = "Please specify a roll, e.g., :red[2]:green[d]:orange[20]"
    else:
        roll = details.split("d")
        if len(roll) == 2:
            num_dice = int(roll[0])
            num_sides = int(roll[1])
            rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
            user = st.session_state.user.username
            content = (
                f"🎲 :green[**{user}**] rolls {num_dice}d{num_sides}: :orange[{rolls}]"
            )
        else:
            content = "Invalid roll"
    return CmdResult(
        sender_id=_get_user_by_username("System").id,
        content=content,
    )


def _cmd_dm(
    details: str | None,
) -> CmdResult:
    # make some assymptions
    sender_id = system_user.id
    target_id = st.session_state.user.id

    if not details:
        content = "Please specify a user and a message"
    else:
        if not details.startswith("@"):
            content = "Please specify a user to send a message to"
        else:
            first_space = details.find(" ")
            if first_space == -1:
                content = f"Please specify a message to send :blue[{details}]"
            else:
                target_username = details[1:first_space]
                content = details[first_space:].strip()

                if target_username == "gpt4":
                    # Ask GPT-4
                    chat_model = ai.get_chat_model()
                    content = ai.ask_gpt(chat_model, content)
                    sender_id = _get_user_by_username("GPT4").id
                    target_id = st.session_state.user.id
                else:
                    target = _get_user_by_username(target_username)
                    if not target:
                        content = f"User :blue[@{target_username}] not found"
                    else:
                        target_id = target.id
                        sender_id = st.session_state.user.id
    return CmdResult(
        sender_id=sender_id,
        target_id=target_id,
        content=content,
    )


def _cmd_help(
    details: str | None,
) -> CmdResult:
    return CmdResult(
        sender_id=_get_user_by_username("System").id,
        target_id=st.session_state.user.id,
        content="""
        |:orange[Command]|:orange[Args]|:orange[Description]|
        |------|------|-----|
        |:blue[**/roll**] | _n_:blue[**d**]_m_ | Roll some dice, e.g., `/roll 2d20`|
        |:blue[**/dm**] | :green[@useername] _message_ | Send a private message to a user, e.g., `/dm @user ...`|
        """,
    )


#
# Callbacks (_before_ the state is managed, so we can make changes)
#

cmd_dispatch = {
    "roll": _cmd_roll,
    "dm": _cmd_dm,
    "help": _cmd_help,
}


def _delete_message(
    message_id: str,
) -> None:
    """
    Delete a message
    """
    messages_api = st.session_state.messages_api
    messages_api.delete_message(
        id=message_id,
    )
    if "messages" in st.session_state:
        del st.session_state.messages
        st.session_state.reset_messages = True


def _send_message(
    content: str,
) -> None:
    """
    Send a message to the campaign
    """

    # system_user = _get_user_by_username("System")
    # gpt4_user = _get_user_by_username("GPT4")

    if content.startswith("/"):
        first_space = content.find(" ")
        if first_space == -1:
            first_space = len(content)
        details = content[first_space:].strip()

        command = content[1:first_space]
        if command in cmd_dispatch:
            result = cmd_dispatch[command](details)
        else:
            result = CmdResult(
                sender_id=_get_user_by_username("System").id,
                target_id=st.session_state.user.id,
                content=f"Unknown command: :blue[{command}]",
            )
    else:
        result = CmdResult(
            sender_id=st.session_state.user.id,
            content=content,
        )

    messages_api = st.session_state.messages_api
    message_create = client.MessageCreate(
        campaign=st.session_state.campaign.id,
        sender=result.sender_id,
        target=result.target_id,
        content=result.content,
    )
    messages_api.send_message(
        message_create=message_create,
    )

    if "messages" in st.session_state:
        del st.session_state.messages


#
# UI
#

st.title("🎲 Game")

campaign_options = st.session_state.campaigns if "campaigns" in st.session_state else []
st.selectbox(
    label="Campaign",
    options=campaign_options,
    index=0,
    key="campaign",
    format_func=lambda campaign: campaign.name,
)


name = st.session_state.user.username if st.session_state.user else None
campaign_name = st.session_state.campaign.name if st.session_state.campaign else None
if name and campaign_name:
    st.write(
        f"Greetings :green[**{name}**]! You are currently playing in the :blue[**{campaign_name}**] campaign."
    )
else:
    st.write("Please select a user and campaign")
    st.stop()


def _is_private(
    sender_id: str,
    target_id: str,
) -> bool:
    user_id = st.session_state.user.id
    if target_id == user_id:
        return True
    if sender_id == user_id and target_id not in [None, ""]:
        return True
    return False


async def message_worker() -> None:
    """
    Get messages from the server
    """
    await asyncio.sleep(1)

    if "campaign" not in st.session_state:
        return

    since = None
    if "messages" not in st.session_state:
        st.session_state.messages = []
    else:
        if len(st.session_state.messages) > 0:
            # Get the timestamp of the last message
            last_message = st.session_state.messages[-1]
            since = last_message.timestamp

    try:
        messages_api = st.session_state.messages_api
        messages = [
            client.Message(**message)
            for message in messages_api.get_messages(
                campaign=st.session_state.campaign.id,
                since=since,
            )
        ]
        if len(messages) > 0:
            st.session_state.messages.extend(messages)
            st.experimental_rerun()

    except client.ApiException as e:
        st.exception(f"Exception when calling MessagesApi->get_messages: {e}\n")


if "message_controls" not in st.session_state:
    st.session_state.message_controls = False
if "reset_messages" not in st.session_state:
    st.session_state.reset_messages = False

# Render messages
if "messages" in st.session_state:
    system_user = _get_user_by_username("System")

    with st.container():
        for message in st.session_state.messages:
            # Only show messages that are public or private to the user
            if message.target not in [None, "", st.session_state.user.id]:
                # Message not meant for this user, skip it unless it was sent by the user
                if message.sender != st.session_state.user.id:
                    continue
            sender_name = _get_user_name(message.sender)
            with st.chat_message(
                name=sender_name,
                avatar=_get_user_avatar(message.sender),
            ):
                user_id = st.session_state.user.id
                if message.sender == system_user.id:
                    sender_display = f":red[**{sender_name}**]"
                else:
                    sender_display = (
                        f":green[**{sender_name}**]"
                        if message.sender == user_id
                        else f":blue[**{sender_name}**]"
                    )

                target_name = _get_user_name(message.target)
                target_display = (
                    f":green[**{target_name}**]"
                    if message.target == user_id
                    else f":blue[**{target_name}**]"
                )

                # Parse the timestamp string into a datetime object
                timestamp = datetime.strptime(message.timestamp, "%Y-%m-%dT%H:%M:%S.%f")

                # Convert the timestamp to the local timezone
                local_timestamp = timestamp.astimezone()

                # Format the timestamp according to the system's locale settings
                formatted_timestamp = local_timestamp.strftime(
                    locale.nl_langinfo(locale.D_T_FMT)
                )

                time_display = f":grey[{formatted_timestamp}]"
                is_private = _is_private(
                    message.sender,
                    message.target,
                )

                if is_private:
                    st.write(f"🔒{sender_display} to {target_display} {time_display}")
                else:
                    st.write(f"{sender_display} {time_display}")
                st.write(message.content)

                if st.session_state.message_controls:
                    if st.button("Delete", key=f"delete_{message.id}"):
                        _delete_message(message.id)

prompt = st.chat_input("Speak!")
if prompt:
    _send_message(prompt)

#
# Sidebar UI
#

st.sidebar.markdown("---")
st.sidebar.markdown("## Game Controls")
if st.sidebar.button("🎲 Roll 1d20"):
    _send_message("/roll 1d20")
st.sidebar.checkbox("Message Controls", key="message_controls")
#
# Main
#


async def main() -> NoReturn:
    with st.empty():
        while True:
            await asyncio.gather(message_worker())


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        loop.close()
