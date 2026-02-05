import streamlit as st
from services.image_loader import load_random_images
from services.timer import start_timer, stop_timer
from components.progress import show_progress
import os
from config import FASE1_FOLDER

def run():

    if not st.session_state.imagenes:
        st.session_state.imagenes = load_random_images()

    if st.session_state.start_time is None:
        st.session_state.start_time = start_timer()

    idx = st.session_state.index
    img_name = st.session_state.imagenes[idx]
    img_path = os.path.join(FASE1_FOLDER, img_name)

    show_progress()
    st.image(img_path, use_container_width=True)

    if st.button("Avanzar"):
        tiempo = stop_timer(st.session_state.start_time)

        st.session_state.tiempos.append(tiempo)
        st.session_state.current_image = img_name
        st.session_state.fase = "scale"
        st.session_state.start_time = None
        st.rerun()
