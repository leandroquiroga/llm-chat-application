import streamlit as st
import streamlit_shadcn_ui as ui
from src.presentation.pages.chat_page import render as render_chat_page


st.set_page_config(page_title="LLM Chat App", page_icon="💬", layout="wide")

st.markdown("""
        <div style='text-align: center; padding: 1rem; margin-bottom: 1rem;'>
            <h1>💬 LLM Chat Application</h1>
            <p style='color: gray;'>Welcome! Configure your model in the sidebar and start chatting.</p>
        </div>
        """, unsafe_allow_html=True
)

render_chat_page()
