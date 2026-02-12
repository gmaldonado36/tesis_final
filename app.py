import streamlit as st
from pages import bienvenida, instrucciones, prueba, test, fase1, scale, end, inicio_fase1
from services.state_manager import init_state

st.set_page_config(layout="centered")

# Inicializa session_state
init_state()

fase = st.session_state.fase

if fase == "bienvenida": # Pantalla de bienvenida
    bienvenida.run()
elif fase == "instrucciones": # Pantalla de instrucciones
    instrucciones.run()
elif fase == "prueba": # Explicación del bloque de prueba
    prueba.run()
elif fase =="test": # Bloque de prueba
    test.run()
elif fase == "inicio_fase1":
    inicio_fase1.run()
elif fase == "fase1": # Primera fase del experimento
    fase1.run()
elif fase == "scale":
    scale.run()
elif fase == "end":
    end.run()
   