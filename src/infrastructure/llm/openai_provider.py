from langchain_openai import ChatOpenAI
from src.infrastructure.llm.base import BaseLLMProvider


class OpenAIProvider(BaseLLMProvider):
    """ OpenAI LLM provider implementation. """
    
    def __init__(self, model_name: str = "gpt-3.5-turbo", temperature: float = 0.5) -> None:
        """ Initializes the OpenAI provider with the specified model and temperature. """
        self._llm = ChatOpenAI(model=model_name, temperature=temperature)    
        super().__init__(model_name=model_name, provider_name="openai", temperature=temperature, llm=self._llm)
        
    @property
    def provider_name(self) -> str:
        """ Returns the name of the LLM provider. """
        return self._provider_name
    