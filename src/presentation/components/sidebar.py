import streamlit as st
import streamlit_shadcn_ui as ui
from src.application.services.chat_service import ChatService
from src.infrastructure.llm.factory import ProviderFactory
from src.constants.constants import PROVIDER_LABELS, PROVIDER_MODELS


def render(chat_service: ChatService) -> None:
    with st.sidebar:
        st.markdown("## Configuration")

        selected_provider = ui.select(
            label="LLM Provider", options=PROVIDER_LABELS, key="provider_select"
        )
        model_options = PROVIDER_MODELS.get(selected_provider.lower(), [])
        selected_model = ui.select(
            label="Model", options=model_options, key=f"model_{selected_provider.lower()}"
        )

        temperature = st.slider(
            label="Temperature", min_value=0.0, max_value=1.0,
            value=0.5, step=0.1, key="temperature_slider",
        )

        if (
            temperature != st.session_state.get("prev_temp")
            or selected_provider != st.session_state.get("prev_provider")
            or selected_model != st.session_state.get("prev_model")
        ):
            chat_service.provider = ProviderFactory.create(
                provider_type=selected_provider.lower(),
                model_name=selected_model,
                temperature=temperature,
            )
            st.session_state["prev_temp"] = temperature
            st.session_state["prev_provider"] = selected_provider
            st.session_state["prev_model"] = selected_model

        st.divider()

        if ui.button(text="New Conversation", variant="default", key="new_conversation"):
            chat_service.clear_history()
            st.rerun()