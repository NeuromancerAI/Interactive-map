import folium
import pandas


data = pandas.read_csv("test2.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
name = list(data["NAME"])
stat = list(data["STATUS"])
web = list(data["WEBSITE"])

map = folium.Map(location=[24.771901, 55.528385], zoom_start=7)

fg = folium.FeatureGroup(name="My Map")

for ln, lt, na, st, wb in zip(lon, lat, name, stat, web):

    fg.add_child(folium.Marker(location=[lt, ln], popup=str(na + " - " + st + " : " + wb), icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("Map3.html")
