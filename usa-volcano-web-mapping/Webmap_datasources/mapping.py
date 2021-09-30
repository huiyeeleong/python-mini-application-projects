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


#create map for usa
map = folium.Map(location=[38.58, -99.09], 
zoom_start=5, tiles="Stamen Terrain")

#create marker 
feature_group = folium.FeatureGroup(name="My Map")

#for loop for adding multiple marker
for lt, ln, el in zip(lat,lon, elev):
    feature_group.add_child(folium.Marker(
        location=[lt,ln], 
        popup= str(el), 
        icon=folium.Icon(color='green')))
        
map.add_child(feature_group)

#create the map html file
map.save("usa-volcano-web-mapping/map.html")