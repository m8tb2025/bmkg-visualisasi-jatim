import streamlit as st
import folium
from streamlit_folium import st_folium
import numpy as np

st.set_page_config(page_title="Streamline Angin Jawa Timur", layout="wide")

st.title("🌬️ Streamline Angin Jawa Timur (Folium Map)")
st.markdown("Visualisasi arah dan kecepatan angin pada peta interaktif")

# Grid Jawa Timur
lon = np.linspace(110, 115, 15)  # lebih jarang biar tidak padat
lat = np.linspace(-9, -6.5, 15)
Lon, Lat = np.meshgrid(lon, lat)

# Komponen angin u dan v (dummy data)
u = -2 + np.sin(np.radians(Lat)) * 2
v =  2 + np.cos(np.radians(Lon)) * 2

# Hitung kecepatan
speed = np.sqrt(u**2 + v**2)

# Pilih waktu
time_selected = st.selectbox(
    "Pilih waktu (jam UTC)", 
    ["00", "03", "06", "09", "12", "15", "18", "21"], 
    index=0
)

# Buat peta folium
m = folium.Map(location=[-7.5, 112], zoom_start=7, tiles="CartoDB positron")

# Tambahkan vektor angin ke peta (pakai garis panah sederhana)
for i in range(Lon.shape[0]):
    for j in range(Lon.shape[1]):
        lon0, lat0 = Lon[i, j], Lat[i, j]
        u_ij, v_ij = u[i, j], v[i, j]
        lon1, lat1 = lon0 + 0.2 * u_ij, lat0 + 0.2 * v_ij  # arah panah
        
        folium.PolyLine(
            locations=[(lat0, lon0), (lat1, lon1)],
            color="blue",
            weight=2,
            opacity=0.8
        ).add_to(m)
        
        # Titik awal dengan info popup kecepatan
        folium.CircleMarker(
            location=(lat0, lon0),
            radius=2,
            color="red",
            fill=True,
            fill_opacity=0.7,
            popup=f"U={u_ij:.2f}, V={v_ij:.2f}, Speed={speed[i,j]:.2f} m/s"
        ).add_to(m)

# Tampilkan peta di Streamlit
st_folium(m, width=800, height=600)
