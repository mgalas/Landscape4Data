import CleanOrganise, Retrieve, MetaData, Output, Audit, Match

class Main:
    filePath = ''
    metaFilePath = ''
    data = []
    auditData = []
    cleanedData = []
    metaData = []
    outputData = []
    def __init__(self):

        # self.filePath = './data/01aJourneyDataExtract10Jan16-23Jan16.csv'
        self.filePath = './data/test.csv'
        self.metaFilePath = self.filePath[:-4]
        self.metaFilePath = self.metaFilePath + "_META.csv"

        retrieveObj = Retrieve.Retrieve(self.filePath)
        self.data = retrieveObj.getData("csv")
        auditObj = Audit.Audit(self.data)
        self.auditData = auditObj.getAuditedData()

        cleanOrganiseObj = CleanOrganise.CleanOrganise(self.auditData)
        self.cleanedData = cleanOrganiseObj.cleanData(5)

        metaDataObj = MetaData.MetaData(self.data, self.filePath)
        self.metaData = metaDataObj.getData()
        newAuditObj = Audit.Audit(self.cleanedData)
        self.cleanedData = newAuditObj.getAuditedData()
        # print(self.cleanedData)
        self.outputData.append([self.metaData])
        self.outputData.append([self.cleanedData])

        Output.Output(self.outputData, self.metaFilePath, 2)

        Match.Match(self.metaFilePath)



if __name__ == "__main__":
    Main()
