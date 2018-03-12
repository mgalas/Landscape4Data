import csv, requests, json


stationIDObj = [];


def tflApi(item):
    urlQueryid = item.replace(" ","%20")
    url = "https://api.tfl.gov.uk/BikePoint/Search?query="+urlQueryid+"&app_key=c9dcd95b35785f8c19a41ce2d384ea41&app_id=3ccf74d3"
    response = requests.get(url)
    try:
        indObj = response.json()[0]
    except Exception as e:
        indObj = None
        print (e)

    return (indObj)

def getLatLon(str):
    res = tflApi(str)
    lat = ''
    lon = ''
    if not (res == None):
        lat = res.get('lat')
        lon = res.get('lon')
    return ([lat,lon])

def groupStationID (stationID):
    boolVal,pos = inObj(stationID)
    if not boolVal:
        addInObj(stationID)
    else:
        updateCount(stationID,pos)

def inObj (stdID):
    pos = 0
    if (len(stationIDObj) == 0):
        return False,pos
    for item in stationIDObj:
        if item[0] == stdID:
            return True,pos
        pos += 1
    return False,pos

def addInObj (stdID):
    stationIDObj.append([stdID,1])

def updateCount (stationID,pos):
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
    print ("Done Counting Now Getting Lat/Lon")
    for item in stationIDObj:
        latlon = getLatLon(item[0])
        item.append(latlon[0]);
        item.append(latlon[1]);
    print("Done!!")
    with open('./output.csv','w') as output:
        for sublist in stationIDObj:
            for item in sublist:
                output.write(str(item) + ',')
            output.write('\n')
