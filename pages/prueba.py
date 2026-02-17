import streamlit as st

def run():
    st.title("Inicio del Bloque de Prueba")

    st.write("A continuación, comenzará un bloque de prueba. Este bloque de prueba no formará parte de los resultados finales ")
    st.write("Cuando estés listo(a), haz clic en “Avanzar” para comenzar el bloque de prueba.")

    if st.button("Avanzar", type="primary"):
        st.session_state.fase = "test"
        st.rerun()