import unittest
from Retrieve import Retrieve

class Test_Retrieve (unittest.TestCase):
    def setUp (self):
        self.retrieve = Retrieve('./data/trial.csv')
        self.emptyfile = Retrieve('./data/ti.csv')

    def test_wrongFile(self):
        data = self.emptyfile.getData("csv")
        self.assertEqual(data[0], [])

    def test_header(self):
        data = self.retrieve.getData("csv")
        self.assertEqual(data[0], ['Station name', 'Location', 'Frequency', 'lat', 'long'])

    def read_data_point(self):


if __name__ == "__main__":
    unittest.main()
