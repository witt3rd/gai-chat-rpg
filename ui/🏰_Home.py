# # System # #

# # Packages # #
import streamlit as st
from streamlit_chat import message

# # Project # #
from config import get_config

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
with open("style.css", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(
    """
<div class="header-container">
<img src="app/static/hero.jpg" alt="ChatRPG" class="header-image">
<div class="header-text">
    <h2>ChatRPG</h2>
    <p>Generative Realms: AI-driven Dungeons & Dragons</p>
</div>
</div>
""",
    unsafe_allow_html=True,
)

# tab_main, tab_char, tab_admin, tab_about = st.tabs(
#     ["Main", "Character", "Admin", "About"]
# )

# with tab_main:
#     st.markdown("## Main")

# with tab_char:
#     st.markdown("## Character")

# with tab_admin:
#     st.markdown("## Admin")

# with tab_about:
#     with open("README.md", "r", encoding="utf-8") as f:
#         readme = f.read()
#     readme = readme.replace("static/", "./app/static/")
#     st.markdown(readme, unsafe_allow_html=True)
