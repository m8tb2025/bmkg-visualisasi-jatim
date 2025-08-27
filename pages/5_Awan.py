import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import pandas as pd

# === 1. Buka data (misal GRIB/NetCDF) ===
ds = xr.open_dataset("cloud_data.nc")   # ganti sesuai file data
low_cloud = ds["cld_low"]               # variabel awan rendah (0–3 km)

# === 2. Daftar waktu per 3 jam ===
times = pd.date_range(start=str(low_cloud.time.values[0]), 
                      end=str(low_cloud.time.values[-1]), freq="3H")

# === 3. Looping tiap jam ===
for t in times:
    data_t = low_cloud.sel(time=t)

    fig, ax = plt.subplots(subplot_kw={"projection": ccrs.PlateCarree()}, figsize=(8,6))
    ax.coastlines()
    
    # === 4. Plot data awan rendah ===
    im = data_t.plot(ax=ax, cmap="gray_r", transform=ccrs.PlateCarree(),
                     add_colorbar=False)
    
    # === 5. Tambahkan judul waktu ===
    plt.title(f"Low Clouds (Cu, Cb, St, Sc)\nValid: {t:%Y-%m-%d %H UTC}", fontsize=12)
    
    # === 6. Simpan hasil ===
    plt.savefig(f"lowcloud_{t:%Y%m%d%H}.png", dpi=150, bbox_inches="tight")
    plt.clo
