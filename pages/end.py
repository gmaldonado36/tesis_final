import streamlit as st
from services.excel_writer import write_to_google_sheets


def run():
    st.title("Finalizado")
    st.success("Gracias por completar el experimento")

    # Evitar que se escriba múltiples veces
    if "saved_to_sheets" not in st.session_state:
        write_to_google_sheets()
        st.session_state.saved_to_sheets = True
        st.success("Resultados guardados en Google Sheets ✅")



