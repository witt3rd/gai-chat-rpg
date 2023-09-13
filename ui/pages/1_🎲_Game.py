# # # System # # #

# # # Packages # # #
import chat_rpg_client as client
import streamlit as st

# # # Project # # #
from ui.util.config import get_config

#

st.set_page_config(
    page_title="🎲 Game",
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
        host=get_config().server_url,
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
        users = [client.UserOut(**user) for user in users_api.get_all_users()]
        print(f"{users}")
        st.session_state.users = users
    except client.ApiException as e:
        st.exception(
            "Exception when calling UsersApi->get_users_users_users_get: %s\n" % e
        )

#
# UI
#

st.title("🎲 Game")

st.header("Campaigns")


campaigns = [
    "The Lost Mine of Phandelver",
]

st.selectbox(
    label="Select a user",
    options=st.session_state.users,
    index=0,
    key="user",
    format_func=lambda user: user.username,
)

st.selectbox(
    label="Select a campaign",
    options=campaigns,
    index=0,
    key="campaign",
)


st.markdown(f"# {st.session_state.campaign} for {st.session_state.user.name}")
