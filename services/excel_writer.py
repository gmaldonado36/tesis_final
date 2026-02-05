import pandas as pd
from io import BytesIO
import streamlit as st

def generate_excel():
    data = {
        "nombre_usuario": [st.session_state.nombre]*len(st.session_state.imagenes),
        "imagen": st.session_state.imagenes,
        "tiempo_segundos": st.session_state.tiempos,
        "escala": st.session_state.escalas,
    }

    df = pd.DataFrame(data)

    buffer = BytesIO()
    df.to_excel(buffer, index=False)
    buffer.seek(0)
    return buffer
