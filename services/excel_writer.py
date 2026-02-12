import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import uuid

# 🔑 ID DEL SPREADSHEET (de la URL)
SPREADSHEET_ID = "1sYqw7dqVtD0eh3oHMsAz9mo2EDftWfgtEKv2FujCEHA"

# 📄 Nombre de la pestaña donde guardar
WORKSHEET_NAME = "database"


# ---------- CONEXIÓN ----------
@st.cache_resource
def connect_to_sheets():
    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ],
    )
    return gspread.authorize(creds)


# ---------- WRITE ----------
def write_to_google_sheets():
    try:
        # Validación mínima
        if "imagenes" not in st.session_state or len(st.session_state.imagenes) == 0:
            return

        if "run_id" not in st.session_state:
            st.session_state.run_id = str(uuid.uuid4())

        run_id = st.session_state.run_id

        df = pd.DataFrame({
            "run_id": [run_id] * len(st.session_state.imagenes),
            "nombre_usuario": [st.session_state.get("nombre", "anon")] * len(st.session_state.imagenes),
            "imagen": st.session_state.imagenes,
            "tiempo_segundos": st.session_state.tiempos,
            "escala": st.session_state.escalas,
        })

        client = connect_to_sheets()
        spreadsheet = client.open_by_key(SPREADSHEET_ID)

        # 🔥 Intenta abrir la pestaña, si no existe la crea
        try:
            sheet = spreadsheet.worksheet(WORKSHEET_NAME)
        except gspread.exceptions.WorksheetNotFound:
            sheet = spreadsheet.add_worksheet(title=WORKSHEET_NAME, rows="1000", cols="20")

            # Headers automáticos
            sheet.append_row([
                "run_id",
                "nombre_usuario",
                "imagen",
                "tiempo_segundos",
                "escala",
            ])

        rows = df.astype(str).values.tolist()

        if len(rows) == 0:
            return

        sheet.append_rows(rows, value_input_option="USER_ENTERED")

    except Exception as e:
        # En producción no mostramos detalles, pero evitamos crash
        st.error("No se pudieron guardar los resultados.")
