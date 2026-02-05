import streamlit as st

def run():
    st.title("Instrucciones")

    st.write("Lee cuidadosamente estas instrucciones antes de comenzar.")
    st.write("Verás una serie de imágenes y luego deberás calificarlas.")

    nombre = st.text_input("Escribe tu nombre")

    if nombre:
        st.success("Listo para comenzar")
        st.session_state.nombre = nombre
        if st.button("Avanzar"):
            st.session_state.fase = "fase1"
            st.rerun()
    else:
        st.button("Avanzar", disabled=True)
