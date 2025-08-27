import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Suhu Jawa Timur", layout="wide")

st.title("Suhu Permukaan - Jawa Timur")
st.markdown("Visualisasi prakiraan suhu setiap 3 jam untuk wilayah Jawa Timur")

# Dummy data suhu (°C) [lon, lat, suhu]
data_suhu = [
    [112.75, -7.25, 34],  # Surabaya
    [111.65, -7.55, 28],  # Madiun
    [113.30, -7.75, 26],  # Jember
    [114.35, -8.15, 30],  # Banyuwangi
]

# Pilih waktu (per 3 jam)
time_selected = st.selectbox(
    "Pilih waktu (jam UTC)", 
    ["00", "03", "06", "09", "12", "15", "18", "21"], 
    index=0
)

# Base map Jawa Timur
m = folium.Map(location=[-7.5, 112], zoom_start=7, tiles="cartodb positron")

# Fungsi warna suhu
def suhu_color(temp):
    if temp <= 24:
        return "blue"
    elif 25 <= temp <= 28:
        return "green"
    elif 29 <= temp <= 32:
        return "orange"
    else:
        return "red"

# Plot data suhu dengan angka langsung di map
for lon, lat, temp in data_suhu:
    folium.map.Marker(
        [lat, lon],
        icon=folium.DivIcon(
            html=f"""
                <div style="
                    font-size: 14px;
                    font-weight: bold;
                    color: {suhu_color(temp)};
                    text-align: center;
                ">
                    {temp}°C
                </div>
            """
        )
    ).add_to(m)

st_folium(m, width=900, height=600)
