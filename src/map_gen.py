import folium
import pandas as pd
import numpy as np

# Load joined data
data = pd.read_csv("../data/joined_data.csv")
# Remove null locations and keeping active fixit
data_clean = data[~data['lat'].isnull() &
                  data['Date Trap Fixed'].isnull()]

# Pull out relevant columns for leaflet map
vname = list(data_clean["Trap Number"])
lat = list(data_clean["lat"])
lon = list(data_clean["lon"])
elev = list(data_clean["date"])
status = list(data_clean["Description From Trapper"])

map = folium.Map(location=[-41.3, 174.9], zoom_start=12, tiles="OpenStreetMap")

fgv = folium.FeatureGroup(name="Traps")

for lt, ln, el, st, vnm in zip(lat, lon, elev, status, vname):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 8, popup= folium.Popup("<b> Trap: </b>" + vnm + "<br> " +
            "<b> Reported: </b>" + el + "<br> " +
            "<b> Issue: </b>" + st, max_width=450),
    fill_color='red', color = 'red', fill=True, fill_opacity=0.7))

map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("../results/fixit_traps.html")
