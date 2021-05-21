from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="GetLoc")
location = geolocator.reverse("-27.435356, 153.025818")
print(location.address)
## 44, Seventh Avenue, Swan Hill, Windsor, Brisbane City, Queensland, 4030, Australia
