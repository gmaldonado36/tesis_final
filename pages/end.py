import streamlit as st
from services.excel_writer import write_to_google_sheets


def run():
    st.title("Finalizado")
    st.success("Gracias por completar el experimento")

    if "saved_to_sheets" not in st.session_state:
        st.session_state.saved_to_sheets = False

    # 🔥 GUARDA AUTOMÁTICAMENTE
    if not st.session_state.saved_to_sheets:
        st.write("Guardando automáticamente...")
        write_to_google_sheets()
        st.session_state.saved_to_sheets = True
        st.success("Resultados guardados correctamente ✅")

    st.info("Puedes cerrar esta página con seguridad")
