"""
Campaigns page
"""
# # # System # # #

# # # Packages # # #
import chat_rpg_client as client
import streamlit as st

# # # Project # # #
from ui.sidebar import show_sidebar

#

st.set_page_config(
    page_title="Campaign",
    page_icon="🗺️",
    # layout="wide",
    initial_sidebar_state="expanded",
)
show_sidebar()

#
# Callbacks (_before_ the state is managed, so we can make changes)
#


def create_campaign() -> None:
    campaigns_api = st.session_state.campaigns_api

    campaigns_api.create_campaign(
        campaign_create=client.CampaignCreate(
            name=st.session_state.name,
        )
    )
    del st.session_state.campaigns
    st.success("Created!")


def update_campaign() -> None:
    campaigns_api = st.session_state.campaigns_api

    campaigns_api.update_campaign(
        id=str(st.session_state.selected_campaign.id),
        campaign_update=client.CampaignUpdate(
            name=st.session_state.name,
        ),
    )
    del st.session_state.campaigns
    st.success("Updated!")


def delete_campaign() -> None:
    campaigns_api = st.session_state.campaigns_api

    campaigns_api.delete_campaign(
        id=st.session_state.selected_campaign.id,
    )
    del st.session_state.campaigns
    st.success("Deleted!")


#
# State initialization
#

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
    except client.ApiException as e:
        st.exception(f"Exception when calling CampaignsApi->get_all_campaigns: {e}\n")

#
# UI
#

st.title("🗺️ Campaign")
st.markdown("---")

campaign_names = [campaign.name for campaign in st.session_state.campaigns]

selected_campaign = st.selectbox(
    label="Select a campaign or add new",
    options=["Add new campaign"] + campaign_names,
    index=0,
    key="selected_campaign_name",
)

st.session_state.selected_campaign = None
for campaign in st.session_state.campaigns:
    if campaign.name == st.session_state.selected_campaign_name:
        st.session_state.selected_campaign = campaign
        break

st.text_input(
    label="Name",
    value=st.session_state.selected_campaign.name
    if st.session_state.selected_campaign
    else "",
    key="name",
)
col1, col2 = st.columns(2)
if st.session_state.selected_campaign:
    col1.button(
        label="Update Campaign",
        on_click=update_campaign,
        use_container_width=True,
    )
    col2.button(
        label="Delete Campaign",
        on_click=delete_campaign,
        use_container_width=True,
        type="primary",
    )
else:
    col1.button(
        label="Create Campaign",
        on_click=create_campaign,
        use_container_width=True,
    )
    col2.button(
        label="Delete Campaign",
        on_click=delete_campaign,
        use_container_width=True,
        disabled=True,
    )
