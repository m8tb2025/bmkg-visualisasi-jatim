import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature

st.set_page_config(page_title="Streamline Angin Jawa Timur", layout="wide")

st.title("Streamline Angin Jawa Timur")
st.markdown("Visualisasi arah dan kecepatan angin (setiap 3 jam) dalam bentuk **streamline** dengan peta dasar")

# --- Dummy grid data (lon, lat, u, v) ---
lon = np.linspace(110, 115, 40)
lat = np.linspace(-9, -6.5, 40)
Lon, Lat = np.meshgrid(lon, lat)

# u = komponen zonal, v = komponen meridional
u = -2 + np.sin(np.radians(Lat)) * 2
v =  2 + np.cos(np.radians(Lon)) * 2

# Pilih waktu
time_selected = st.selectbox(
    "Pilih waktu (jam UTC)", 
    ["00", "03", "06", "09", "12", "15", "18", "21"], 
    index=0
)

# Plot
fig = plt.figure(figsize=(8,8))
ax = plt.axes(projection=ccrs.PlateCarree())

# Batas domain Jawa Timur
ax.set_extent([110, 115, -9, -6.5], crs=ccrs.PlateCarree())

# Tambahkan peta dasar
ax.add_feature(cfeature.COASTLINE, linewidth=0.8)
ax.add_feature(cfeature.BORDERS, linewidth=0.5)
ax.add_feature(cfeature.LAND, facecolor="lightgray")
ax.add_feature(cfeature.OCEAN, facecolor="lightblue")

# Streamline
strm = ax.streamplot(
    Lon, Lat, u, v,
    transform=ccrs.PlateCarree(),
    density=2.0,
    color=np.sqrt(u**2+v**2), # magnitude angin
    cmap="viridis",
    linewidth=1
)

# Colorbar
cbar = plt.colorbar(strm.lines, ax=ax, orientation="vertical", shrink=0.7, pad=0.05)
cbar.set_label("Kecepatan Angin (m/s)")

ax.set_title(f"Streamline Angin Jawa Timur (UTC {time_selected})")

st.pyplot(fig)
