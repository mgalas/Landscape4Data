import csv, json

class Output:
    dataToBeWritten = []
    newfilePath = ""
    arrayType = 1;

    def __init__(self,data,filePath,arrayType):
        self.dataToBeWritten = data
        self.newfilePath = filePath
        self.arrayType = arrayType
        print(self.dataToBeWritten)
        self.writeToFile()

    def writeToFile(self):
<<<<<<< HEAD
        with open(self.newfilePath, "w+", newline='') as outputFile:
=======
        with open(self.newfilePath, "w+", newline= '') as outputFile:
>>>>>>> e35b32ec45ab7edc1a215c0bd14a0b4b50e65be2
            csvWriter = csv.writer(outputFile, delimiter=',')
            if self.arrayType == 2:
                for row in self.dataToBeWritten:
                    for item in row:
                        for data in item:
                            csvWriter.writerow(data)
            else:
                csvWriter.writerow(self.dataToBeWritten)
