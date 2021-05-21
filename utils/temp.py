import pandas as pd
import numpy as np

import datetime as DT
import hmac
from geopy.geocoders import Nominatim
# from geopy.distance import vincenty
# from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="GetLoc")
# location = geolocator.reverse("-27.435356, 153.025818")
# print(location.address)

def sublst(row):
    s1 = row['Lat']
    s2 = row['Lon']
    s3="%s %s"%(s1,s2)
    return geolocator.reverse(s3).address

url = ("csv/realestatemaps21february2018slq.csv")

tips = pd.read_csv(url)
df = tips[["Title","Lat","Lon"]].head(3)

# df['city_coord'] = df['Lat'].apply(geolocator.geocode).apply(lambda x: (x.Lat, x.Lon))
# df['city_coord'] = df.apply(lambda x: (x.Lat, x.Lon))
# df['city_coord'] = df.apply(sublst ,axis=1)
df['city_coord'] = df.apply(lambda x: "%s %s"%(x['Lat'], x['Lon']) ,axis=1).apply(lambda y : geolocator.geocode(y).address)
# df['city_coord'] = df[['Lat','Lon']].apply(lambda x:)
print(df)



# csv_file = pd.DataFrame(pd.read_csv(url, sep = ",", header = 0, index_col = False))	
# csv_file.to_json("data.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)

df.to_json('file.json', orient='records')