import pandas as pd
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import uuid

SHEET_NAME = "DataTesis"


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

    # Validación básica
    if "imagenes" not in st.session_state or len(st.session_state.imagenes) == 0:
        return

    # 🔒 ID ÚNICO ESTABLE POR SESIÓN
    if "run_id" not in st.session_state:
        st.session_state.run_id = str(uuid.uuid4())

    run_id = st.session_state.run_id

    data = {
        "run_id": [run_id] * len(st.session_state.imagenes),
        "nombre_usuario": [st.session_state.nombre] * len(st.session_state.imagenes),
        "imagen": st.session_state.imagenes,
        "tiempo_segundos": st.session_state.tiempos,
        "escala": st.session_state.escalas,
    }

    df = pd.DataFrame(data)

    client = connect_to_sheets()
    sheet = client.open(SHEET_NAME).sheet1

    # 🔍 Leer IDs existentes
    existing_ids = sheet.col_values(1)

    # 🛑 Si ya existe → NO escribir
    if run_id in existing_ids:
        return

    sheet.append_rows(df.values.tolist())
