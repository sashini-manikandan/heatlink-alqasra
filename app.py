from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="HEATLINK | Al Qasra",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

html_path = Path(__file__).parent / "heatlink_al_qasra.html"
html = html_path.read_text(encoding="utf-8")

# The original prototype is a self-contained HTML/CSS/JavaScript page.
# Streamlit displays it inside an iframe; scrolling is enabled for smaller screens.
components.html(html, height=2400, scrolling=True)
