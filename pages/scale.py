import streamlit as st
from config import ESCALA_IMAGE


def run():
    st.title("Califica la imagen")
    st.write("¿Qué tanta emoción te generó la imagen que acabas de ver?")

    st.image(ESCALA_IMAGE, use_container_width=True)

    escala = st.slider("Selecciona un valor", 1, 9, key="slider")

    origen = st.session_state.get("origen_scale", "fase1")

    if st.button("Avanzar"):
        # Limpia slider para evitar widget zombie
        slider_val = st.session_state.pop("slider", escala)

        if origen == "test":
            # Bloque de prueba: NO guardar datos, solo avanzar
            st.session_state.index_test += 1

            if st.session_state.index_test >= len(st.session_state.imagenes_test):
                st.session_state.fase = "inicio_fase1"
            else:
                st.session_state.fase = "test"

        elif origen == "fase1":
            # Fase 1: SÍ guardar datos
            st.session_state.escalas.append(slider_val)
            st.session_state.index += 1

            if st.session_state.index >= len(st.session_state.imagenes):
                st.session_state.fase = "end"
            else:
                st.session_state.fase = "fase1"

        st.rerun()

