import unittest
import requests
from geopy.geocoders import Nominatim, get_geocoder_for_service
from pathlib import Path

class Test_Integration (unittest.TestCase):
    def setUp(self):
        self.item = "Frith Street, Soho"
        self.input = Path('../../data/01aJourneyDataExtract10Jan16-23Jan16.csv')

    def test_TFLAPI(self):
        urlQueryid = self.item.replace(" ","%20")
        url = "https://api.tfl.gov.uk/BikePoint/Search?query="+urlQueryid+"&app_key=192e25146670a8b781a9c53a01b3027f&app_id=9a47548b"
        response = requests.get(url)
        self.assertTrue(response.json()[0] != [])

    def test_Nominatim(self):
        #For the service provided, try to return a geocoder class.
        get_geocoder_for_service("nominatim")
        geolocator = Nominatim()
        location = geolocator.geocode(self.item)
        self.assertTrue (location != None )

    def test_InputFile(self):
        self.assertTrue(self.input.is_file())

if __name__ == "__main__":
    unittest.main()


