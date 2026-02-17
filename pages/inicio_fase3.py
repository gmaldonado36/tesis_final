import streamlit as st


def run():
    st.title("Inicio Fase 3")

    st.write("Has completado la Fase 2. ¡Ya casi terminas!")
    st.write("Si lo deseas, puedes tomar un breve descanso antes de continuar.")
    st.write("La dinámica será la misma: observarás una serie de imágenes y después de cada una calificarás la intensidad emocional que te generó usando la escala SAM (del 1 al 9).")
    st.write("Donde 1 representa una intensidad emocional muy baja y 9 una intensidad emocional muy alta.")

    if st.button("Comenzar Fase 3", type="primary"):
        st.session_state.fase = "fase3"
        st.rerun()
