import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import uuid

# 🔑 PEGA AQUÍ TU SPREADSHEET ID
SPREADSHEET_ID = "1sYqw7dqVtD0eh3oHMsAz9mo2EDftWfgtEKv2FujCEHA"

# (opcional) nombre de la pestaña exacta
WORKSHEET_NAME = "Sheet1"


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
        st.write("DEBUG tamaños →")
        st.write("imagenes:", len(st.session_state.get("imagenes", [])))
        st.write("tiempos:", len(st.session_state.get("tiempos", [])))
        st.write("escalas:", len(st.session_state.get("escalas", [])))

        if "imagenes" not in st.session_state or len(st.session_state.imagenes) == 0:
            st.error("imagenes vacío → no se guarda")
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

        st.write("DEBUG dataframe ↓")
        st.write(df)

        client = connect_to_sheets()

        # 🔥 ABRE POR ID (NO POR NOMBRE)
        spreadsheet = client.open_by_key(SPREADSHEET_ID)
        st.write("Spreadsheet conectado:", spreadsheet.title)

        # 🔥 ABRE LA PESTAÑA EXACTA
        sheet = spreadsheet.worksheet(WORKSHEET_NAME)
        st.write("Escribiendo en pestaña:", sheet.title)

        rows = df.astype(str).values.tolist()

        if len(rows) == 0:
            st.error("No hay filas para escribir")
            return

        sheet.append_rows(rows, value_input_option="USER_ENTERED")

        st.success(f"OK → {len(rows)} filas escritas")

    except Exception as e:
        st.error("ERROR REAL:")
        st.exception(e)
