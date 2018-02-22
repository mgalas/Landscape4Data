import unittest, csv
from Main import Main

class Test_E2E (unittest.TestCase):

    def setUp(self):
        # self.inputPath = './data/test_2.csv'
        # self.main = Main()
        self.outputMETAPath = './data/test_META.csv'
        self.outputXMLPATH = './data/test_META.xml'

    #
    def test_checkMETA(self):
        with open(self.outputMETAPath, "r") as f:
            reader = csv.reader(f, delimiter = ',')
            readerData = list(reader)
            print(readerData)
        self.assertEqual(readerData, [['station name', 'occurence', 'lat', 'long', 'id'], ['Frith Street, Soho', '1', '51.513103', '-0.131213', '349937283'], ['Victoria Park Road, Hackney Central', '1', '51.536424', '-0.054162', '469788549'], ['Baylis Road, Waterloo', '1', '51.501444', '-0.110699', '264835734'], ['Hewison Street, Old Ford', '1', '51.533283', '-0.028155', '1818809538'], ['Brick Lane Market, Shoreditch', '1', '51.522617', '-0.071653', '1322524169'], ['Parsons Green Station, Parsons Green', '1', '51.475089', '-0.201968', '3662252439'],['Jubilee Street, Stepney', '1', '51.515975', '-0.053177', '395349093'],['Imperial Wharf Station', '1', '51.474665', '-0.183165', '4405961993']])

    def test_checkOSM (self):
        import xml.etree.ElementTree as ET
        list = []
        tree = ET.parse(self.outputXMLPATH)
        root = tree.getroot()
        for child in root:
            list.append(child.tag)
            list.append(child.attrib)
        self.assertEqual(list, ['node', {'id': '349937283', 'action': 'modify', 'lat': '51.513103', 'lon': '-0.131213', 'visible': 'true'}, 'node', {'id': '469788549', 'action': 'modify', 'lat': '51.536424', 'lon': '-0.054162', 'visible': 'true'}, 'node', {'id': '264835734', 'action': 'modify', 'lat': '51.501444', 'lon': '-0.110699', 'visible': 'true'}, 'node', {'id': '1818809538', 'action': 'modify', 'lat': '51.533283', 'lon': '-0.028155', 'visible': 'true'}, 'node', {'id': '1322524169', 'action': 'modify', 'lat': '51.522617', 'lon': '-0.071653', 'visible': 'true'}, 'node', {'id': '3662252439', 'action': 'modify', 'lat': '51.475089', 'lon': '-0.201968', 'visible': 'true'}, 'node', {'id': '395349093', 'action': 'modify', 'lat': '51.515975', 'lon': '-0.053177', 'visible': 'true'}, 'node', {'id': '4405961993', 'action': 'modify', 'lat': '51.474665', 'lon': '-0.183165', 'visible': 'true'}, 'node', {'id': '4320819428', 'action': 'modify', 'lat': '51.466633', 'lon': '-0.169821', 'visible': 'true'}, 'node', {'id': '151490715', 'action': 'modify', 'lat': '51.500353', 'lon': '-0.217515', 'visible': 'true'}, 'node', {'id': '926239874', 'action': 'modify', 'lat': '51.489479', 'lon': '-0.115156', 'visible': 'true'}, 'node', {'id': '469789692', 'action': 'modify', 'lat': '51.481747', 'lon': '-0.124642', 'visible': 'true'}, 'node', {'id': '425411529', 'action': 'modify', 'lat': '51.511542', 'lon': '-0.056667', 'visible': 'true'}, 'node', {'id': '1726420906', 'action': 'modify', 'lat': '51.528224', 'lon': '-0.037471', 'visible': 'true'}, 'node', {'id': '4296066373', 'action': 'modify', 'lat': '51.525941', 'lon': '-0.036017', 'visible': 'true'}, 'node', {'id': '98251552', 'action': 'modify', 'lat': '51.524868', 'lon': '-0.099489', 'visible': 'true'}, 'node', {'id': '884208380', 'action': 'modify', 'lat': '51.522264', 'lon': '-0.114079', 'visible': 'true'}, 'node', {'id': '1229122159', 'action': 'modify', 'lat': '51.518090', 'lon': '-0.163609', 'visible': 'true'}, 'node', {'id': '148878071', 'action': 'modify', 'lat': '51.522008', 'lon': '-0.151359', 'visible': 'true'}, 'node', {'id': '222182690', 'action': 'modify', 'lat': '51.532091', 'lon': '-0.061420', 'visible': 'true'}, 'node', {'id': '2060550141', 'action': 'modify', 'lat': '51.519265', 'lon': '-0.021345', 'visible': 'true'}])


if __name__ == "__main__":
    unittest.main()
