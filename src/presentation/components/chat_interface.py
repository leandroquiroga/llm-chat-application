import streamlit as st
import streamlit_shadcn_ui as ui
from src.application.services.chat_service import ChatService


def render(chat_service: ChatService) -> None:
    """Renders the main chat interface where users can input messages and view conversation history."""

    for message in chat_service.chat_history.messages:
        with st.chat_message(message.role):
            st.markdown(message.content)

    user_input = st.chat_input("Type your message here...")

    if user_input:

        with st.chat_message("user"):
            st.markdown(user_input)

        with st.spinner("Generating response..."):
            with st.chat_message("assistant"):
                placeholder = st.empty()
                full_response = ""

            try:
                for chunk in chat_service.send_message_stream(user_input):
                    full_response += str(chunk)
                    placeholder.markdown(full_response + "▌")

                placeholder.markdown(full_response)
                
                st.rerun()
            except Exception as e:
                error_msg = str(e)

                if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
                    ui.alert(title="Límite de uso alcanzado",
                            description="Cambiá de proveedor o esperá unos segundos.",
                            class_name="error", key="quota_err")

                elif "404" in error_msg and "not found" in error_msg.lower():
                    ui.alert(title="Modelo no disponible",
                            description=f"'{chat_service.provider.model_name}' no existe. Elegí otro modelo.",
                            class_name="warning", key="model_err")

                elif "API_KEY" in error_msg or "401" in error_msg or "unauthorized" in error_msg.lower():
                    ui.alert(title="Error de autenticación",
                            description="Verificá tu API key en el archivo .env",
                            class_name="error", key="auth_err")

                else:
                    # Error genérico
                    ui.alert(title="Error inesperado",
                            description=error_msg[:100] + "...",
                            class_name="warning", key="generic_err")

