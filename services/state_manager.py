import streamlit as st

def init_state():
    defaults = {
        "fase": "instructions",
        "nombre": "",
        "imagenes": [],
        "index": 0,
        "start_time": None,
        "tiempos": [],
        "escalas": [],
        "current_image": None,
    }

    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
