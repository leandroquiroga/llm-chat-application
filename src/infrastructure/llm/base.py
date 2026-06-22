from typing import Generator
from src.domain.models.message import ChatHistory
from src.domain.interfaces.llm_provider import LLMProvider
from langchain_core.prompts import PromptTemplate
from src.domain.models.message import Message 
from src.constants.constants import SYSTEM_PROMPT

class BaseLLMProvider(LLMProvider):
    """ Base class for LLM providers. """
    
    def __init__(self, model_name: str, provider_name: str, temperature: float, llm) -> None:
        self._model_name = model_name
        self._provider_name = provider_name
        self._temperature = temperature
        self._llm = llm
        
    @property
    def model_name(self) -> str:
        """ Returns the name of the LLM model being used. """
        return self._model_name
    
    
    @property
    def temperature(self) -> float:
        """ Returns the temperature setting for the LLM. """
        return self._temperature
    
    def _build_prompt_context(self, chat_history: ChatHistory, user_input: str) -> dict:
        """ Builds the prompt context for the LLM based on the chat history and user input. """
        history_lines = []
        for message in chat_history.messages:
            role = "user" if message.role == "user" else "assistant"
            history_lines.append(f"{role}: {message.content}")
        return {
            "chat_history": "\n".join(history_lines),
            "messages": user_input
        }
        
    def generate(self, chat_history: ChatHistory, user_input: str) -> Message:
        """ Generates from the LLM based on the chat history and user input. """
        prompt = PromptTemplate.from_template(SYSTEM_PROMPT)
        chain = prompt | self._llm
        response = chain.invoke(self._build_prompt_context(chat_history, user_input))
        print(f"response: {response}")
        return Message(role="assistant", content=str(response.content))
    
    def stream(self, chat_history: ChatHistory, user_input: str) -> Generator[str, None, None]:
        """ Streams from the LLM based on the chat history and user input. """
        prompt = PromptTemplate.from_template(SYSTEM_PROMPT)
        chain = prompt | self._llm
        for chunk in chain.stream(self._build_prompt_context(chat_history, user_input)):
            yield str(chunk.content)