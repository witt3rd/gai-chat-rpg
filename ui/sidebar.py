"""
Common sidebar elements
"""
# # System # #

# # Packages # #
import chat_rpg_client as client
import streamlit as st

# import streamlit_authenticator as stauth

# # Project # #
from ui.config import get_config

###


def show_sidebar() -> None:
    #
    # State initialization
    #

    if "server_url" not in st.session_state:
        st.session_state.server_url = get_config().server_url

    if "server_socket" not in st.session_state:
        st.session_state.server_socket = get_config().server_socket

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
            st.exception(
                f"Exception when calling CampaignsApi->get_all_campaigns: {e}\n"
            )

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

    server_url = st.sidebar.text_input(
        label="Server URL",
        value=st.session_state.server_url,
    )
    if server_url:
        st.session_state.server_url = server_url

    server_socket = st.sidebar.text_input(
        label="Server Socket",
        value=st.session_state.server_socket,
    )
    if server_socket:
        st.session_state.server_socket = server_socket

    st.sidebar.selectbox(
        label="Select a user",
        options=st.session_state.users,
        index=0,
        key="user",
        format_func=lambda user: user.username,
    )

    st.sidebar.button(
        "Logout",
        disabled=True,
    )

    if not st.session_state.user:
        st.stop()


# Login

# if "client" not in st.session_state:
#     configuration = chat_rpg_client.Configuration(
#         host=get_config().server_url,
#     )

#     client = chat_rpg_client.ApiClient(configuration)
#     st.session_state.client = client

# if "users_api" not in st.session_state:
#     client = st.session_state.client
#     users_api = chat_rpg_client.UsersApi(client)
#     st.session_state.users_api = users_api

# if "users" not in st.session_state:
#     try:
#         # Get Users
#         users_api = st.session_state.users_api
#         users_list = users_api.users_users_get()
#         # convert from an array of users to a dict of users keyed by name
#         users_dict = {}
#         for userd in users_list:
#             user = UserOut.from_dict(userd)
#             users_dict[user.username] = user
#         st.session_state.users = users_dict
#         st.write(users_dict)
#     except ApiException as e:
#         st.exception(
#             "Exception when calling UsersApi->get_users_users_users_get: %s\n" % e
#         )

# authenticator = stauth.Authenticate(
#     credentials={"usernames": st.session_state.users},
#     cookie_name=get_config().cookie_name,
#     key=get_config().cookie_key,
#     cookie_expiry_days=get_config().cookie_expiry_days,
#     #     config['credentials'],
#     #     config['cookie']['name'],
#     #     config['cookie']['key'],
#     #     config['cookie']['expiry_days'],
#     #     config['preauthorized']
# )

# if st.session_state["authentication_status"] is None:
#     with st.sidebar:
#         col1, col2 = st.columns(2)
#         with col1:
#             if st.button("Login", use_container_width=True):
#                 st.warning("Please enter your username and password")
#                 authenticator.login("Login", "main")

#         with col2:
#             if st.button("Register", use_container_width=True):
#                 st.warning("Please enter your details")


# if st.session_state["authentication_status"]:
#     authenticator.logout("Logout", "main", key="unique_key")
#     st.write(f'Welcome *{st.session_state["name"]}*')
#     st.title("Some content")
# elif st.session_state["authentication_status"] is False:
#     st.error("Username/password is incorrect")

# if st.session_state["authentication_status"]:
#     try:
#         if authenticator.register_user("Register user", preauthorization=False):
#             st.success("User registered successfully")
#     except Exception as e:
#         st.error(e)

# if st.session_state["authentication_status"]:
#     try:
#         (
#             username_of_forgotten_password,
#             email_of_forgotten_password,
#             new_random_password,
#         ) = authenticator.forgot_password("Forgot password")
#         if username_of_forgotten_password:
#             st.success("New password to be sent securely")
#             # Random password should be transferred to user securely
#         else:
#             st.error("Username not found")
#     except Exception as e:
#         st.error(e)

# if st.session_state["authentication_status"]:
#     try:
#         if authenticator.reset_password("witt3rd", "Reset password"):
#             st.success("Password modified successfully")
#     except Exception as e:
#         st.error(e)

# if st.session_state["authentication_status"]:
#     try:
#         if authenticator.update_user_details(username, "Update user details"):
#             st.success("Entries updated successfully")
#     except Exception as e:
#         st.error(e)
