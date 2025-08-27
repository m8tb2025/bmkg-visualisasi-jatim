import streamlit as st
import folium
from folium.plugins import MarkerCluster
from branca.element import Template, MacroElement

st.title("Peta Awan Rendah")

# Koordinat tengah Jatim
m = folium.Map(location=[-7.5, 112.5], zoom_start=7)

# Contoh titik awan rendah
awan_data = [
    {"lokasi": [-7.3, 112.7], "jenis": "Cb"},
    {"lokasi": [-7.8, 111.5], "jenis": "Cu"},
    {"lokasi": [-8.1, 113.2], "jenis": "St"},
]

# Warna untuk jenis awan
warna = {"Cb": "red", "Cu": "blue", "St": "gray"}

for awan in awan_data:
    folium.CircleMarker(
        location=awan["lokasi"],
        radius=7,
        color=warna[awan["jenis"]],
        fill=True,
        fill_color=warna[awan["jenis"]],
        popup=f"Awan {awan['jenis']}"
    ).add_to(m)

# Tambahkan legend pakai HTML template
legend_html = """
{% macro html(this, kwargs) %}
<div style="
    position: fixed; 
    bottom: 50px; left: 50px; width: 160px; height: 110px; 
    background-color: white;
    border:2px solid grey; z-index:9999; font-size:14px;
    ">
&nbsp;<b>Legenda Awan Rendah</b><br>
&nbsp;<i style="background:red;color:red;">oo</i>&nbsp;Cb (Cumulonimbus)<br>
&nbsp;<i style="background:blue;color:blue;">oo</i>&nbsp;Cu (Cumulus)<br>
&nbsp;<i style="background:gray;color:gray;">oo</i>&nbsp;St (Stratus)<br>
</div>
{% endmacro %}
"""
legend = MacroElement()
legend._template = Template(legend_html)
m.get_root().add_child(legend)

st.components.v1.html(m._repr_html_(), height=600)
