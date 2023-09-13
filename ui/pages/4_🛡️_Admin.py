# # # System # # #

# # # Packages # # #
import chat_rpg_client as client
import streamlit as st

# # # Project # # #
from ui.util.config import get_config

#

st.set_page_config(
    page_title="🛡️ Admin",
    page_icon="🛡️",
    # layout="wide",
    initial_sidebar_state="expanded",
)


#
# Callbacks (_before_ the state is managed, so we can make changes)
#


def create_user() -> None:
    users_api = st.session_state.users_api

    users_api.create_user(
        user_signup=client.UserSignup(
            username=st.session_state.username,
            name=st.session_state.name,
            email=st.session_state.email,
            password=st.session_state.password,
            is_admin=st.session_state.is_admin,
        )
    )
    del st.session_state.users
    st.success("Created!")


def update_user() -> None:
    users_api = st.session_state.users_api

    users_api.update_user(
        id=st.session_state.selected_user.id,
        user_in=client.UserIn(
            username=st.session_state.username,
            name=st.session_state.name,
            email=st.session_state.email,
            password=st.session_state.password,
            is_admin=st.session_state.is_admin,
        ),
    )
    del st.session_state.users
    st.success("Updated!")


def delete_user() -> None:
    users_api = st.session_state.users_api

    users_api.delete_user(
        id=st.session_state.selected_user.id,
    )
    del st.session_state.users
    st.success("Deleted!")


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

st.title("🛡️ Admin")

# st.header("Users")
with st.expander("🧙 Users", expanded=True):
    usernames = [user.username for user in st.session_state.users]

    selected_user = st.selectbox(
        label="Select a user or add new",
        options=["Add new user"] + usernames,
        index=0,
        key="selected_username",
    )

    st.session_state.selected_user = None
    for user in st.session_state.users:
        if user.username == st.session_state.selected_username:
            st.session_state.selected_user = user
            break

    st.text_input(
        label="Username",
        value=st.session_state.selected_user.username
        if st.session_state.selected_user
        else "",
        key="username",
    )
    st.text_input(
        label="Name",
        value=st.session_state.selected_user.name
        if st.session_state.selected_user
        else "",
        key="name",
    )
    st.text_input(
        label="Email",
        value=st.session_state.selected_user.email
        if st.session_state.selected_user
        else "",
        key="email",
    )
    st.text_input(
        label="Password",
        value=st.session_state.selected_user.password
        if st.session_state.selected_user
        else "",
        key="password",
        type="password",
    )
    st.checkbox(
        label="Is Admin?",
        value=st.session_state.selected_user.is_admin
        if st.session_state.selected_user
        else False,
        key="is_admin",
    )
    col1, col2 = st.columns(2)
    if st.session_state.selected_user:
        col1.button(
            label="Update User",
            on_click=update_user,
            use_container_width=True,
        )
        col2.button(
            label="Delete User",
            on_click=delete_user,
            use_container_width=True,
            type="primary",
        )
    else:
        col1.button(
            label="Create User",
            on_click=create_user,
            use_container_width=True,
        )
        col2.button(
            label="Delete User",
            on_click=delete_user,
            use_container_width=True,
            disabled=True,
        )
