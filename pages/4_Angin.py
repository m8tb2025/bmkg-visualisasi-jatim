import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Angin Jawa Timur", layout="wide")

st.title("Wind Barb (Arah & Kecepatan Angin) - Jawa Timur")
st.markdown("Visualisasi angin setiap 3 jam di beberapa lokasi Jawa Timur")

# Dummy data: [lon, lat, u (zonal), v (meridional)]
data_angin = [
    [112.75, -7.25, -2, -4],   # Surabaya
    [111.65, -7.55, 1, -3],    # Madiun
    [113.30, -7.75, -3, -1],   # Jember
    [114.35, -8.15, 2, -2],    # Banyuwangi
]

# Pilih waktu
time_selected = st.selectbox(
    "Pilih waktu (jam UTC)", 
    ["00", "03", "06", "09", "12", "15", "18", "21"], 
    index=0
)

# Ambil lon, lat, u, v
lon = [d[0] for d in data_angin]
lat = [d[1] for d in data_angin]
u   = [d[2] for d in data_angin]
v   = [d[3] for d in data_angin]

# Plot wind barb
fig, ax = plt.subplots(figsize=(6,6))
ax.barbs(lon, lat, u, v, length=7, barb_increments=dict(half=5, full=10, flag=50))

ax.set_title(f"Wind Barb Jawa Timur (UTC {time_selected})")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

st.pyplot(fig)
