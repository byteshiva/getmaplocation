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




# def calculator(operation, value1, value2):
#     switcher = {
#        "house": lambda v1, v2: {"Name":v1},

#        "/": lambda v1, v2: v1/v2,

#        "+": lambda v1, v2: v1+v2,

#        "-": lambda v1, v2: v1-v2,
#     }
#     return switcher.get(operation)(value1, value2)



# ---
# [('the book club', 'house'), ('100-106', 'house_number'), ('leonard st', 'road'), ('shoreditch', 'suburb'), ('london', 'city'), ('greater london', 'state_district'), ('ec2a 4rh', 'postcode'), ('united kingdom', 'country')]

# "Name": "Stunning Victorian",
# "Address__c": "18 Henry St",
# "City__c": "Cambridge",
# "State__c": "MA",
# "Zip__c": "01742",

## To speed up the compute, run in parallel using threads
# df['city_coord'] = df.apply(lambda x: "%s %s"%(x['Lat'], x['Lon']) ,axis=1).apply(lambda y : geolocator.geocode(y).address)
# df['unfamilar_object'] = df.apply(lambda x: "%s %s"%(x['Lat'], x['Lon']) ,axis=1).apply(lambda y : gl.getPropertiesSubObject(y))
# print(tr)

# from postal.expand import expand_address

# geolocator = Nominatim(user_agent="GetLoc")
# location = geolocator.geocode(latlong)
# location = cg.validateCache(latlong)
# location = geolocator.geocode("-27.435222, 153.065364")

# address = '44, Seventh Avenue, Swan Hill, Windsor, Brisbane City, Queensland, 4030, Australia'
# location = cache.address_cached(address)

# if __name__ == '__main__':
#     latlong = "-27.435356,153.025818"
#     validateCache(latlong)

# g = geopy.geocoders.GoogleV3()
# cache.save_to_cache(addr, location_from_nominatim)
