import streamlit as st
import pandas as pd
import os
from datetime import datetime


def run():
    st.title("¡Gracias por participar!")
    st.write("Has completado todas las fases del experimento.")

    # Construir resultados de las 3 fases
    rows = []

    # Fase 1
    imagenes_f1 = st.session_state.get("imagenes_fase1", [])
    tiempos_f1 = st.session_state.get("tiempos_fase1", [])
    escalas_f1 = st.session_state.get("escalas_fase1", [])
    for i in range(len(escalas_f1)):
        rows.append({
            "fase": 1,
            "imagen": imagenes_f1[i] if i < len(imagenes_f1) else "",
            "tiempo_seg": round(tiempos_f1[i], 2) if i < len(tiempos_f1) else "",
            "escala_sam": escalas_f1[i]
        })

    # Fase 2
    imagenes_f2 = st.session_state.get("imagenes_fase2", [])
    tiempos_f2 = st.session_state.get("tiempos_fase2", [])
    escalas_f2 = st.session_state.get("escalas_fase2", [])
    for i in range(len(escalas_f2)):
        rows.append({
            "fase": 2,
            "imagen": imagenes_f2[i] if i < len(imagenes_f2) else "",
            "tiempo_seg": round(tiempos_f2[i], 2) if i < len(tiempos_f2) else "",
            "escala_sam": escalas_f2[i]
        })

    # Fase 3
    imagenes_f3 = st.session_state.get("imagenes_fase3", [])
    tiempos_f3 = st.session_state.get("tiempos_fase3", [])
    escalas_f3 = st.session_state.get("escalas_fase3", [])
    for i in range(len(escalas_f3)):
        rows.append({
            "fase": 3,
            "imagen": imagenes_f3[i] if i < len(imagenes_f3) else "",
            "tiempo_seg": round(tiempos_f3[i], 2) if i < len(tiempos_f3) else "",
            "escala_sam": escalas_f3[i]
        })

    if rows:
        df = pd.DataFrame(rows)

        # Guardar CSV
        os.makedirs("results", exist_ok=True)
        participant = st.session_state.get("participant_id", "unknown")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"results/{participant}_{timestamp}.csv"
        df.to_csv(filename, index=False)

        st.success(f"Resultados guardados en `{filename}`")
        st.dataframe(df)
    else:
        st.warning("No se registraron resultados.")
