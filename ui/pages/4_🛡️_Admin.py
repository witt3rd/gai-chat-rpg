# # # System # # #

# # # Packages # # #

import streamlit as st
import chat_rpg_client
from chat_rpg_client.models.user_out import UserOut
from chat_rpg_client.rest import ApiException

# # # Project # # #
from ui.config import get_config

#

st.set_page_config(
    page_title="🛡️ Admin",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

if "client" not in st.session_state:
    configuration = chat_rpg_client.Configuration(
        host=get_config().server_url,
    )
    client = chat_rpg_client.ApiClient(
        configuration=configuration,
        header_name="User-Agent",
        header_value="chat-rpg-client",
    )
    st.session_state.client = client

if "users_api" not in st.session_state:
    client = st.session_state.client
    users_api = chat_rpg_client.UsersApi(
        api_client=client,
    )
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

st.selectbox(
    label="Select a user",
    options=st.session_state.users,
    index=0,
    key="user",
)

with st.form(key="create_user") as form:
    st.header("Create User")

    st.text_input(label="Username", key="username")
    st.text_input(label="Name", key="name")
    st.text_input(label="Email", key="email")
    st.text_input(label="Password", key="password", type="password")

    if st.form_submit_button(label="Create User"):
        users_api = st.session_state.users_api

        users_api.user_users_post(
            user_signup=chat_rpg_client.UserSignup(
                username=st.session_state.username,
                name=st.session_state.name,
                email=st.session_state.email,
                password=st.session_state.password,
            )
        )

        st.success("Created!")
