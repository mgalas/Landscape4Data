from geopy.geocoders import Nominatim

geolocator = Nominatim()
coordList = []
coordList.append("52.509669, 13.376294")

for address in coordList:
    location = geolocator.reverse(address)
    print(location.raw)
