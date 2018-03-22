import unittest
from src.pipeline.Match import Match
from pathlib import Path
import xml.etree.ElementTree as ET

class Test_MetaData (unittest.TestCase):
    def setUp(self):
        self.metaFilePath = '../../data/test_META.csv'
        self.expectedResultPath = '../../data/expectedXMLResult.osm'
        self.osmFilePath = '../../data/test_META.osm'
        self.matchObj = Match(self.metaFilePath)
        self.my_file = Path('../../data/test_META.osm')

    def test_XMLProduced(self):
        #check that an osm file is produced
        self.assertTrue(self.my_file.is_file())

    def test_CorrectReading(self):
        expect = ET.parse(self.expectedResultPath).getroot()
        expectData = []
        outputData = []
        for child in expect:
            value= (child.tag, child.attrib)
            expectData.append(value)
        output = ET.parse(self.osmFilePath).getroot()
        for child in output:
            value = (child.tag, child.attrib)
            outputData.append(value)
        print(outputData)
        self.assertEqual(expectData, outputData)

if __name__ == "__main__":
    unittest.main()
