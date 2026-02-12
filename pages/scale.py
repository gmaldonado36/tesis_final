import streamlit as st
from config import ESCALA_IMAGE

def run():
    st.title("Califica la imagen")

    st.image(ESCALA_IMAGE, use_container_width=True)

    escala = st.slider("Selecciona un valor", 1, 9, key="slider")

    if st.button("Avanzar"):
        st.session_state.escalas.append(escala)
        st.session_state.index += 1

        # Limpia slider para evitar widget zombie
        st.session_state.pop("slider", None)

        if st.session_state.index >= len(st.session_state.imagenes):
            st.session_state.fase = "end"
        else:
            st.session_state.fase = "fase1"

        st.rerun()
