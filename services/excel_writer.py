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
        # Validación mínima: al menos una fase debe tener datos
        has_f1 = len(st.session_state.get("imagenes_fase1", [])) > 0
        has_f2 = len(st.session_state.get("imagenes_fase2", [])) > 0
        has_f3 = len(st.session_state.get("imagenes_fase3", [])) > 0

        if not has_f1 and not has_f2 and not has_f3:
            return

        if "run_id" not in st.session_state:
            st.session_state.run_id = str(uuid.uuid4())

        run_id = st.session_state.run_id
        nombre = st.session_state.get("nombre", "anon")

        # Recopilar datos de las 3 fases
        all_run_ids = []
        all_nombres = []
        all_fases = []
        all_imagenes = []
        all_tiempos = []
        all_escalas = []

        fases_config = [
            {
                "fase": 1,
                "imagenes": st.session_state.get("imagenes_fase1", []),
                "tiempos": st.session_state.get("tiempos_fase1", []),
                "escalas": st.session_state.get("escalas_fase1", []),
            },
            {
                "fase": 2,
                "imagenes": st.session_state.get("imagenes_fase2", []),
                "tiempos": st.session_state.get("tiempos_fase2", []),
                "escalas": st.session_state.get("escalas_fase2", []),
            },
            {
                "fase": 3,
                "imagenes": st.session_state.get("imagenes_fase3", []),
                "tiempos": st.session_state.get("tiempos_fase3", []),
                "escalas": st.session_state.get("escalas_fase3", []),
            },
        ]

        for fase_data in fases_config:
            fase_num = fase_data["fase"]
            imagenes = fase_data["imagenes"]
            tiempos = fase_data["tiempos"]
            escalas = fase_data["escalas"]

            n = len(escalas)
            for i in range(n):
                all_run_ids.append(run_id)
                all_nombres.append(nombre)
                all_fases.append(fase_num)
                all_imagenes.append(imagenes[i] if i < len(imagenes) else "")
                all_tiempos.append(round(tiempos[i], 2) if i < len(tiempos) else "")
                all_escalas.append(escalas[i])

        df = pd.DataFrame({
            "run_id": all_run_ids,
            "nombre_usuario": all_nombres,
            "fase": all_fases,
            "imagen": all_imagenes,
            "tiempo_segundos": all_tiempos,
            "escala": all_escalas,
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
                "fase",
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

