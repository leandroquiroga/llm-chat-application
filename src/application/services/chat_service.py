from typing import Generator
from src.domain.interfaces.llm_provider import LLMProvider
from src.domain.models.message import Message, ChatHistory


class ChatService:
    """ Service for managing chat interactions with the LLM provider. """
    
    def __init__(self, provider: LLMProvider) -> None:
        """ Initializes the chat service with the specified LLM provider. """
        self._provider = provider
        self._chat_history = ChatHistory()
        
    @property
    def provider(self) -> LLMProvider:
        """ Returns the LLMProvider instance used by the chat service. """
        return self._provider
    
    @provider.setter
    def provider(self, provider: LLMProvider) -> None:
        """ Sets a new LLMProvider instance for the chat service. """
        self._provider = provider
        
    @property
    def chat_history(self) -> ChatHistory:
        """ Returns the current chat history. """
        return self._chat_history

    def send_message_stream(self, user_input: str) -> Generator[str, None, None]:
        """ Sends a message to the LLM provider and yields the response. """
        full_response = ""
        for chunk in self._provider.stream(self._chat_history, user_input):
            full_response += chunk
            yield chunk
        
        self._chat_history.add_message(role="user", content=user_input)
        self._chat_history.add_message(role="assistant", content=full_response)
        
    def send_message(self, user_input: str) -> Message:
        """ Sends a message to the LLM provider and returns the response. """
        response_message = self._provider.generate(self._chat_history, user_input)
        self._chat_history.add_message(role="user", content=user_input)
        self._chat_history.add_message(role="assistant", content=response_message.content)
        return response_message
        
    def clear_history(self) -> None:
        """ Clears the chat history. """
        self._chat_history = ChatHistory()