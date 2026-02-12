import streamlit as st
from services.excel_writer import write_to_google_sheets


def run():
    st.title("Finalizado")
    st.success("Gracias por completar el experimento")

    # Limpia cualquier widget previo (muy importante)
    st.session_state.pop("slider", None)

    # Botón explícito de finalización
    if st.button("Finalizar experimento", type="primary"):

        # Evita doble ejecución
        if not st.session_state.get("saved_to_sheets", False):
            try:
                write_to_google_sheets()
                st.session_state.saved_to_sheets = True
                st.success("Resultados guardados correctamente ✅")
            except Exception as e:
                st.error("Error guardando resultados")
                st.exception(e)

        st.stop()  # corta cualquier rerun
