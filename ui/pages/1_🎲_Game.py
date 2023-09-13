"""
Game page
"""
# # # System # # #

# # # Packages # # #
import chat_rpg_client as client
import streamlit as st

# # # Project # # #
from ui.util.config import get_config

#

st.set_page_config(
    page_title="Game",
    page_icon="🎲",
    layout="wide",
    initial_sidebar_state="expanded",
)

#
# Callbacks (_before_ the state is managed, so we can make changes)
#


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
        st.exception(
            "Exception when calling UsersApi->get_users_users_users_get: %s\n" % e
        )

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
    except client.ApiException as e:
        st.exception(f"Exception when calling CampaignsApi->get_all_campaigns: {e}\n")


#
# UI
#

st.title("🎲 Game")

st.header("Campaigns")


st.selectbox(
    label="Select a user",
    options=st.session_state.users,
    index=0,
    key="user",
    format_func=lambda user: user.username,
)

st.selectbox(
    label="Select a campaign",
    options=st.session_state.campaigns,
    index=0,
    key="campaign",
    format_func=lambda campaign: campaign.name,
)


if "messages" not in st.session_state:
    ms = [
        {
            "sender": "Dungeon Master",
            "target": "All",
            "content": "Welcome to the game!",
        },
        {
            "sender": "Thor",
            "target": "All",
            "content": "/dan roll 1d20",
        },
    ]
    st.session_state.messages = ms

name = st.session_state.user.username if st.session_state.user else None
campaign_name = st.session_state.campaign.name if st.session_state.campaign else None
if name and campaign_name:
    st.markdown(f"### Hello {name}! You are playing in the {campaign_name} campaign.")
else:
    st.write("Please select a user and campaign")

for message in st.session_state.messages:
    with st.chat_message(
        name=message["sender"] if message["sender"] != "Dungeon Master" else "AI",
    ):
        st.write(f"**{message['sender']}** says to **{message['target']}**:")
        st.write(message["content"])


prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
    m = {
        "sender": st.session_state.user.username,
        "target": "All",
        "content": prompt,
    }
    print(f"Sending message: {m}")
    st.session_state.messages.append(m)
    st.experimental_rerun()
