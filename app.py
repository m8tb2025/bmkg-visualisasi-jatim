import streamlit as st

st.set_page_config(page_title="BMKG Visualisasi Jatim", layout="wide")

st.title("🌦️ Visualisasi Prakiraan Cuaca Jawa Timur")
st.markdown("""
Aplikasi ini menampilkan data prakiraan cuaca BMKG setiap 3 jam untuk wilayah Jawa Timur.
Silakan pilih parameter di menu sebelah kiri.
""")

st.info("Gunakan sidebar untuk memilih visualisasi per parameter (CH, Suhu, Angin, Visibilitas).")
