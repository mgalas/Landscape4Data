import abc, six
# from src import Cache
import Cache

@six.add_metaclass(abc.ABCMeta)
class CleanOrganise():
    dataFromFile = []
    organisedData = []
    header = []
    groupCounter = 0 #for testing
    cacheObj = None

    @abc.abstractmethod
    def __init__(self, d, cacheLocation):
        self.dataFromFile = []
        self.organisedData = []
        self.header = []
        self.dataFromFile = d
        self.header = self.dataFromFile[0]
        self.dataFromFile = self.dataFromFile[1:]
        self.organisedData = []
        self.groupCounter = 0
        self.cacheObj = Cache.Cache(cacheLocation)

    def inObj (self, queryValue):
        pos = 0
        if (len(self.organisedData) == 0):
            return False,pos
        for data in self.organisedData:
            if data[0] == queryValue:
                return True, pos
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


    def addToCache(self,stName, dataFromApi):
        self.cacheObj.addToCache(stName,dataFromApi)

    def getFromCache(self,stName):
        return self.cacheObj.getFromCache(stName)

    # def OSMaddToCache(self, coordStr, osmID):
    #     with open("./data/cache/osm_api_cache.txt", "a+") as cache:
    #         cache.write(str(coordStr) + "@" + str(osmID) + "\n")
    #
    # def OSMgetFromCache(self, coordStr):
    #     try:
    #         with open("./data/cache/osm_api_cache.txt", "r") as cache:
    #             for line in cache:
    #                 data = line.split("@")
    #                 if data[0] == coordStr:
    #                     return (data[1])
    #     except Exception as e:
    #         return ("")
    #     return ("")
    #
    # def getNodeID(self, coordStr):
    #     dataFromApi = self.OSMgetFromCache(coordStr)
    #     if dataFromApi == "":
    #         geolocator = Nominatim()
    #         try:
    #             location = geolocator.reverse(coordStr)
    #             self.OSMaddToCache(coordStr, location.raw['osm_id'])
    #             time.sleep(1)
    #             return (location.raw['osm_id'])
    #         except Exception as e:
    #             return ("")
    #     else:
    #         return dataFromApi

    def groupCounterPlus(self):
        self.groupCounter += 1

    def getGroupCounter(self):
        return self.groupCounter


    @abc.abstractmethod
    def apiCall(self,item):
        pass

    @abc.abstractmethod
    def cleanData(self,dataValue):
        pass
