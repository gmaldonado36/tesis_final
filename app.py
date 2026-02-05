import streamlit as st
from pages import instructions, fase1, scale, end
from services.state_manager import init_state

st.set_page_config(layout="centered")

init_state()

fase = st.session_state.fase

if fase == "instructions":
    instructions.run()
elif fase == "fase1":
    fase1.run()
elif fase == "scale":
    scale.run()
elif fase == "end":
    end.run()
