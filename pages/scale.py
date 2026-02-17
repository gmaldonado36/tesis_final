import streamlit as st
from config import ESCALA_IMAGE


def run():
    st.title("Califica la imagen")
    st.write("¿Qué tanta emoción te generó la imagen que acabas de ver?")

    st.image(ESCALA_IMAGE, use_container_width=True)

    escala = st.slider("Selecciona un valor", 1, 9, key="slider")

    origen = st.session_state.get("origen_scale", "fase1")

    if st.button("Avanzar"):
        slider_val = st.session_state.pop("slider", escala)

        if origen == "test":
            st.session_state.index_test += 1
            if st.session_state.index_test >= len(st.session_state.imagenes_test):
                st.session_state.fase = "inicio_fase1"
            else:
                st.session_state.fase = "test"

        elif origen == "fase1":
            st.session_state.escalas_fase1.append(slider_val)
            st.session_state.index_fase1 += 1
            if st.session_state.index_fase1 >= len(st.session_state.imagenes_fase1):
                st.session_state.fase = "inicio_fase2"
            else:
                st.session_state.fase = "fase1"

        elif origen == "fase2":
            st.session_state.escalas_fase2.append(slider_val)
            st.session_state.index_fase2 += 1
            if st.session_state.index_fase2 >= len(st.session_state.imagenes_fase2):
                st.session_state.fase = "inicio_fase3"
            else:
                st.session_state.fase = "fase2"

        elif origen == "fase3":
            st.session_state.escalas_fase3.append(slider_val)
            st.session_state.index_fase3 += 1
            if st.session_state.index_fase3 >= len(st.session_state.imagenes_fase3):
                st.session_state.fase = "end"
            else:
                st.session_state.fase = "fase3"

        st.rerun()



  
