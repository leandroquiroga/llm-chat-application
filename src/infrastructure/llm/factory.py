from src.infrastructure.llm.openai_provider import OpenAIProvider
from src.infrastructure.llm.gemini_provider import GeminiProvider
from src.infrastructure.llm.base import BaseLLMProvider

class ProviderFactory:
    """ Factory for creating LLM provider instances. """
    
    _providers = {
        "openai": OpenAIProvider,
        "gemini": GeminiProvider
    }
    
    @classmethod
    def create(cls, provider_type: str, model_name: str, temperature: float) -> BaseLLMProvider:
        """ Creates an instance of the specified LLM provider. """
        
        if provider_type not in cls._providers:
            raise ValueError(f"Unsupported provider type: {provider_type}. Available providers: {list(cls._providers.keys())}")
        
        provider_class = cls._providers[provider_type]
        return provider_class(model_name=model_name, temperature=temperature)
        
