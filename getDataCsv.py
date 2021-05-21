import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
import getlocation as gl

geolocator = Nominatim(user_agent="GetLoc")

url = ("csv/realestatemaps21february2018slq.csv")
realtyStateMapsData = pd.read_csv(url)

df = realtyStateMapsData[["Title","Lat","Lon"]].head(20)

## 1st Lamda function returns concatenates and return a string,
## 2st Lamda function returns geo address for Lat, Lon string passed from 1st lamda function.

## To speed up the compute, run in parallel using threads
df['city_coord'] = df.apply(lambda x: "%s %s"%(x['Lat'], x['Lon']) ,axis=1).apply(lambda y : geolocator.geocode(y).address)
df['unfamilar_object'] = df.apply(lambda x: "%s %s"%(x['Lat'], x['Lon']) ,axis=1).apply(lambda y : gl.getPropertiesSubObject(y))
# print(tr)
df.to_json('file.json', orient='records')
