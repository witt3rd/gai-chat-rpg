import streamlit as st

#

st.set_page_config(
    page_title="🎲 Game",
    page_icon="🎲",
    layout="wide",
    initial_sidebar_state="expanded",
)

campaigns = [
    "The Lost Mine of Phandelver",
]

users = [
    "Dan",
    "Donald",
    "Matt",
]

st.selectbox(
    label="Select a user",
    options=users,
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
