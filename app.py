import streamlit as st
from pages import bienvenida, scale, end, instrucciones, fase1

from services.state_manager import init_state

st.set_page_config(layout="centered")

init_state()

fase = st.session_state.fase

if fase == "bienvenida":
    bienvenida.run()
elif fase == "instrucciones":
    instrucciones.run()
elif fase == "fase1":
    fase1.run()
elif fase == "scale":
    scale.run()
elif fase == "end":
    end.run()
