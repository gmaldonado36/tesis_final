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
    if "imagenes_fase1" not in st.session_state or not st.session_state.imagenes_fase1:
        st.session_state.imagenes_fase1 = load_random_images(FASE1_FOLDER)
        st.session_state.index_fase1 = 0
        st.session_state.tiempos_fase1 = []
        st.session_state.escalas_fase1 = []
        st.session_state.start_time = None

    # Si ya terminó todas las imágenes, ir a fase 2
    if st.session_state.index_fase1 >= len(st.session_state.imagenes_fase1):
        st.session_state.fase = "inicio_fase2"
        st.rerun()
        return

    idx = st.session_state.index_fase1
    img_name = st.session_state.imagenes_fase1[idx]
    img_path = os.path.join(FASE1_FOLDER, img_name)

    # Iniciar timer si aún no se ha iniciado para esta imagen
    if st.session_state.start_time is None:
        st.session_state.start_time = time.time()

    # Mostrar progreso y la imagen
    total = len(st.session_state.imagenes_fase1)
    current = st.session_state.index_fase1
    st.progress((current) / total, text=f"Imagen {current + 1} de {total}")

    img = Image.open(img_path)
    img.thumbnail((900, 900))
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(img, use_container_width=True)

    if st.button("Avanzar"):
        tiempo = stop_timer(st.session_state.start_time)
        st.session_state.tiempos_fase1.append(tiempo)
        st.session_state.current_image = img_name
        st.session_state.origen_scale = "fase1"
        st.session_state.fase = "scale"
        st.session_state.start_time = None
        st.rerun()


