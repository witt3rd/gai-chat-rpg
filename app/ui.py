# # System # #
import requests

# # Packages # #
from pydantic.type_adapter import TypeAdapter
import streamlit as st
from streamlit_chat import message

# # Project # #
from config import get_config
from model import (
    PersonaOutput,
)

###

#
# Streamlit app
#

st.set_page_config(
    page_title="Reflector",
    page_icon="🎭",
)


#
# Server
#
def get_server() -> str:
    return f"http://{get_config().server_host}:{get_config().server_port}"


def get_personas() -> list[PersonaOutput]:
    results = requests.get(f"{get_server()}/personas")
    personas = [TypeAdapter(PersonaOutput).validate_python(p) for p in results.json()]
    print(personas)
    return personas


#
# UI
#

# Custom CSS
with open("style.css", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(
    """
<div class="header-container">
<img src="./app/static/hero.png" alt="Reflector" class="header-image">
<div class="header-text">
    <h2>Reflector</h2>
    <p>Dynamic Human Mimicry via In-Context Learning and Prompt Engineering</p>
</div>
</div>
""",
    unsafe_allow_html=True,
)

tab1, tab2 = st.tabs(["Main", "About"])

with tab1:
    st.markdown("## Chat")
    personas = get_personas()
    persona = st.selectbox("Persona", [p.name for p in personas])

with tab2:
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()
    readme = readme.replace("static/", "./app/static/")
    st.markdown(readme, unsafe_allow_html=True)
