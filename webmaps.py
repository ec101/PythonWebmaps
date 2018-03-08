import pandas
import folium

data = pandas.read_csv("Volcanoes_USA.txt")
latitudes = list(data["LAT"])
longitudes = list(data["LON"])
elevations = list(data["ELEV"])

def colorProducer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="MyMap")

for lt, ln, el in zip(latitudes, longitudes, elevations):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=5, popup=str(el)+"m", fill="true", fill_color=colorProducer(el), color=colorProducer(el), fill_opacity=0.7))
    #fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+"m", icon=folium.Icon(color=colorProducer(el))))

map.add_child(fg)

map.save("Map1.html")
