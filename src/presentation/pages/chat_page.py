import streamlit as st
from src.application.services.chat_service import ChatService
from src.infrastructure.llm.factory import ProviderFactory
from src.presentation.components.sidebar import render as render_sidebar
from src.presentation.components.chat_interface import render as render_chat_interface
from src.config.settings import settings
from src.constants.constants import COLORS


def render() -> None:
    """ Main function to render the chat page, including the sidebar and chat interface. """
    
    if "chat_service" not in st.session_state:
        provider = ProviderFactory.create(provider_type=settings.LLM_PROVIDER, model_name=settings.LLM_PROVIDER , temperature=settings.TEMPERATURE_DEFAULT)
        st.session_state.chat_service = ChatService(provider=provider)
        
        
    chat_service: ChatService = st.session_state.chat_service
    
    provider = chat_service.provider.provider_name
    model = chat_service.provider.model_name
    color = COLORS.get(provider, "⚪")
    st.markdown(
        f"{color} **{provider.upper()}** · `{model}`"
    )
    render_sidebar(chat_service)
    render_chat_interface(chat_service)