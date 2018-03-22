import csv
class Retrieve:
    counter = 0
    data = []
    filePath = ""
    def __init__(self,fp):
        self.data = []
        self.filePath = fp

    def setFilePath (self,txt):
        self.filePath = txt

    # Just For CSV files
    def getCSV(self):
        with open(self.filePath) as csvfile:
            csvData = csv.reader(csvfile, delimiter=',')
            i = 0
            for item in csvData:
                self.data.append([])
                for j in range(len(item)):
                    self.data[i].append(item[j])
                i+=1
                self.counterPlus()

    def counterPlus(self):
        self.counter += 1

    def getCounter(self):
        return self.counter

    def getData(self,type):
        print("Retrieving Data...")
        if type == "csv":
            self.getCSV()
        print("Data Retrieved.")
        # print(self.data)
        return self.data
