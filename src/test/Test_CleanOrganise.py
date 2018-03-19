# for this test to work, you need to make sure the relative path to cache in the tflCycle.py and tflOyster.py are correct

import unittest, requests
from src import tflCycle, tflOysterCount
from geopy.geocoders import Nominatim

class Test_CleanOrganise (unittest.TestCase):

    def setUp (self):
        self.cycleData = [['Rental Id', 'Duration', 'Bike Id', 'End Date', 'EndStation Id', 'EndStation Name', 'Start Date', 'StartStation Id', 'StartStation Name'],
         ['50754225', '240', '11834', '10/01/2016 00:04', '383', 'Frith Street, Soho', '10/01/2016 00:00', '18', 'Drury Lane, Covent Garden'],
         ['50754226', '300', '9648', '10/01/2016 00:05', '383', 'Victoria Park Road, Hackney Central', '10/01/2016 00:00', '479', 'Pott Street, Bethnal Green'],
         ['50754227', '1200', '10689', '10/01/2016 00:20', '272', 'Baylis Road, Waterloo', '10/01/2016 00:00', '425', 'Harrington Square 2, Camden Town'],
         ['50754228', '780', '8593', '10/01/2016 00:14', '471', 'Hewison Street, Old Ford', '10/01/2016 00:01', '487', 'Canton Street, Poplar'],
          ['50754229', '600', '8619', '10/01/2016 00:11', '399', 'Brick Lane Market, Shoreditch', '10/01/2016 00:01', '501', 'Cephas Street, Bethnal Green'],
          ['50754230', '600', '8619', '10/01/2016 12:11', '399', 'Brick Lane Market, Shoreditch', '10/01/2016 00:01', '501', 'Cephas Street, Bethnal Green']]
        self.oysterData=[['downo', 'daytype', 'SubSystem', 'StartStn', 'EndStation', 'EntTime', 'EntTimeHHMM', 'ExTime', 'EXTimeHHMM', 'ZVPPT', 'JNYTYP', 'DailyCapping', 'FFare', 'DFare', 'RouteID', 'FinalProduct'],
                         ['3', 'Tue', 'LUL', 'Unstarted', 'Kings Cross M', '0', '00:00', '633', '10:33', 'Z0104', 'TKT', 'N', '0', '0', 'XX', 'LUL Travelcard-7 Day'],
                         ['4', 'Wed', 'LUL', 'Unstarted', 'Sudbury Hill', '0', '00:00', '447', '07:27', 'Z0110', 'TKT', 'N', '0', '0', 'XX', 'Freedom Pass (Elderly)'],
                         ['3', 'Tue', 'NR', 'Unstarted', 'Richmond', '0', '00:00', '966', '16:06', 'Z0304', 'TKT', 'N', '0', '0', 'XX', 'LUL Travelcard-7 Day'],
                         ['4', 'Wed', 'NR', 'Unstarted', 'Romford', '0', '00:00', '657', '10:57', 'Z0110', 'TKT', 'N', '0', '0', 'XX', 'Freedom Pass (Elderly)'],
                         ['6', 'Fri', 'NR', 'Unstarted', 'Norwood Junction SR', '0', '00:00', '450', '07:30', 'Z0104', 'TKT', 'N', '0', '0', 'XX', 'LUL Travelcard-7 Day'],
                         ['6', 'Fri', 'LUL', 'Unstarted', 'Clapham Common', '0', '00:00', '439', '07:19', 'Z0104', 'TKT', 'N', '0', '0', 'XX', 'LUL Travelcard-7 Day']]
        self.cleanDataObj = tflCycle.tflCycle(self.cycleData)
        self.cleanDataObj2 = tflOysterCount.tflOysterCount(self.oysterData)
        self.cleanData = self.cleanDataObj.cleanData()
        self.cleanOysterData = self.cleanDataObj2.cleanData()
        for row in self.cleanData:
            if 'Brick Lane Market, Shoreditch' in row:
                self.targetRow = row
        self.lat_BrickLane =requests.get("https://api.tfl.gov.uk/BikePoint/Search?query=Brick%20Lane%20Market,%20Shoreditch&app_key=c9dcd95b35785f8c19a41ce2d384ea41&app_id=3ccf74d3").json()[0].get('lat')
        self.lon_BrickLane =requests.get("https://api.tfl.gov.uk/BikePoint/Search?query=Brick%20Lane%20Market,%20Shoreditch&app_key=c9dcd95b35785f8c19a41ce2d384ea41&app_id=3ccf74d3").json()[0].get('lon')

    def test_cycle_grouping(self):
        # group Counter is added by one everytime there is an overlap of the bike id
        # the no. of overlap should equal to the number of rows of the original data minus one (as we remove the header) minus the cleaned data
        self.assertEqual(self.cleanDataObj.getGroupCounter(), len(self.cycleData)-1 -len(self.cleanData))

    def test_oyster_grouping(self):
       self.assertEqual(self.cleanDataObj2.getGroupCounter(), len(self.oysterData) - 1 - len(self.cleanOysterData))

    def test_update_count(self):
        # brick lane market should have 2 occurrences
        self.assertEqual(self.targetRow[1],2)

    def test_lat_value(self):
        self.assertEqual(str(self.lat_BrickLane) , self.targetRow[2])

    def test_lon_value(self):
        self.assertEqual(str(self.lon_BrickLane), self.targetRow[3])

    #
    # def test_node_value(self):
    #     geolocator = Nominatim()
    #     nodeID = geolocator.reverse((self.lat_BrickLane , self.lon_BrickLane)).raw['osm_id']
    #     self.assertEqual(self.targetRow[4], nodeID)
    #
    #

if __name__ == "__main__":
    unittest.main()
