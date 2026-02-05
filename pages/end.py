import streamlit as st
from services.excel_writer import generate_excel

def run():
    st.title("Finalizado")

    st.success("Gracias por completar el experimento")

    excel = generate_excel()

    st.download_button(
        label="Descargar resultados",
        data=excel,
        file_name="resultados.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
