class Cache:
    cacheFile = ''
    def __init__(self,cacheFile):
        self.cacheFile = cacheFile

    def addToCache(self, stName, dataFromApi):
        with open(self.cacheFile, "a+") as cache:
            cache.write(str(stName) + "@" + str(dataFromApi.get("lat")) + "#" + str(dataFromApi.get("lon")) + "\n")

    def getFromCache(self, stName):
        try:
            with open(self.cacheFile, "r") as cache:
                for line in cache:
                    data = line.split("@")
                    if data[0] == stName:
                        return [True, data[1]]
        except Exception as e:
            return None
        return None
