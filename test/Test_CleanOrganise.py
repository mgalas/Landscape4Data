import unittest, requests
from CleanOrganise import CleanOrganise
from geopy.geocoders import Nominatim

class Test_CleanOrganise (unittest.TestCase):

    def setUp (self):
        self.data = [['Rental Id', 'Duration', 'Bike Id', 'End Date', 'EndStation Id', 'EndStation Name', 'Start Date', 'StartStation Id', 'StartStation Name'],
         ['50754225', '240', '11834', '10/01/2016 00:04', '383', 'Frith Street, Soho', '10/01/2016 00:00', '18', 'Drury Lane, Covent Garden'],
         ['50754226', '300', '9648', '10/01/2016 00:05', '383', 'Victoria Park Road, Hackney Central', '10/01/2016 00:00', '479', 'Pott Street, Bethnal Green'],
         ['50754227', '1200', '10689', '10/01/2016 00:20', '272', 'Baylis Road, Waterloo', '10/01/2016 00:00', '425', 'Harrington Square 2, Camden Town'],
         ['50754228', '780', '8593', '10/01/2016 00:14', '471', 'Hewison Street, Old Ford', '10/01/2016 00:01', '487', 'Canton Street, Poplar'],
          ['50754229', '600', '8619', '10/01/2016 00:11', '399', 'Brick Lane Market, Shoreditch', '10/01/2016 00:01', '501', 'Cephas Street, Bethnal Green'],
          ['50754230', '600', '8619', '10/01/2016 12:11', '399', 'Brick Lane Market, Shoreditch', '10/01/2016 00:01', '501', 'Cephas Street, Bethnal Green']]
        self.cleanDataObj = CleanOrganise(self.data)
        self.cleanData = self.cleanDataObj.cleanData(5)
        for row in self.cleanData:
            if 'Brick Lane Market, Shoreditch' in row:
                self.targetRow = row
        self.lat_BrickLane =requests.get("https://api.tfl.gov.uk/BikePoint/Search?query=Brick%20Lane%20Market,%20Shoreditch&app_key=c9dcd95b35785f8c19a41ce2d384ea41&app_id=3ccf74d3").json()[0].get('lat')
        self.lon_BrickLane =requests.get("https://api.tfl.gov.uk/BikePoint/Search?query=Brick%20Lane%20Market,%20Shoreditch&app_key=c9dcd95b35785f8c19a41ce2d384ea41&app_id=3ccf74d3").json()[0].get('lon')

    def test_grouping_ID(self):
        # group Counter is added by one everytime there is an overlap of the bike id
        # the no. of overlap should equal to the number of rows of the original data minus one (as we remove the header) minus the cleaned data
        self.assertEqual(self.cleanDataObj.getGroupCounter(), len(self.data)-1 -len(self.cleanData))

    def test_update_count(self):
        # brick lane market should have 2 occurence
        self.assertEqual(self.targetRow[1],2)

    def test_lat_value(self):
        self.assertEqual(self.lat_BrickLane, self.targetRow[2])

    def test_lon_value(self):
        self.assertEqual(self.lon_BrickLane, self.targetRow[3])

    def test_node_value(self):
        geolocator = Nominatim()
        nodeID = geolocator.reverse((self.lat_BrickLane , self.lon_BrickLane)).raw['osm_id']
        self.assertEqual(self.targetRow[4], nodeID)

    def test_clean_data(self):
        self.assertEqual(self.cleanData, [['Frith Street, Soho', 1, 51.513103, -0.131213, '349937283'],['Victoria Park Road, Hackney Central', 1, 51.536424, -0.054162, '469788549'],
['Baylis Road, Waterloo', 1, 51.501444, -0.110699, '264835734'],['Hewison Street, Old Ford', 1, 51.533283, -0.028155, '1818809538'],['Brick Lane Market, Shoreditch', 2, 51.522617, -0.071653, '1322524169']] )



if __name__ == "__main__":
    unittest.main()
