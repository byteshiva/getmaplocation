from geopy.geocoders import Nominatim
from postal.parser import parse_address
from libs import cachedgeo as cg

def getGeoObj(key, value):
    switcher = {
       "house":  lambda value: {"Name":value},
       "suburb":  lambda value: "",
       "country":  lambda value: "",
       "house_number":  lambda value: {"Address__c":value},
       "city":  lambda value: {"City__c":value},
       "road":   lambda value: {"Address__c":value},
       "state":   lambda value: {"State__c":value},
       "state_district":   lambda value: {"State__c":value},
       "postcode":   lambda value: {"Zip__c":value},
    #  "country":   lambda value: {"Country__c":value},
    }
    return switcher.get(key)(value)

def getPropertiesSubObject(latlong):
    obj = {}
    location_addr = cg.validateCache(latlong)
    addrdetails = parse_address(location_addr)

    for sublist in addrdetails:
        if(sublist[1] == 'road' and 'Address__c' in obj):
            if ('Address__c' in obj):
                obj.update(getGeoObj(sublist[1], obj['Address__c'] + " " + sublist[0]))
        else:
            obj.update(getGeoObj(sublist[1], sublist[0]))
    
    return obj