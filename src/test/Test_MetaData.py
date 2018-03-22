import unittest
from src.pipeline.MetaData import MetaData

class Test_MetaData (unittest.TestCase):

    def setUp (self):
        self.data = [ ["Frith Street, Soho",1,51.513103,-0.131213,349937283],
        ["Victoria Park Road, Hackney Central",1,51.536424,-0.054162,469788549],
        ["Baylis Road, Waterloo",1,51.501444,-0.110699,264835734],
        ["Hewison Street, Old Ford",1,51.533283,-0.028155,1818809538],
        ["Brick Lane Market, Shoreditch",1,51.522617,-0.071653,1322524169],
        ["Parsons Green Station, Parsons Green",1,51.475089,-0.201968,3662252439],
        ["Jubilee Street, Stepney",1,51.515975,-0.053177,395349093]]
        self.filePath = '../../data/test_Meta.csv'
        self.metaDataObj= MetaData(self.data, self.filePath)
        self.metaDataObjTwo= MetaData(self.data, self.filePath)
        self.metaDataObjThree = MetaData(self.data, self.filePath)


    def test_viewMetaTag(self):
         # default <'station name','cycle','lat','long','id'> in the user input
        self.assertEqual(self.metaDataObj.getData(), [['station name','cycle','lat','long','id']])

    def test_listMetaTags(self):
        # test that the initial list is empty
        #  print(self.metaDataObj.listMetaTags())
        self.assertTrue(self.metaDataObj.metaTags ==  [])

    def test_addMetaTags(self):
        print('Test To Add ')
        self.metaDataObjTwo.addMetaTag()
        self.assertFalse(self.metaDataObjTwo.metaTags == [])
        print(self.metaDataObjTwo.metaTags)

    def test_deleteMetaTags(self):
        print(" Test To Remove A New Tag ")
        self.metaDataObjThree.addMetaTag()
        self.metaDataObjThree.removeMetaTag()
        self.assertTrue(self.metaDataObjThree.metaTags == [])


if __name__ == "__main__":
    unittest.main()
