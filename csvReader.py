import csv, requests, json


stationIDObj = [];
pos = 0;


#Have to work on this part
def tflApi(item):
    urlQueryid = item.replace(" ","%20")
    url = "https://api.tfl.gov.uk/BikePoint/Search?query="+urlQueryid+"&app_key=c9dcd95b35785f8c19a41ce2d384ea41&app_id=3ccf74d3"
    response = requests.get(url)
    indObj = response.json()[0]
    return (indObj)

def getLatLon(str):
        res = tflApi(str)
        lat = res.get('lat')
        lon = res.get('lon')
        return ([lat,lon])


#Till here!!!!!!!!!!!!!!!!!!!!

def groupStationID (stationID):
    if (inObj(stationID) == False):
        addInObj(stationID)
    else:
        updateCount(stationID)

def inObj (stdID):
    pos = 0
    if (len(stationIDObj) == 0):
        return False
    for item in stationIDObj:
        if item[0] == stdID:
            return True
        pos += 1
    return False


def addInObj (stdID):
    # latlon = getLatLon(stdID)
    stationIDObj.append([stdID,1
    #latlon[0],latlon[1]
    ])


def updateCount (stationID):
    stationIDObj[pos][1] += 1

with open('../01aJourneyDataExtract10Jan16-23Jan16.csv', newline='') as csvfile:
    tflReader = csv.reader(csvfile, delimiter=',')
    i = 0
    for row in tflReader:
        if (i != 0):
            stationID = row[5]
            # stationID = stationID[1:]
            groupStationID(stationID)
        i += 1
    print(stationIDObj)
