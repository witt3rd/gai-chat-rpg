"""
Main application page
"""
# # System # #

# # Packages # #
import streamlit as st

# # Project # #
from ui.sidebar import show_sidebar

###

#
# Streamlit app
#

st.set_page_config(
    page_title="ChatRPG",
    page_icon="🏰",
)
show_sidebar()

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

# if __name__ == "__main__":
#     print("Home page")
