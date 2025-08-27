import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Streamline Angin Jawa Timur", layout="wide")

st.title("Streamline Angin Jawa Timur")
st.markdown("Visualisasi arah dan kecepatan angin (setiap 3 jam) dalam bentuk **streamline**")

# --- Dummy grid data (lon, lat, u, v) ---
lon = np.linspace(110, 115, 30)
lat = np.linspace(-9, -6.5, 30)
Lon, Lat = np.meshgrid(lon, lat)

# u = komponen zonal, v = komponen meridional
u = -2 + np.sin(Lat) * 2
v =  2 + np.cos(Lon) * 2

# Pilih waktu
time_selected = st.selectbox(
    "Pilih waktu (jam UTC)", 
    ["00", "03", "06", "09", "12", "15", "18", "21"], 
    index=0
)

# Plot
fig, ax = plt.subplots(figsize=(7,7))

# Streamline
strm = ax.streamplot(
    Lon, Lat, u, v,
    density=2,              # makin besar makin rapat
    color=np.sqrt(u**2+v**2), # warna = magnitude angin
    cmap="viridis", 
    linewidth=1
)

cbar = fig.colorbar(strm.lines, ax=ax, orientation="vertical", shrink=0.7)
cbar.set_label("Kecepatan Angin (m/s)")

ax.set_xlim(110, 115)
ax.set_ylim(-9, -6.5)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_title(f"Streamline Angin Jawa Timur (UTC {time_selected})")

st.pyplot(fig)
