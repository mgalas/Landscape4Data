import os, Output

class MetaData:
    filePath = ''
    fileName = ''
    dataFromFile = []
    header = []
    fileDetails = []
    metaTags = []
    def __init__(self,dataFromFile,filePath):
        self.dataFromFile = []
        self.header = dataFromFile[0]
        self.dataFromFile = dataFromFile[1:]
        self.filePath = filePath
        self.askForMetaTags()


    def getFileDetails(self):
        data = os.stat(self.filePath)
        return data

    def askForMetaTags(self):
        moreInput = True
        while moreInput:
            response = input("Menu: \n1. List Meta Tags \n2. Add Meta Tag \n3. Remove Meta Tag \n4. Confirm \n\n")
            if response == "1":
                self.listMetaTags()
            elif response == "2":
                self.addMetaTag()
            elif response == "3":
                self.removeMetaTag()
            elif response == "4":
                moreInput = False
            else:
                print("Invalid Input, Please try again")


    def listMetaTags(self):
        print("List of Meta Tags")
        print(self.metaTags)

    def addMetaTag(self):
        isCorrect = False
        newTag = ""
        while not isCorrect:
            newTag = input("Please type in Meta Tag and hit enter \n\n")
            print(newTag)
            confirm = input("Is this correct? \nType 1 for yes 2 for no \n\n")
            if confirm == "1":
                isCorrect = True
        self.metaTags.append([newTag])

    def removeMetaTag(self):
        isDone = False
        index = 0
        while not isDone:
            self.listMetaTags()
            index = input("Please type in the position of the meta tag to be removed. \n\n")
            print(self.metaTags[index-1])
            confirm = input("Is this the tag you wish to delete? \nType 1 for yes 2 for no \n\n")
            if confirm == "1":
                isDone = True
        del self.metaTags[index-1]

    def getData(self):
        return (self.metaTags)
