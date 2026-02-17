import streamlit as st
from pages import bienvenida, instrucciones, prueba, test, fase1, fase2, fase3, scale, end, inicio_fase1, inicio_fase2, inicio_fase3
from services.state_manager import init_state

st.set_page_config(layout="centered")

init_state()

fase = st.session_state.fase

if fase == "bienvenida":
    bienvenida.run()
elif fase == "instrucciones":
    instrucciones.run()
elif fase == "prueba":
    prueba.run()
elif fase == "test":
    test.run()
elif fase == "inicio_fase1":
    inicio_fase1.run()
elif fase == "fase1":
    fase1.run()
elif fase == "scale":
    scale.run()
elif fase == "inicio_fase2":
    inicio_fase2.run()
elif fase == "fase2":
    fase2.run()
elif fase == "inicio_fase3":
    inicio_fase3.run()
elif fase == "fase3":
    fase3.run()
elif fase == "end":
    end.run()


   