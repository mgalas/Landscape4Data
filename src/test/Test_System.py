import unittest
from pathlib import Path
from src.pipeline.Main import Main

class Test_System(unittest.TestCase):
    def setUp(self):
        try:
            self.run_once(self.runMain())
        except (IndexError, ValueError) as e:
            pass
        self.metaOutput= '../../data/cycle/01aJourneyDataExtract10Jan16-23Jan16_META.csv'
        self.xmlOutput = '../../data/cycle/01aJourneyDataExtract10Jan16-23Jan16_CLEANED.osm'

    def test_META_Exist(self):
        input = Path(self.metaOutput)
        self.assertTrue(input.is_file())

    def test_OSM_Exist(self):
        input = Path(self.xmlOutput)
        self.assertTrue(input.is_file())

    def run_once(self, f):
        def wrapper(*args, **kwargs):
            if not wrapper.has_run:
                wrapper.has_run = True
                return f(*args, **kwargs)
        wrapper.has_run = False
        return wrapper

    # @run_once
    def runMain(macid):
        return Main()



if __name__ == "__main__":
    unittest.main()


