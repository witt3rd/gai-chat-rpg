# # System # #
from functools import lru_cache
import os

# # Packages # #
from langchain import PromptTemplate
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from loguru import logger

# # Project # #
from server.config import get_config

###


@lru_cache()
def _get_prompt(name: str) -> str:
    prompt_file = os.path.join(get_config().prompts_dir, f"{name}.txt")
    with open(prompt_file, "r", encoding="utf-8") as f:
        return f.read()


def analyze_persona(
    transcript: str,
    persona_name: str,
    persona_story: str,
) -> str:
    chat = ChatOpenAI(
        openai_api_key=get_config().openai_api_key,
        model="gpt-4",
        streaming=True,
        verbose=True,
        callbacks=[StreamingStdOutCallbackHandler()],
        temperature=0,
        max_tokens=512,
    )
    backstory_template = PromptTemplate.from_template(
        _get_prompt("persona_backstory_tmpl"),
    )
    backstory_prompt = backstory_template.format(
        persona=persona_name,
        story=persona_story,
    )

    transcript_template = PromptTemplate.from_template(
        _get_prompt("transcript_tmpl"),
    )
    transcript_prompt = transcript_template.format(
        transcript=transcript,
    )

    analyze_persona_template = PromptTemplate.from_template(
        _get_prompt("analyze_persona_tmpl"),
    )
    analysis_prompt = analyze_persona_template.format(
        persona=persona_name,
    )

    messages = [
        SystemMessage(content=_get_prompt("system_mimcry")),
        HumanMessage(content=backstory_prompt),
        HumanMessage(content=transcript_prompt),
        HumanMessage(content=analysis_prompt),
    ]
    response = chat(messages=messages)
    analysis = response.content
    logger.info(f"Analysis of {persona_name}: {analysis}")
    return analysis
