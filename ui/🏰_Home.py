# # System # #

# # Packages # #
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_chat import message

# # Project # #
import chat_rpg_client as client
from ui.util.config import get_config


###

#
# Streamlit app
#

st.set_page_config(
    page_title="ChatRPG",
    page_icon="🏰",
)


#
# UI
#

# Custom CSS
with open("./ui/style.css", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(
    """
<p align="center">
  <img width="140" src="app/static/wizard.jpg" />  
  <img width="140" src="app/static/paladan.jpg" />  
  <img width="140" src="app/static/yaeger.jpg" />  
  <h2 align="center">ChatRPG</h2>
  <p align="center">🧙‍♂️ Generative Realms: AI-driven Dungeons & Dragons 🐉</p>
</p>
""",
    unsafe_allow_html=True,
)

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
