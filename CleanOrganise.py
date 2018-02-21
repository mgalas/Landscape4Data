import requests, json, Output
from geopy.geocoders import Nominatim


class CleanOrganise:
    dataFromFile = []
    organisedData = []
    header = []
    counter = 0

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

    def tflApi(self,item):
        urlQueryid = item.replace(" ","%20")
        url = "https://api.tfl.gov.uk/BikePoint/Search?query="+urlQueryid+"&app_key=192e25146670a8b781a9c53a01b3027f&app_id=9a47548b"
        response = requests.get(url)
        try:
            indObj = response.json()[0]
        except Exception as e:
            indObj = None
            print("Invalid TFL API response")
        return (indObj)

    def getLatLon(self,stationName):
        res = self.tflApi(stationName)
        lat = ''
        lon = ''
        if not (res == None):
            lat = res.get('lat')
            lon = res.get('lon')
        return ([lat,lon])

    def getNodeID(self,coordStr):
        geolocator = Nominatim()
        try:
            location = geolocator.reverse(coordStr)
            return (location.raw['osm_id'])
        except Exception as e:
            print("\t\t"+str(e))
        return ("")



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
        for sortedItem in self.organisedData:
            coordString =str(sortedItem[2]) + "," + str(sortedItem[3])
            nodeID = self.getNodeID(coordString)
            sortedItem.append(nodeID)
            # print(sortedItem)
        print("Data Cleaned and Organised.")
        return (self.organisedData)
