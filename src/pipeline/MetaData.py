import os
class MetaData:
    filePath = ''
    fileName = ''
    dataFromFile = []
    header = []
    fileDetails = []
    metaTags = []
    metaData = []
    def __init__(self,dataFromFile,filePath):
        self.dataFromFile = []
        self.header = []
        self.fileDetails = []
        self.metaTags = []
        self.metaData = []
        self.header = dataFromFile[0]
        self.dataFromFile = dataFromFile[1:]
        self.filePath = filePath


    def getFileDetails(self):
        data = os.stat(self.filePath)
        return data

    def askForMetaTags(self):
        moreInput = True
        while moreInput:

            response = input("Menu: \n1. List Meta Tags \n2. Add Meta Tag \n3. Remove Meta Tag \n4. Confirm \n\n")
            if response == 1:
                self.listMetaTags()
            elif response == 2:
                self.addMetaTag()
            elif response == 3:
                self.removeMetaTag()
            elif response == 4:
                moreInput = False
            else:
                print("Invalid Input, Please try again")


    def listMetaTags(self):
        print("List of Meta Tags")
        print(self.metaTags)

    def addMetaTag(self):
        isCorrect = False
        newTag = None
        while not isCorrect:
            try:
                newTag = input("Please type in Meta Tag in between two quotation marks and hit enter \n\n")
                print(newTag)
            except SyntaxError:
                print("Please try again")
                self.addMetaTag()
            confirm = input("Is this correct? \nType 1 for yes 2 for no \n\n")
            if confirm == 1:
                isCorrect = True
        self.metaTags.append(newTag)

    def removeMetaTag(self):
        isDone = False
        index = 0
        while not isDone:
            self.listMetaTags()
            index = int(input("Please type in the position of the meta tag to be removed. \n\n"))
            print(self.metaTags[index-1])
            confirm = input("Is this the tag you wish to delete? \nType 1 for yes 2 for no \n\n")
            if confirm == 1:
                isDone = True
        del self.metaTags[index-1]

    def getData(self):
        print("Collecting Meta Data...")
        self.askForMetaTags()
        self.fileDetails = self.getFileDetails()
        self.metaData.append([self.fileDetails])
        # self.metaTags = ['station name', 'cycle', 'lat', 'long', 'id']
        self.metaData.append(self.metaTags)
        print("Meta Data Collected.")
        return (self.metaData)
