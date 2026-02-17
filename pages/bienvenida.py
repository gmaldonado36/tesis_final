import streamlit as st

def run():
    st.title("Bienvenida")

    st.write("Bienvenidos a la prueba.")
    st.write("Gracias por participar en este estudio.")
    st.write("Cuando estés **listo(a)**, haz clic en **“Avanzar”** para seguir.")

    nombre = st.text_input("Por favor escribe tu nombre")

    if nombre:
        st.session_state.nombre = nombre
        st.success("Listo para comenzar")
        if st.button("Avanzar"):
            st.session_state.fase = "instrucciones"
            st.rerun()
    else:
        st.button("Avanzar", disabled=True)