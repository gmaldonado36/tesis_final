
import streamlit as st
from config import TOTAL_IMAGES


def show_progress():
    idx = st.session_state.index
    progress = min(idx / TOTAL_IMAGES, 1.0)
    st.progress(progress)
    st.write(f"Imagen {min(idx+1, TOTAL_IMAGES)} de {TOTAL_IMAGES}")
