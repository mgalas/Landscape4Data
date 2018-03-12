import requests, time
from geopy.geocoders import Nominatim


class CleanOrganise:
    dataFromFile = []
    organisedData = []
    header = []
    groupCounter = 0 #for testing

    def __init__(self,d):
        self.dataFromFile = []
        self.organisedData = []
        self.header = []
        self.dataFromFile = d
        self.header = self.dataFromFile[0]
        self.dataFromFile = self.dataFromFile[1:]

    def inObj (self,queryValue):
        pos = 0
        if (len(self.organisedData) == 0):
            return False,pos
        for data in self.organisedData:
            if data[0] == queryValue:
                return True,pos
            pos += 1
        return False,pos

    def addInObj (self,newValue):
        self.organisedData.append([newValue,1])

    def updateCount (self,pos):
        self.organisedData[pos][1] += 1

    def groupStationID (self,groupValue):
        boolVal,pos = self.inObj(groupValue)
        if not boolVal:
            self.addInObj(groupValue)
        else:
            self.updateCount(pos)
            self.groupCounterPlus()

    def TFLaddToCache(self,stName, dataFromApi):
        with open("./data/cache/tfl_api_cache.txt", "a+") as cache:
            cache.write(str(stName) + "@" + str(dataFromApi.get("lat")) + "#" + str(dataFromApi.get("lon")) + "\n")

    def TFLgetFromCache(self,stName):
        try:
            with open("./data/cache/tfl_api_cache.txt", "r") as cache:
                for line in cache:
                    data = line.split("@")
                    if data[0] == stName:
                        return ([True,data[1]])
        except Exception as e:
            return ([False,''])

        return ([False,''])

    def tflApi(self,item):
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
            self.TFLaddToCache(item, indObj)
        return (indObj)

    def getLatLon(self,stationName):
        res = None
        dataFromCache = self.TFLgetFromCache(stationName)
        lat = ''
        lon = ''
        if dataFromCache[0] == False:
            res = self.tflApi(stationName)
            if not (res == None):
                lat = res.get('lat')
                lon = res.get('lon')
        else:
            lat,lon = dataFromCache[1].split("#")

        return ([lat,lon])

    def OSMaddToCache(self,coordStr, osmID):
        with open("./data/cache/osm_api_cache.txt", "a+") as cache:
            cache.write(str(coordStr) + "@" + str(osmID) + "\n")

    def OSMgetFromCache(self,coordStr):
        try:
            with open("./data/cache/osm_api_cache.txt", "r") as cache:
                for line in cache:
                    data = line.split("@")
                    if data[0] == coordStr:
                        return (data[1])
        except Exception as e:
            return ("")
        return ("")

    def getNodeID(self,coordStr):
        dataFromApi = self.OSMgetFromCache(coordStr)
        if dataFromApi == "":
            geolocator = Nominatim()
            try:
                location = geolocator.reverse(coordStr)
                self.OSMaddToCache(coordStr,location.raw['osm_id'])
                time.sleep(1)
                return (location.raw['osm_id'])
            except Exception as e:
                return ("")
        else:
            return dataFromApi
        return ("")


    def groupCounterPlus(self):
        self.groupCounter += 1

    def getGroupCounter(self):
        return self.groupCounter

    def cleanData(self,dataValue):
        print("Cleaning and Organising Data...")
        self.organisedData = []
        for item in self.dataFromFile:
            self.groupStationID(item[dataValue])

        print('\t retrieving lat and long')

        self.counter = 0
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
