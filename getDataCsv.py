import pandas as pd
import numpy as np
# from geopy.geocoders import Nominatim
import getlocation as gl
from libs import cachedgeo as cg

# geolocator = Nominatim(user_agent="GetLoc")

url = ("csv/realestatemaps21february2018slq.csv")
realtyStateMapsData = pd.read_csv(url)

df = realtyStateMapsData[["Title","Lat","Lon"]].head(25)

## 1st Lamda function returns concatenates and return a string,
## 2st Lamda function returns geo address for Lat, Lon string passed from 1st lamda function.
df['city_coord'] = df.apply(lambda x: "%s %s"%(x['Lat'], x['Lon']) ,axis=1).apply(lambda y :cg.validateCache(y))
df['unfamilar_object'] = df.apply(lambda x: "%s %s"%(x['Lat'], x['Lon']) ,axis=1).apply(lambda y : gl.getPropertiesSubObject(y))

df.to_json('./data/json/file.json', orient='records')
