import streamlit as st
from services.excel_writer import write_to_google_sheets


def run():
    st.title("Finalizado")
    st.success("Gracias por completar el experimento")

    if "saved_to_sheets" not in st.session_state:
        st.session_state.saved_to_sheets = False

    if not st.session_state.saved_to_sheets:

        if st.button("Finalizar experimento", type="primary"):

            with st.spinner("Guardando resultados..."):

                try:
                    write_to_google_sheets()
                    st.session_state.saved_to_sheets = True
                    st.success("Resultados guardados correctamente ✅")
                    st.rerun()

                except Exception as e:
                    st.error("Error guardando resultados")
                    st.exception(e)

    else:
        st.info("Resultados ya guardados 👍")
