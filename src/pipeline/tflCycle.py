import requests
from CleanOrganise import CleanOrganise

"""
This is for TFL's Cycle Hire System
"""
class tflCycle(CleanOrganise):
    def __init__(self, data):
        super(tflCycle, self).__init__(data, '../../data/cache/tfl_api_cache.txt')

    def apiCall(self, item):
        indObj = None
        urlQueryid = item.replace(" ", "%20")
        url = "https://api.tfl.gov.uk/BikePoint/Search?query=" + urlQueryid + "&app_key=192e25146670a8b781a9c53a01b3027f&app_id=9a47548b"
        response = requests.get(url)
        try:
            indObj = response.json()[0]
        except Exception as e:
            indObj = None
            # Invalid TFL API response
        if not indObj is None:
            self.addToCache(item, indObj)
        return indObj

    def getLatLon(self, stationName):
        res = None
        apiDataFromCache = self.getFromCache(stationName)
        if apiDataFromCache is None:
            apiDataFromCache = [False, '']
        lat = ''
        lon = ''
        if not apiDataFromCache[0]:
            res = self.apiCall(stationName)
            if not (res is None):
                lat = res.get('lat')
                lon = res.get('lon')
        else:
            lat, lon = apiDataFromCache[1].rstrip('\n').split("#")
        return [lat, lon]

    def cleanData(self):
        print("Cleaning and Organising Data...")
        self.organisedData = []
        self.counter = 0

        for item in self.dataFromFile:
            self.groupStationID(item[5])

        print('\t retrieving lat and long')

        for sortedItem in self.organisedData:
            self.counter += 1
            latlon = self.getLatLon(sortedItem[0])
            sortedItem.append(latlon[0])
            sortedItem.append(latlon[1])

        print('\t retrieving node id')
        # for sortedItem in self.organisedData:
        #     coordString =str(sortedItem[2]) + "," + str(sortedItem[3])
        #     nodeID = self.getNodeID(coordString)
        #     sortedItem.append(nodeID)
        # print(sortedItem)
        self.header = ['station name', 'cycle', 'lat', 'long']
        # print(self.header)
        self.organisedData.insert(0, self.header)
        print("Data Cleaned and Organised.")
        # print(self.organisedData)
        return self.organisedData

    def cycleGroupCounter(self):
        var = self.getGroupCounter()
        return var
