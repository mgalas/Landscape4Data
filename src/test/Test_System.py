import unittest
from src.Main import Main
from pathlib import Path

class Test_System(unittest.TestCase):
    def setUp(self):
        #change the file path in main to '../../data/test.csv'
        # Main()
        # self.input = '../../data/test.csv'
        self.metaOutput= '../../data/test_META.csv'
        self.xmlOutput = '../../data/test_META.osm'

    def test_META_Exist(self):
        input = Path(self.metaOutput)
        self.assertTrue(input.is_file())

    def test_OSM_Exist(self):
        input = Path(self.xmlOutput)
        self.assertTrue(input.is_file())



if __name__ == "__main__":
    unittest.main()


