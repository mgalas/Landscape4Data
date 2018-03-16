import requests
from src.CleanOrganise import CleanOrganise


class tflOysterCount(CleanOrganise):
    def __init__(self, data):
        super(tflOysterCount, self).__init__(data, '../data/cache/tfl_api_Oyster_cache.txt')

    def apiCall(self,item):
        indObj = None
        urlQueryid = item.replace(" ", "%20")
        url = "https://api.tfl.gov.uk/StopPoint/Search?query="+urlQueryid+"&modes=tube&faresOnly=false&includeHubs=false&tflOperatedNationalRailStationsOnly=false&app_id=3ccf74d3&app_key=c9dcd95b35785f8c19a41ce2d384ea41"
        response = requests.get(url)
        try:
            indObj = response.json()
        except Exception as e:
            indObj = None
            # print("\t\tInvalid TFL API response")
        if indObj is not None and indObj.get('matches') is not None:
            if not len(indObj.get('matches')) == 0:
                self.addToCache(item, indObj.get('matches')[0])
                return (indObj)
        return None




    def getLatLon(self, stationName):
        lat = ''
        lon = ''
        if not stationName == "Bus":
            apiDataFromCache = self.getFromCache(stationName)
            if apiDataFromCache == None:
                apiDataFromCache = [False, '']
            if apiDataFromCache[0] == False:
                res = self.apiCall(stationName)
                if not (res == None):
                    lat = res.get('matches')[0].get('lat')
                    lon = res.get('matches')[0].get('lon')
            else:
                lat, lon = apiDataFromCache[1].split("#")

        return ([lat, lon])


    def cleanData(self):
        print("Cleaning and Organising Data...")
        self.organisedData = []
        for item in self.dataFromFile:
            self.groupStationID(item[4])
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


