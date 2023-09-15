"""
AI helpers
"""
# # # System # # #

# # # Packages # # #
from langchain.agents import ConversationalChatAgent, load_tools, AgentExecutor
from langchain.callbacks import StreamlitCallbackHandler, get_openai_callback
from langchain.chat_models import ChatOpenAI
from langchain.chat_models.base import BaseChatModel
from langchain.llms import OpenAI
from langchain.memory import ChatMessageHistory
from langchain.schema import (
    BaseMemory,
    HumanMessage,
    OutputParserException,
)
from langchain.schema.language_model import BaseLanguageModel

# # # Project # # #
from ui.config import get_config


def get_chat_model() -> BaseChatModel:
    chat_model = ChatOpenAI(
        model="gpt-4",
        temperature=0,
        verbose=True,
        streaming=True,
        openai_api_key=get_config().openai_api_key,
    )
    return chat_model


def ask_gpt(
    chat_model: BaseChatModel,
    message: str,
) -> str:
    """
    Ask the GPT model a question and return the response.
    """
    messages = [
        HumanMessage(
            content=message,
        )
    ]
    response = chat_model(messages)
    return response.content
