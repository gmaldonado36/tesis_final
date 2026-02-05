import streamlit as st

def next_button(enabled, label="Avanzar"):
    return st.button(label, disabled=not enabled)
