import streamlit as st

def run():
    st.title("Bienvenida")

    st.write("Bienvenidos a la prueba.")
    st.write("Gracias por participar en este estudio.")
    st.write("Cuando estés listo(a), haz clic en “Continuar” para seguir.")

    nombre = st.text_input("Por favor escribe tu nombreEscribe tu nombre")

    if nombre:
        st.success("Listo para comenzar")
        st.session_state.nombre = nombre
        if st.button("Avanzar"):
            st.session_state.fase = "fase1"
            st.rerun()
    else:
        st.button("Avanzar", disabled=True)
