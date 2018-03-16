import requests
from src.CleanOrganise import CleanOrganise


class tflCycle(CleanOrganise):
    def __init__(self, data):
        super(tflCycle, self).__init__(data, '../data/cache/tfl_api_cache.txt')

    def apiCall(self,item):
        indObj = None
        urlQueryid = item.replace(" ","%20")
        url = "https://api.tfl.gov.uk/BikePoint/Search?query="+urlQueryid+"&app_key=192e25146670a8b781a9c53a01b3027f&app_id=9a47548b"
        response = requests.get(url)
        try:
            indObj = response.json()[0]
        except Exception as e:
            indObj = None
            # print("\t\tInvalid TFL API response")
        if not indObj == None:
            self.addToCache(item, indObj)
        return (indObj)


    def getLatLon(self, stationName):

        res = None

        apiDataFromCache = self.getFromCache(stationName)
        if apiDataFromCache == None:
            apiDataFromCache = [False, '']
        lat = ''
        lon = ''
        if apiDataFromCache[0] == False:

            res = self.apiCall(stationName)
            if not (res == None):
                lat = res.get('lat')
                lon = res.get('lon')
        else:

            lat, lon = apiDataFromCache[1].split("#")

        return ([lat, lon])

    def cleanData(self):
        print("Cleaning and Organising Data...")
        self.organisedData = []
        for item in self.dataFromFile:
            self.groupStationID(item[5])

            self.counter = 0
        print('\t retrieving lat and long')
        for sortedItem in self.organisedData:
            self.counter += 1
            latlon= self.getLatLon(sortedItem[0])
            sortedItem.append(latlon[0])
            sortedItem.append(latlon[1])

        print('\t retrieving node id')
        # for sortedItem in self.organisedData:
        #     coordString =str(sortedItem[2]) + "," + str(sortedItem[3])
        #     nodeID = self.getNodeID(coordString)
        #     sortedItem.append(nodeID)
            # print(sortedItem)
        print("Data Cleaned and Organised.")
        return (self.organisedData)

