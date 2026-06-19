from abc import ABC, abstractmethod
from typing import Generator
from src.domain.models.message import Message, ChatHistory

class LLMProvider(ABC):
    @abstractmethod
    def generate(self, chat_history: ChatHistory, user_input: str) -> Message:
        pass

    @abstractmethod
    def stream(self, chat_history: ChatHistory, user_input: str) -> Generator[str, None, None]:
        pass

    @property
    @abstractmethod
    def model_name(self) -> str:
        pass

    @property
    @abstractmethod
    def provider_name(self) -> str:
        pass
