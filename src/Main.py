import time
from src import Output, Match, Audit, MetaData, Retrieve, CleanOrganise, tflCycle, tflOysterCount


class Main:
    filePath = ''
    metaFilePath = ''
    data = []
    auditData = []
    cleanedData = []
    metaData = []
    outputData = []

    def __init__(self):
        start_time = time.time()

        self.filePath1 = '../data/cycle/01aJourneyDataExtract10Jan16-23Jan16.csv'
        self.filePath2 = '../data/oyster card/Nov09JnyExport.csv'

        self.filePath = [self.filePath1, self.filePath2]

        for i in range(2):
            self.metaFilePath = self.filePath[i][:-4]
            self.metaFilePath = self.metaFilePath + "_META.csv"
            retrieveObj = Retrieve.Retrieve(self.filePath[i])
            self.data = retrieveObj.getData("csv")
            auditObj = Audit.Audit(self.data)
            self.auditData = auditObj.getAuditedData()
            if i == 0:
                cleanOrganiseObj = tflCycle.tflCycle(self.auditData)
            else:
                cleanOrganiseObj = tflOysterCount.tflOysterCount(self.auditData)
            self.cleanedData = cleanOrganiseObj.cleanData()
            metaDataObj = MetaData.MetaData(self.data, self.filePath[i])
            self.metaData = metaDataObj.getData()
            newAuditObj = Audit.Audit(self.cleanedData)
            self.cleanedData = newAuditObj.getAuditedData()
            self.outputData.append([self.metaData])
            self.outputData.append([self.cleanedData])
            Output.Output(self.outputData, self.metaFilePath, 2)

            Match.Match(self.metaFilePath)

            elapsed_time = time.time() - start_time
            print("Time = " + str(elapsed_time) + "\n")
            self.outputData = []


if __name__ == "__main__":
    Main()
