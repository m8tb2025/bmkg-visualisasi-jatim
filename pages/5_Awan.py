import streamlit as st
import folium
from streamlit_folium import st_folium

# Judul
st.title("Sebaran Awan Rendah di Jawa Timur")

# Dummy data stasiun + awan
# Format: [nama, lat, lon, jenis_awan]
data_awan = [
    ["Juanda", -7.379, 112.787, "Cu"],
    ["Malang", -7.926, 112.602, "Cb"],
    ["Kediri", -7.816, 112.011, "St"],
    ["Madiun", -7.630, 111.523, "Sc"],
]

# Map center di Jatim
m = folium.Map(location=[-7.5, 112.5], zoom_start=8, tiles="CartoDB positron")

# Warna/ikon sesuai jenis awan
ikon_awan = {
    "Cu": ("cloud", "blue", "Cumulus"),
    "Cb": ("bolt", "red", "Cumulonimbus"),
    "St": ("align-justify", "gray", "Stratus"),
    "Sc": ("cloud", "green", "Stratocumulus"),
}

# Tambahkan marker
for nama, lat, lon, jenis in data_awan:
    ikon, warna, label = ikon_awan.get(jenis, ("question", "black", "Unknown"))
    folium.Marker(
        location=[lat, lon],
        popup=f"{nama} - {jenis}",
        tooltip=f"{nama}: {jenis}",
        icon=folium.Icon(color=warna, icon=ikon, prefix="fa"),
    ).add_to(m)

# Tambahkan legend custom (HTML + CSS)
legend_html = """
<div style="
    position: fixed; 
    bottom: 30px; l
