import unittest, csv
from MetaData import MetaData

class Test_MetaData (unittest.TestCase):

    def setUp (self):
        self.data = [ ["Frith Street, Soho",1,51.513103,-0.131213,349937283],
        ["Victoria Park Road, Hackney Central",1,51.536424,-0.054162,469788549],
        ["Baylis Road, Waterloo",1,51.501444,-0.110699,264835734],
        ["Hewison Street, Old Ford",1,51.533283,-0.028155,1818809538],
        ["Brick Lane Market, Shoreditch",1,51.522617,-0.071653,1322524169],
        ["Parsons Green Station, Parsons Green",1,51.475089,-0.201968,3662252439],
        ["Jubilee Street, Stepney",1,51.515975,-0.053177,395349093]]
        self.filePath = './data/test_Meta.csv'



    def test_listMetaTags(self):
        print("is the initial list empty")
        # print(self.metaDataObj.listMetaTags())
        metaDataObj = MetaData(self.data, self.filePath)
        self.assertTrue(metaDataObj.listMetaTags() ==  None)

    # def test_addMetaTag(self):
    #      metaDataobj2 = MetaData(self.data, self.filePath)
    #      metaDataobj2.addMetaTag()
    #      #type <'station name','cycle occurence','lat','long','id','extra'> in the user input
    #      self.assertEqual(metaDataObj2.metaTags, ['station name','cycle occurence','lat','long','id','extra'])
    # def test_removeMetaTag(self):
    #     # print(self.metaDataObj.metaTags)
    #     #delete the 6th position
    #     # self.metaDataObj.removeMetaTag()
    #     self.assertEqual(self.metaDataObj.metaTags,  ['station name','cycle occurence','lat','long','id'])
    # def test_getData(self):
    #     self.assertEqual(self.metaDataObj.getData()[0:4],  ['station name','cycle occurence','lat','long','id'])

if __name__ == "__main__":
    unittest.main()
