#import modules
#folium is for mapping
import folium
import pandas

#read from volcanoes txt
data = pandas.read_csv("usa-volcano-web-mapping/Webmap_datasources/Volcanoes.txt")

#only read latitude and longtitude 
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#define green colour function
#only elevation will prompt green
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

html = """<h4>Volcano information:</h4>
Height: %s m
"""

#create map for usa
map = folium.Map(location=[38.58, -99.09], 
zoom_start=5, tiles="Stamen Terrain")

#create marker 
feature_group = folium.FeatureGroup(name="My Map")

#for loop for adding multiple marker
# add location on map
for lt, ln, el in zip(lat,lon, elev):
    feature_group.add_child(folium.CircleMarker(
        location=[lt,ln],
        radius= 6, 
        popup= str(el) + " m", 
        fill_color = color_producer(el), color = 'grey', fill_capacity=0.7))

#cover the map with sepearete line
feature_group.add_child(folium.GeoJson(data =(open('usa-volcano-web-mapping/Webmap_datasources/world.json', 'r', encoding='utf-8-sig').read())))
        
map.add_child(feature_group)

#create the map html file
map.save("usa-volcano-web-mapping/map.html")