from geopy.geocoders import Nominatim
# from geopy.distance import vincenty
# from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="GetLoc")

def sublst(row):
    s1 = row['Lat']
    s2 = row['Lon']
    s3="%s %s"%(s1,s2)
    return geolocator.reverse(s3).address