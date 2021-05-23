import geopy
import pickle
import sqlite3
# from geopy.geocoders import Nominatim


class Cache(object):
    def __init__(self, fn='cache.db'):
        self.conn = conn = sqlite3.connect(fn)
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS '
                    'Geo ( '
                    'address STRING PRIMARY KEY, '
                    'latlong STRING, '
                    'location BLOB '
                    ')')
        conn.commit()

    def latlong_cached(self, latlong):
        cur = self.conn.cursor()
        cur.execute('SELECT location FROM Geo WHERE latlong=?', (latlong,))
        res = cur.fetchone()
        if res is None:
            return False
        return pickle.loads(res[0])

    def save_to_cache_latlong(self, latlong, location):
        cur = self.conn.cursor()
        cur.execute('INSERT INTO Geo(latlong, location) VALUES(?, ?)',
                    (latlong, sqlite3.Binary(pickle.dumps(location, -1))))
        self.conn.commit()


def validateCache(latlon):
    # run a small test in this case
    import pprint

    cache = Cache('./db/test1.db')
    latlong = latlon

    location = cache.latlong_cached(latlong)

    if location:
        # print('was cached: {}\n{}'.format(location, pprint.pformat(location.raw)))
        print('was cached: \n{}'.format(pprint.pformat(location.address)))
        address_location = location.address
    else:
        print('was not cached, looking up and caching now')
        geolocator = geopy.Nominatim(user_agent="GetLoc")
        location_from_nominatim = geolocator.geocode(latlong)
        # addr = location_from_nominatim.address
        address_location = location_from_nominatim.address
        # print('found as: {}\n{}'.format(location_from_nominatim, pprint.pformat(location_from_nominatim.raw)))

        cache.save_to_cache_latlong(latlong, location_from_nominatim)
        print('... and now cached.')

    return address_location
