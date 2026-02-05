import streamlit as st
from config import TOTAL_IMAGES

def show_progress():
    idx = st.session_state.index
    st.progress(idx / TOTAL_IMAGES)
    st.write(f"Imagen {idx+1} de {TOTAL_IMAGES}")
