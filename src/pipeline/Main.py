import time
import src.pipeline.Output, src.pipeline.Match, src.pipeline.Audit, src.pipeline.MetaData, src.pipeline.Retrieve, \
    src.pipeline.tflCycle, src.pipeline.tflOysterCount

class Main:
    filePath = ''
    metaFilePath = ''
    data = []
    auditData = []
    cleanedData = []
    metaData = []
    outputData = []
    outputMeta= []

    def __init__(self):
        start_time = time.time()

        self.filePath1 = '../../data/cycle/01aJourneyDataExtract10Jan16-23Jan16.csv'
        self.filePath2 = '../../data/oyster card/Nov09JnyExport.csv'
        self.filePath = [self.filePath1, self.filePath2]




        for i in range(2):
            self.metaFilePath = self.filePath[i][:-4]
            self.metaFilePath = self.metaFilePath + "_META.csv"
            self.cleanOrganisedPath = self.filePath[i][:-4]
            self.cleanOrganisedPath = self.cleanOrganisedPath + "_CLEANED.csv"
            retrieveObj = src.pipeline.Retrieve.Retrieve(self.filePath[i])
            self.data = retrieveObj.getData("csv")
            auditObj = src.pipeline.Audit.Audit(self.data)
            self.auditData = auditObj.getAuditedData()
            if i == 0:
                cleanOrganiseObj = src.pipeline.tflCycle.tflCycle(self.auditData)
            else:
                cleanOrganiseObj = src.pipeline.tflOysterCount.tflOysterCount(self.auditData)
            self.cleanedData = cleanOrganiseObj.cleanData()

            metaDataObj = src.pipeline.MetaData.MetaData(self.data, self.filePath[i])
            self.metaData = metaDataObj.getData()
            newAuditObj = src.pipeline.Audit.Audit(self.cleanedData)

            self.cleanedData = newAuditObj.getAuditedData()
            self.outputData.append([self.cleanedData])
            src.pipeline.Output.Output(self.outputData, self.cleanOrganisedPath, 2)
            src.pipeline.Match.Match(self.cleanOrganisedPath)

            self.outputMeta.append([self.metaData])
            src.pipeline.Output.Output(self.outputMeta, self.metaFilePath, 2)
            elapsed_time = time.time() - start_time

            print("Time = " + str(elapsed_time) + "\n")
            self.outputData = []
            self.outputMeta =[]


if __name__ == "__main__":
    Main()
