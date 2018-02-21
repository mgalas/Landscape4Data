#class to convert csv file in the current folder to osm xml format.
import csv,sys,os

class Match:

    def __init__(self,fp):
        self.filePath= fp
        self.csv2osm()

    def csv2osm(self):
        #for all csv files
        # csvFiles = [f for f in os.listdir('.') if f.endswith('.csv') or f.endswith('.CSV')]
        # for csvFile in csvFiles:
        print('export xml from csv')
        csvFile = self.filePath
        xmlFile=  csvFile[:-4] + '.osm'
        reader = csv.DictReader(open(csvFile))
        xmlData = open(xmlFile, 'w')
        xmlData.write('<?xml version="1.0" encoding="utf-8"?>' + "\n")
        xmlData.write('<osm version="0.6" generator="csvtoosm">' + "\n")
        for row in reader:
            i=-1
            # print(row['id'])
            if 'id' in row:
                osm_id = row['id']
                action = "modify"
            else:
                osm_id = i
                i -= 1
                action = "create"
            version = ''
            if 'version' in row:
                version = 'version="%s"' % row['version']
            xmlData.write('  <node id="%s" action="%s" lat="%f" lon="%f" %s visible="true">\n' %
            (osm_id, action, float(row['lat'].replace(',', '.')), float(row['long'].replace(',', '.')), version))
             # print key-value tags
            for k, v in row.items():
                if k != 'lat' and k != 'long' and v != '':
                 xmlData.write ('<tag k="%s" v="%s" />\n' %(k,v))
            xmlData.write('  </node>\n' )
        xmlData.write('</osm>' + "\n")
        xmlData.close()
