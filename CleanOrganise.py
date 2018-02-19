import requests, json, Output
from geopy.geocoders import Nominatim


class CleanOrganise:
    dataFromFile = []
    organisedData = []
    header = []


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
        url = "https://api.tfl.gov.uk/BikePoint/Search?query="+urlQueryid+"&app_key=c9dcd95b35785f8c19a41ce2d384ea41&app_id=3ccf74d3"
        response = requests.get(url)
        try:
            indObj = response.json()[0]
        except Exception as e:
            indObj = None
            print (e)
        return (indObj)

    def getLatLon(self,str):
        res = self.tflApi(str)
        lat = ''
        lon = ''
        if not (res == None):
            lat = res.get('lat')
            lon = res.get('lon')
        return ([lat,lon])
    def getNodeID(self,str):
        geolocator = Nominatim()
        location = geolocator.reverse(str)
        return (location.raw['osm_id'])


    def cleanData(self,dataValue):
        self.organisedData = []
        for item in self.dataFromFile:
            self.groupStationID(item[dataValue])
        print('now retrieving lat and long')
        for sortedItem in self.organisedData:
            latlon= self.getLatLon(sortedItem[0])
            sortedItem.append(latlon[0])
            sortedItem.append(latlon[1])

        print('now retrieving node id')
        for sortedItem in self.organisedData:
            coordString =str(sortedItem[2]) + "," + str(sortedItem[3])
            nodeID = self.getNodeID(coordString)
            sortedItem.append(nodeID)
            # print(sortedItem)
        return (self.organisedData)
