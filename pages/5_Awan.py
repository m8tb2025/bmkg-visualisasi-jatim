from streamlit_folium import st_folium
import folium

# Buat peta
m = folium.Map(location=[-7.5, 112.5], zoom_start=7)

# Tambahkan legend custom (CSS biar lebih kecil)
legend_html = """
<div style="
position: fixed; 
bottom: 50px; left: 50px; width: 150px; 
background-color: white; 
border:2px solid grey; 
z-index:9999; 
font-size:12px;
padding: 5px;
">
<b>Legenda Awan Rendah</b><br>
<i style="background:red;width:10px;height:10px;float:left;margin-right:5px;"></i> Cb (Cumulonimbus)<br>
<i style="background:blue;width:10px;height:10px;float:left;margin-right:5px;"></i> Cu (Cumulus)<br>
<i style="background:gray;width:10px;height:10px;float:left;margin-right:5px;"></i> St (Stratus)<br>
</div>
"""

m.get_root().html.add_child(folium.Element(legend_html))

# Tampilkan di Streamlit
st_folium(m, width=700, height=500)
