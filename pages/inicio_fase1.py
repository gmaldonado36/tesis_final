import streamlit as st

def run():
    st.title("Inicio Fase 1")

    st.write("Bienvenidos a la primera fase.")
    st.write("Esta prueba consta de tres fases.")
    st.write("Al finalizar cada fase, podrás tomar un breve descanso si lo deseas.")
    st.write("Cuando estés listo(a) para continuar, podrás iniciar la siguiente fase haciendo clic en el botón correspondiente.")
    st.write("Después de observar cada imagen, aparecerá una escala SAM (Self-Assessment Manikin). En esta escala deberás indicar del 1 al 9 qué tanta intensidad de la emoción te generó ante la imagen presentada, donde 1 representa una intensidad emocional muy baja y 9 una intensidad emocional muy alta.")

    if st.button("Avanzar", type="primary"):
        st.session_state.fase = "fase1"
        st.rerun()