import streamlit as st
from services.excel_writer import write_to_google_sheets



def run():
    st.title("Finalizado")
    st.success("Gracias por completar el experimento")

    # Ejecutar SOLO una vez por sesión
    if not st.session_state.get("saved_to_sheets", False):
        try:
            write_to_google_sheets()
            st.session_state.saved_to_sheets = True
            st.success("Resultados guardados en Google Sheets ✅")
        except Exception as e:
            st.error("Error guardando resultados")
            st.exception(e)


