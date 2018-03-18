import unittest
from src.Audit import Audit

class Test_Audit (unittest.TestCase):

    def setUp (self):
        self.data = [['Rental Id', 'Duration', 'Bike Id', 'End Date', 'EndStation Id', 'EndStation Name', 'Start Date', 'StartStation Id', 'StartStation Name'],
         ['50754225', '240', '11834', '10/01/2016 00:04', '383', 'Frith Street, Soho', '10/01/2016 00:00', '18', 'Drury Lane, Covent Garden'],
         ['50754226', '300', '9648', '10/01/2016 00:05', '383', 'Victoria Park Road, Hackney Central', '10/01/2016 00:00', '479', 'Pott Street, Bethnal Green'],
         ['50754227', '1200', '10689', '10/01/2016 00:20', '272', 'Baylis Road, Waterloo', '10/01/2016 00:00', '425', 'Harrington Square 2, Camden Town'],
         ['50754228', '780', '8593', '10/01/2016 00:14', '471', 'Hewison Street, Old Ford', '10/01/2016 00:01', '487', 'Canton Street, Poplar'],
          ['50754229', '600', '8619', '10/01/2016 00:11', '399', 'Brick Lane Market, Shoreditch', '10/01/2016 00:01', '501', 'Cephas Street, Bethnal Green'],
          ['50754230', '420', '309', '10/01/2016 00:09', '671', 'Parsons Green Station, Parsons Green', '10/01/2016 00:02', "", 'Sandilands Road, Walham Green']]
        self.auditData = Audit(self.data).getAuditedData()


    def test_Remove(self):
        self.assertTrue(['50754230', '420', '309', '10/01/2016 00:09', '671', 'Parsons Green Station, Parsons Green', '10/01/2016 00:02', "", 'Sandilands Road, Walham Green'] not in self.auditData)

    def test_Rows_No(self):
       self.assertEqual(len(self.auditData), 6)


if __name__ == "__main__":
    unittest.main()
