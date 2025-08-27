import streamlit as st
import folium
from streamlit_folium import st_folium
import math

st.set_page_config(page_title="Angin Jawa Timur", layout="wide")

st.title("Arah & Kecepatan Angin - Jawa Timur")
st.markdown("Visualisasi prakiraan angin setiap 3 jam untuk wilayah Jawa Timur")

# Dummy data angin: [lon, lat, u (komponen zonal), v (komponen meridional)]
# u > 0 artinya angin dari barat ke timur, v > 0 artinya angin dari selatan ke utara
data_angin = [
    [112.75, -7.25, -2, -4],   # Surabaya
    [111.65, -7.55, 1, -3],    # Madiun
    [113.30, -7.75, -3, -1],   # Jember
    [114.35, -8.15, 2, -2],    # Banyuwangi
]

# Pilih waktu (per 3 jam)
time_selected = st.selectbox(
    "Pilih waktu (jam UTC)", 
    ["00", "03", "06", "09", "12", "15", "18", "21"], 
    index=0
)

# Base map Jawa Timur
m = folium.Map(location=[-7.5, 112], zoom_start=7, tiles="cartodb positron")

# Fungsi buat menghitung arah & kecepatan angin
def wind_properties(u, v):
    speed = round(math.sqrt(u**2 + v**2), 1)  # kecepatan
    direction = (math.degrees(math.atan2(-u, -v)) + 360) % 360  # derajat meteorologi
    return speed, direction

# Plot data angin
for lon, lat, u, v in data_angin:
    speed, direction = wind_properties(u, v)

    # Buat panah arah angin
    folium.RegularPolygonMarker(
        location=(lat, lon),
        number_of_sides=3,
        radius=8,
        rotation=direction,
        color="blue",
        fill=True,
        fill_color="blue"
    ).add_to(m)

    # Tambahkan teks kecepatan di samping panah
    folium.map.Marker(
        [lat + 0.1, lon],  # geser dikit biar tidak tumpuk
        icon=folium.DivIcon(
            html=f"""
                <div style="
                    font-size: 12px;
                    font-weight: bold;
                    color: darkblue;
                    text-align: center;
                ">
                    {speed} m/s
                </div>
            """
        )
    ).add_to(m)

st_folium(m, width=900, height=600)
