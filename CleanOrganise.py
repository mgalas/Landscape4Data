import requests, json
import Retrieve as retrieve

class CleanOrganise:
    data = []

    def __init__(self,d):
        self.data = d

    def cleanData(self):
        for item in self.data:
            print (item)

retrieveObj = retrieve.Retrieve('../01aJourneyDataExtract10Jan16-23Jan16.csv')
cleanOrganiseObj = CleanOrganise(retrieveObj.getData())
cleanOrganiseObj.cleanData()
