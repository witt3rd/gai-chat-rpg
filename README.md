<p align="center">
  <img width="140" src="ui/static/hero.jpg" />  
  <h2 align="center">ChatRPG</h2>
  <p align="center">🧙‍♂️ Generative Realms: AI-driven Dungeons & Dragons 🐉</p>
</p>
<p align="center">
  <a href="https://github.com/witt3rd/gai-chat-rpg/issues">
    <img src="https://img.shields.io/github/issues/witt3rd/gai-chat-rpg"/> 
  </a>
  <a href="https://github.com/witt3rd/gai-chat-rpg/network/members">
    <img src="https://img.shields.io/github/forks/witt3rd/gai-chat-rpg"/> 
  </a>  
  <a href="https://github.com/witt3rd/gai-chat-rpg/stargazers">
    <img src="https://img.shields.io/github/stars/witt3rd/gai-chat-rpg"/> 
  </a>
    <a href="https://github.com/witt3rd/gai-chat-rpg/">
    <img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg"/> 
  </a>
<p align="center">
  You can use this service for free. Sponsorship helps ❤️
</p>
<p align="center">
  <a href="https://github.com/sponsors/witt3rd">
    <img src="https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=ff69b4"/> 
  </a>
</p>
<p align="center">
  </a>
    <a href="https://twitter.com/intent/tweet?url=https%3A%2F%2Fgithub.com%2Fwitt3rd%2Fgai-chat-rpg&text=Check%20out%20AI-assisted%20Dungeons%20%26%20Dragons%3A%20ChatRPG">
    <img src="https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fwitt3rd%2Fgai-chat-rpg"/>     
  </a>
</p>
</p>

## Technology Stack

- Frontend UI: [Streamlit](https://docs.streamlit.io/) ([multipage](https://docs.streamlit.io/library/get-started/multipage-apps))
  - [API client code generator from OpenAPI spec](https://github.com/mom1/apiclient-pydantic-generator)
- Backend: FastAPI
  - Routes: `./routes` for thin REST endpoints
  - Models: `./models` ([Beanie ODM](https://beanie-odm.dev/) + [Pydantic](https://docs.pydantic.dev/latest/)) for MongoDB and OpenAPI interactions
  - Services: `./services` for the application logic separate from the routes
- Database: [MongoDB](https://www.mongodb.com/docs/manual/installation/)
  - [VS Code extension](https://www.mongodb.com/docs/mongodb-vscode/)

## Application Description

A multi-page application used as a platform for AI-assisted games of Dungeons & Dragons following the standard 5e rule set.

### Pages

- **Home**: Entry point of the application.
- **Game**: Represents an ongoing campaign with a multimedia chat interface. The game is enhanced by dynamically generated images based on text descriptions of the setting.
- **Adventurer**: A player's page, where they can manage their characters.
- **Campaigns**: Displays all available campaigns. Each campaign consists of parties of characters and a Dungeon Master (DM). A player assumes the role of DM to control and moderate a campaign.
- **Admin**: Accessible only to authenticated administrators. Supports user management functionalities and system configurations.

### Key Features

- **Authentication**: New users can signup and authenticate. Once authenticated, users gain access to the system.
- **Administrative Tools**: Administrators can manage users and control system-wide settings, such as activating new chat commands.
- **Multi-Character Management**: Players can create and manage multiple standard D&D characters.
- **Campaign Management**: Campaigns encompassing parties of characters and a DM can be created and managed.
- **Command Interface**: Chat features extensible command-based interactions. Users can perform special operations like asking rule clarifications with "/help" command.
- **Private Chat**: Users can initiate private chats with one or more users. A history of chat exchanges in a conversation is maintained and accessible anytime.
- **Dynamically Generated Images**: Text descriptions can generate images with a backend FastAPI service, enhancing game immersion.

### Persistence

Character data, campaign details, chat histories, and other relevant state data will be persisted across users and sessions in a MongoDB database.

### Future Considerations

- A plugin system to add new chat commands.
- Advanced game details persistence like character experiences and encounter histories.
- An integration service that exposes a function to accept a text description and returns an image URL for UI display based on dynamically generated images.

## Setup

### Configuration

Create a copy of `.env.template` named `.env` and fill in the required values (e.g., `OPENAI_API_KEY`). Do this for both `/server` and `/ui` directories.

### Dependencies

Create and activate a fresh Python virtual environment, then run:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Running Locally

You can use the scripts to start each of the server (`./run_srv.sh`) and UI (`./run_ui.sh`).

### Deployment

@TODO
