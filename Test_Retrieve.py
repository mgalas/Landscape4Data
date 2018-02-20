import unittest, csv
from Retrieve import Retrieve

class Test_Retrieve (unittest.TestCase):
    address = './data/trial.csv'
    def setUp (self):
        self.retrieve = Retrieve(self.address)
    #     self.emptyfile = Retrieve('./data/ti.csv')
    #
    # def test_wrongFile(self):
    #     data = self.emptyfile.getData("csv")
    #     self.assertEqual(data[0], [])

    def test_header(self):
        data = self.retrieve.getData("csv")
        self.assertEqual(data[0], ['Station name', 'Location', 'Frequency', 'lat', 'long'])

    def test_data_point(self):
        data = self.retrieve.getData("csv")
        print(data[3])
        self.assertEqual(data[3][1], 'Waterloo')

    def test_Rows_No(self):
        data = self.retrieve.getData("csv")
        with open(self.address, "r") as f:
            reader = csv.reader(f, delimiter = ',')
            readerData = list(reader)
            row_count = len(readerData)
        self.assertEqual(self.retrieve.getCounter(), row_count)

if __name__ == "__main__":
    unittest.main()
