"""
Game page
"""
# # # System # # #
import os

# # # Packages # # #
import chat_rpg_client as client
import streamlit as st
from streamlit.elements.image import AtomicImage
from PIL import Image

# # # Project # # #

#

st.set_page_config(
    page_title="Game",
    page_icon="🎲",
    layout="wide",
    initial_sidebar_state="expanded",
)


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
    messages_api = st.session_state.messages_api
    message_create = client.MessageCreate(
        campaign=st.session_state.campaign.id,
        sender=st.session_state.user.id,
        # target=st.session_state.user.id,
        content=content,
    )
    messages_api.send_message(
        campaign=st.session_state.campaign.id,
        message_create=message_create,
    )

    del st.session_state.messages


#
# State initialization
#

if "client" not in st.session_state:
    configuration = client.Configuration(
        host=st.session_state.server_url,
    )
    api_client = client.ApiClient(
        configuration=configuration,
        header_name="User-Agent",
        header_value="chat-rpg-client",
    )
    st.session_state.client = api_client

if "campaigns_api" not in st.session_state:
    api_client = st.session_state.client
    campaigns_api = client.CampaignsApi(
        api_client=api_client,
    )
    st.session_state.campaigns_api = campaigns_api

if "campaigns" not in st.session_state:
    try:
        # Get Campaigns
        campaigns_api = st.session_state.campaigns_api
        campaigns = [
            client.Campaign(**campaign)
            for campaign in campaigns_api.get_all_campaigns()
        ]
        st.session_state.campaigns = campaigns
        if len(campaigns) > 0:
            st.session_state.campaign = campaigns[0]
    except client.ApiException as e:
        st.exception(f"Exception when calling CampaignsApi->get_all_campaigns: {e}\n")

if "users_api" not in st.session_state:
    api_client = st.session_state.client
    users_api = client.UsersApi(
        api_client=api_client,
    )
    st.session_state.users_api = users_api

if "users" not in st.session_state:
    try:
        # Get Users
        users_api = st.session_state.users_api
        users = [client.User(**user) for user in users_api.get_all_users()]
        st.session_state.users = users
    except client.ApiException as e:
        st.exception("Exception when calling UsersApi->get_all_users: %s\n" % e)

if "messages_api" not in st.session_state:
    api_client = st.session_state.client
    messages_api = client.MessagesApi(
        api_client=api_client,
    )
    st.session_state.messages_api = messages_api


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

st.selectbox(
    label="Select a user",
    options=st.session_state.users,
    index=0,
    key="user",
    format_func=lambda user: user.username,
)


if "messages" not in st.session_state and "campaign" in st.session_state:
    try:
        messages_api = st.session_state.messages_api
        messages = [
            client.Message(**message)
            for message in messages_api.get_campaign_messages(
                campaign=st.session_state.campaign.id,
            )
        ]
        st.session_state.messages = messages
    except client.ApiException as e:
        st.exception(
            f"Exception when calling MessagesApi->get_campaign_messages: {e}\n"
        )

name = st.session_state.user.username if st.session_state.user else None
campaign_name = st.session_state.campaign.name if st.session_state.campaign else None
if name and campaign_name:
    st.write(f"Greetings {name}!")
    st.write(f"You are currently playing in the {campaign_name} campaign.")
    if "messages" in st.session_state:
        st.write(
            f"There are {len(st.session_state.messages)} messages in the campaign."
        )
else:
    st.write("Please select a user and campaign")
    st.stop()


if "messages" in st.session_state:
    for message in st.session_state.messages:
        sender = _get_user_name(message.sender)
        with st.chat_message(
            name=sender,
            avatar=_get_user_avatar(message.sender),
        ):
            target = _get_user_name(message.target)
            st.write(f"**{sender}** says to **{target}**:")
            st.write(message.content)


prompt = st.chat_input("Say something")
if prompt:
    send_message(prompt)
    st.experimental_rerun()
