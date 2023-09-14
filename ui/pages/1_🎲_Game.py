"""
Game page
"""
# # # System # # #
import asyncio
import os
import random
from typing import NoReturn

# # # Packages # # #
import chat_rpg_client as client
from PIL import Image
import streamlit as st
from streamlit.elements.image import AtomicImage

# import asyncio
# import threading
# from streamlit.runtime.scriptrunner import add_script_run_ctx
# import websockets
# import aiohttp

# # # Project # # #
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


# st.markdown(
#     """
#     <style>
#     .time {
#         font-size: 130px !important;
#         font-weight: 700 !important;
#         color: #ec5953 !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )


# status = st.empty()

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

#     def start_async_loop(
#         server_socket,
#         status,
#     ):
#         status.subheader("Connecting...")
#         loop = asyncio.new_event_loop()
#         asyncio.set_event_loop(loop)
#         loop.run_until_complete(
#             socket_task(
#                 server_socket,
#                 status,
#             )
#         )
#         loop.close()

#     thread = threading.Thread(
#         target=start_async_loop,
#         args=(st.session_state.server_socket, status),
#     )
#     add_script_run_ctx(thread)
#     thread.start()
#     st.session_state.socket_task = thread


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
def _get_user_name(
    user_id: str,
) -> str:
    """
    Get the name of a user
    """
    if not user_id:
        return "all"

    user = _get_user(user_id)
    return user.username if user else "Unknown"


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
# Callbacks (_before_ the state is managed, so we can make changes)
#
def send_message(
    content: str,
) -> None:
    """
    Send a message to the campaign
    """
    sender = st.session_state.user.id
    target = None
    is_private = False

    if content.startswith("/"):
        first_space = content.find(" ")
        if first_space == -1:
            first_space = len(content)
        details = content[first_space:].strip()

        command = content[1:first_space]
        if command == "roll":
            if details:
                roll = details.split("d")
                if len(roll) == 2:
                    num_dice = int(roll[0])
                    num_sides = int(roll[1])
                    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
                    content = f"Rolling {num_dice}d{num_sides}: {rolls}"
                else:
                    content = "Invalid roll"
            else:
                content = "Please specify a roll, e.g., :red[2]:green[d]:orange[20]"
            target = sender
            is_private = True
        elif command == "dm":
            if details:
                target = details
                content = f"Sending a message to {target}"
            else:
                content = "Please specify a user to send a message to"
            is_private = True
        elif command == "help":
            content = """
            **/roll** - Roll some dice, e.g., `/roll 2d20`\n
            **/dm** - Send a private message to a user, e.g., `/dm @user`
            """
            target = sender
            is_private = True

    messages_api = st.session_state.messages_api
    message_create = client.MessageCreate(
        campaign=st.session_state.campaign.id,
        sender=sender,
        target=target,
        content=content,
        is_private=is_private,
    )
    messages_api.send_message(
        message_create=message_create,
    )

    del st.session_state.messages


#
# UI
#

st.title("🎲 Game")

st.header("Campaigns")


st.selectbox(
    label="Select a campaign",
    options=st.session_state.campaigns,
    index=0,
    key="campaign",
    format_func=lambda campaign: campaign.name,
)


name = st.session_state.user.username if st.session_state.user else None
campaign_name = st.session_state.campaign.name if st.session_state.campaign else None
if name and campaign_name:
    st.write(f"Greetings {name}!")
    st.write(f"You are currently playing in the {campaign_name} campaign.")
else:
    st.write("Please select a user and campaign")
    st.stop()


async def watch() -> NoReturn:
    while True:
        if "campaign" in st.session_state:
            since = None
            if "messages" not in st.session_state:
                st.session_state.messages = []
            else:
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
            except client.ApiException as e:
                st.exception(
                    f"Exception when calling MessagesApi->get_campaign_messages: {e}\n"
                )

            for message in st.session_state.messages:
                if not since or message.timestamp > since:
                    sender = _get_user_name(message.sender)
                    with st.chat_message(
                        name=sender,
                        avatar=_get_user_avatar(message.sender),
                    ):
                        target = _get_user_name(message.target)
                        st.write(f"**{sender}** says to **{target}**:")
                        st.write(message.content)

        # test.markdown(
        #     f"""
        #     <p class="time">
        #         {str(datetime.now())}
        #     </p>
        #     """,
        #     unsafe_allow_html=True,
        # )
        r = await asyncio.sleep(1)


prompt = st.chat_input("Speak")
if prompt:
    send_message(prompt)


asyncio.run(watch())
