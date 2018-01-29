import CleanOrganise, Retrieve

class Main:
    def __init__(self):
        retrieveObj = Retrieve.Retrieve('../01aJourneyDataExtract10Jan16-23Jan16.csv')
        cleanOrganiseObj = CleanOrganise.CleanOrganise(retrieveObj.getData())
        cleanOrganiseObj.cleanData(5)

if __name__ == "__main__":
    Main()
