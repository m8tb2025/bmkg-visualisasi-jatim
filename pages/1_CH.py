import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("🌧️ Curah Hujan (CH) Jawa Timur")

# Dummy koordinat kota-kota Jatim
kota = {
    "Surabaya": [-7.2575, 112.7521],
    "Malang": [-7.9666, 112.6326],
    "Kediri": [-7.8169, 112.0113],
    "Madiun": [-7.6298, 111.5230],
}

# Pilih waktu prakiraan (00, 03, ... 21)
jam = st.slider("Pilih Jam", 0, 21, 0, step=3, format="%02d:00")

# Dummy data CH (mm)
ch_data = {
    "Surabaya": 5 if jam in [12, 15] else 0,
    "Malang": 20 if jam in [15, 18] else 0,
    "Kediri": 50 if jam in [18, 21] else 0,
    "Madiun": 80 if jam in [0, 3] else 0,
}

# Peta folium
m = folium.Map(location=[-7.5, 112.0], zoom_start=8, tiles="cartodbpositron")

# Warna sesuai intensitas hujan
def warna_ch(ch):
    if ch == 0:
        return None
    elif ch < 20:
        return "green"
    elif ch < 50:
        return "yellow"
    else:
        return "red"

for k, v in kota.items():
    if ch_data[k] > 0:
        folium.CircleMarker(
            location=v,
            radius=10,
            popup=f"{k}: {ch_data[k]} mm",
            color=warna_ch(ch_data[k]),
            fill=True,
            fill_color=warna_ch(ch_data[k]),
            fill_opacity=0.6,
        ).add_to(m)

st_folium(m, width=700, height=500)
