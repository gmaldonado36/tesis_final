import streamlit as st


def init_state():
    defaults = {
        "fase": "bienvenida",
        "participant_id": "",
        # Fase 1
        "imagenes_fase1": [],
        "index_fase1": 0,
        "tiempos_fase1": [],
        "escalas_fase1": [],
        # Fase 2
        "imagenes_fase2": [],
        "index_fase2": 0,
        "tiempos_fase2": [],
        "escalas_fase2": [],
        # Fase 3
        "imagenes_fase3": [],
        "index_fase3": 0,
        "tiempos_fase3": [],
        "escalas_fase3": [],
        # Generales
        "start_time": None,
        "current_image": None,
        "origen_scale": "fase1",
        # Test
        "imagenes_test": [],
        "index_test": 0,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value



