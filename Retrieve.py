import csv
class Retrieve:
    data = []
    filePath = ""
    def __init__(self,fp):
        self.data = []
        self.filePath = fp

    def setFilePath (self,txt):
        self.filePath = txt

    # Just For CSV files
    def getCSV(self):
        with open(self.filePath, newline='') as csvfile:
            csvData = csv.reader(csvfile, delimiter=',')
            i = 0
            for item in csvData:
                self.data.append([])
                for j in range(len(item)):
                    self.data[i].append(item[j])
                i+=1
            self.data = self.data[1:]


    # So that Multipe types of data can be imported
    def getData(self):
        self.getCSV()
        return self.data
