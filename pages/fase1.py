import streamlit as st
from services.image_loader import load_random_images
from services.timer import start_timer, stop_timer
from components.progress import show_progress
import os
import time
from PIL import Image
from config import FASE1_FOLDER


def run():
    # Inicializar session_state específico de esta fase
    if "imagenes" not in st.session_state or not st.session_state.imagenes:
        st.session_state.imagenes = load_random_images(FASE1_FOLDER)
        st.session_state.index = 0
        st.session_state.tiempos = []
        st.session_state.escalas = []
        st.session_state.start_time = None
        st.session_state.current_image = None

    # Si ya terminó todas las imágenes, ir a end
    if st.session_state.index >= len(st.session_state.imagenes):
        st.session_state.fase = "end"
        st.rerun()
        return

    idx = st.session_state.index
    img_name = st.session_state.imagenes[idx]
    img_path = os.path.join(FASE1_FOLDER, img_name)

    # Iniciar timer si aún no se ha iniciado para esta imagen
    if st.session_state.start_time is None:
        st.session_state.start_time = time.time()

    # Mostrar progreso y la imagen
    show_progress()

    img = Image.open(img_path)
    img.thumbnail((900, 900))    # ← tamaño que quieras (ancho, alto)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(img, use_container_width=True)

    # Botón para avanzar
    if st.button("Avanzar"):
        tiempo = stop_timer(st.session_state.start_time)
        st.session_state.tiempos.append(tiempo)
        st.session_state.current_image = img_name
        st.session_state.origen_scale = "fase1"
        st.session_state.fase = "scale"
        st.session_state.start_time = None
        st.rerun()

