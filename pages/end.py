import streamlit as st
from services.excel_writer import write_to_google_sheets


def run():
    st.title("Finalizado")

    st.success("Gracias por completar el experimento")

    excel = write_to_google_sheets()



