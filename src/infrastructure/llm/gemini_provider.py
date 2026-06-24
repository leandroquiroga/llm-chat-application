from langchain_google_genai import ChatGoogleGenerativeAI 
from src.infrastructure.llm.base import BaseLLMProvider
from src.config.settings import settings

class GeminiProvider(BaseLLMProvider):
    """ Gemini LLM provider implementation. """
    
    def __init__(self, model_name: str = "gemini-2.5-pro", temperature: float = 0.5) -> None:
        """ Initializes the Gemini provider with the specified model and temperature. """
        self._llm = ChatGoogleGenerativeAI(model=model_name, temperature=temperature, google_api_key=settings.GOOGLE_API_KEY)
        super().__init__(model_name=model_name, provider_name="gemini", temperature=temperature, llm=self._llm)
        
    @property
    def provider_name(self) -> str:
        """ Returns the name of the LLM provider. """
        return self._provider_name