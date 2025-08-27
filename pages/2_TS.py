import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Thunderstorm Jawa Timur", layout="wide")

st.title("Thunderstorm (TS) - Jawa Timur")
st.markdown("Visualisasi prakiraan Thunderstorm (TS) setiap 3 jam untuk wilayah Jawa Timur")

# Dummy data (nanti bisa diganti BMKG)
# Format: [lon, lat, TS 0/1]
data_ts = [
    [112.75, -7.25, 1],  # Surabaya
    [111.65, -7.55, 0],  # Madiun
    [113.30, -7.75, 1],  # Jember
    [114.35, -8.15, 0],  # Banyuwangi
]

# Pilih waktu (per 3 jam)
time_selected = st.selectbox(
    "Pilih waktu (jam UTC)", 
    ["00", "03", "06", "09", "12", "15", "18", "21"], 
    index=0
)

# Base map Jawa Timur
m = folium.Map(location=[-7.5, 112], zoom_start=7, tiles="cartodb positron")

# Plot data
for lon, lat, ts in data_ts:
    color = "purple" if ts == 1 else "gray"
    folium.CircleMarker(
        location=[lat, lon],
        radius=10,
        color=color,
        fill=True,
        fill_opacity=0.6,
        popup=f"TS: {'Ada' if ts==1 else 'Tidak'} (Jam {time_selected} UTC)",
    ).add_to(m)

st_folium(m, width=900, height=600)
