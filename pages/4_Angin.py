import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Streamline Angin Jawa Timur", layout="wide")

st.title("Streamline Angin Jawa Timur")
st.markdown("Visualisasi arah dan kecepatan angin (dummy data)")

# Grid Jawa Timur
lon = np.linspace(110, 115, 40)
lat = np.linspace(-9, -6.5, 40)
Lon, Lat = np.meshgrid(lon, lat)

# Komponen angin u dan v (dummy)
u = -2 + np.sin(np.radians(Lat)) * 2
v =  2 + np.cos(np.radians(Lon)) * 2

# Pilih waktu
time_selected = st.selectbox(
    "Pilih waktu (jam UTC)", 
    ["00", "03", "06", "09", "12", "15", "18", "21"], 
    index=0
)

# Plot streamline
fig, ax = plt.subplots(figsize=(7,7))

strm = ax.streamplot(
    Lon, Lat, u, v,
    density=2.0,
    color=np.sqrt(u**2+v**2),
    cmap="viridis",
    linewidth=1
)

cbar = plt.colorbar(strm.lines, ax=ax, orientation="vertical", shrink=0.7, pad=0.05)
cbar.set_label("Kecepatan Angin (m/s)")

ax.set_title(f"Streamline Angin Jawa Timur (UTC {time_selected})")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

st.pyplot(fig)
