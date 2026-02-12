import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import uuid



def write_to_google_sheets():
    try:
        # -------- DEBUG tamaños --------
        st.write("DEBUG tamaños →")
        st.write("imagenes:", len(st.session_state.get("imagenes", [])))
        st.write("tiempos:", len(st.session_state.get("tiempos", [])))
        st.write("escalas:", len(st.session_state.get("escalas", [])))

        # -------- Validación --------
        if "imagenes" not in st.session_state or len(st.session_state.imagenes) == 0:
            st.error("imagenes vacío → no se guarda")
            return

        if "run_id" not in st.session_state:
            import uuid
            st.session_state.run_id = str(uuid.uuid4())

        run_id = st.session_state.run_id

        import pandas as pd

        df = pd.DataFrame({
            "run_id": [run_id] * len(st.session_state.imagenes),
            "nombre_usuario": [st.session_state.get("nombre", "anon")] * len(st.session_state.imagenes),
            "imagen": st.session_state.imagenes,
            "tiempo_segundos": st.session_state.tiempos,
            "escala": st.session_state.escalas,
        })

        st.write("DEBUG dataframe ↓")
        st.write(df)

        # -------- Conexión --------
        client = connect_to_sheets()
        sheet = client.open(SHEET_NAME).sheet1
        st.write("DEBUG conectado a Google Sheets")

        rows = df.astype(str).values.tolist()

        if len(rows) == 0:
            st.error("No hay filas para escribir")
            return

        sheet.append_rows(rows, value_input_option="USER_ENTERED")

        st.success(f"OK → {len(rows)} filas escritas en Google Sheets")

    except Exception as e:
        st.error("ERROR REAL:")
        st.exception(e)
