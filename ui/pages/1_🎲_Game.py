# # # System # # #

# # # Packages # # #

import streamlit as st
import chat_rpg_client
from chat_rpg_client.models.user_out import UserOut
from chat_rpg_client.rest import ApiException

# # # Project # # #

#

st.set_page_config(
    page_title="🎲 Game",
    page_icon="🎲",
    layout="wide",
    initial_sidebar_state="expanded",
)

if "client" not in st.session_state:
    configuration = chat_rpg_client.Configuration(
        host=get_config().server_url,
    )

    client = chat_rpg_client.ApiClient(configuration)
    st.session_state.client = client

if "users_api" not in st.session_state:
    client = st.session_state.client
    users_api = chat_rpg_client.UsersApi(client)
    st.session_state.users_api = users_api

if "users" not in st.session_state:
    try:
        # Get Users
        users_api = st.session_state.users_api
        users_list = users_api.users_users_get()
        # convert from an array of users to a dict of users keyed by name
        users_dict = {}
        for userd in users_list:
            user = UserOut.from_dict(userd)
            users_dict[user.username] = user
        st.session_state.users = users_dict
        st.write(users_dict)
    except ApiException as e:
        st.exception(
            "Exception when calling UsersApi->get_users_users_users_get: %s\n" % e
        )


campaigns = [
    "The Lost Mine of Phandelver",
]

st.selectbox(
    label="Select a user",
    options=st.session_state.users,
    index=0,
    key="user",
)

st.selectbox(
    label="Select a campaign",
    options=campaigns,
    index=0,
    key="campaign",
)


st.markdown(f"# {st.session_state.campaign} for {st.session_state.user}")
