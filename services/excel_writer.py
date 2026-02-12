import pandas as pd
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

SHEET_NAME = "DataTesis"  # <-- cambia esto


def connect_to_sheets():
    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ],
    )
    client = gspread.authorize(creds)
    return client


def write_to_google_sheets():
    data = {
        "nombre_usuario": [st.session_state.nombre] * len(st.session_state.imagenes),
        "imagen": st.session_state.imagenes,
        "tiempo_segundos": st.session_state.tiempos,
        "escala": st.session_state.escalas,
    }

    df = pd.DataFrame(data)

    client = connect_to_sheets()
    sheet = client.open(SHEET_NAME).sheet1

    # Si quieres agregar sin borrar:
    sheet.append_rows(df.values.tolist())
