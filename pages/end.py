import streamlit as st
from services.excel_writer import write_to_google_sheets


def run():
    st.title("Finalizado")
    st.success("Gracias por completar el experimento")

    # Si ya se guardó → no permitir repetir
    if st.session_state.get("saved_to_sheets", False):
        st.success("Resultados guardados correctamente ✅")
        st.stop()

    st.warning("Presiona FINALIZAR para guardar tus resultados")

    if st.button("Finalizar experimento"):

        try:
            write_to_google_sheets()
            st.session_state.saved_to_sheets = True
            st.success("Datos guardados correctamente ✅")

            # Opcional: bloquear interacción futura
            st.balloons()

        except Exception as e:
            st.error("Error guardando resultados")
            st.exception(e)
