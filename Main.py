import CleanOrganise, Retrieve, MetaData

class Main:
    filePath = ''
    data = []
    def __init__(self):
        filePath = './data/01aJourneyDataExtract10Jan16-23Jan16.csv'
        retrieveObj = Retrieve.Retrieve(filePath)
        data = retrieveObj.getData("csv")
        # cleanOrganiseObj = CleanOrganise.CleanOrganise(data)
        # cleanOrganiseObj.cleanData(5)
        MetaData.MetaData(data,filePath)


if __name__ == "__main__":
    Main()
