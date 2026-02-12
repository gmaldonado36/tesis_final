import streamlit as st
from services.image_loader import load_random_images
from components.progress import show_progress
import os
import time
from config import PRUEBA_FOLDER


def run():
    # Inicializar session_state específico de test
    if "imagenes_test" not in st.session_state or not st.session_state.imagenes_test:
        st.session_state.imagenes_test = load_random_images(PRUEBA_FOLDER)
        st.session_state.index_test = 0
        st.session_state.tiempos_test = []
        st.session_state.start_time_test = None
        st.session_state.current_image_test = None

    # Si ya terminamos todas las imágenes
    if st.session_state.index_test >= len(st.session_state.imagenes_test):
        st.write("¡Bloque de prueba completado!")
        if st.button("Continuar a Fase 1", type="primary"):
            st.session_state.fase = "inicio_fase1"
            st.rerun()
        return

    idx = st.session_state.index_test
    img_name = st.session_state.imagenes_test[idx]
    img_path = os.path.join(PRUEBA_FOLDER, img_name)

    show_progress()

    st.image(img_path, use_container_width=True)

    if st.button("Avanzar a escala"):
        st.session_state.start_time_test = time.time()
        st.session_state.current_image_test = img_name
        st.session_state.origen_scale = "test"  # <-- CLAVE: marca el origen
        st.session_state.fase = "scale"
        st.rerun()
