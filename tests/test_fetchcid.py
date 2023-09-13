import unittest

from src.spider_objout.spider.fetchcid import FetchCid
from src.spider_objout.spider.utils.fetch import Fetch


class Test_Fetchcid(unittest.TestCase):
    def test_parse(self):
        fet = Fetch()
        fcid = FetchCid(fet)
        self.assertIsInstance(fcid.parse(), str)
        self.assertRaises(Exception, fcid.parse, 'hello')
        self.assertRaises(Exception, fcid.parse, b'hello')

    def test_extractcid(self):
        fet = Fetch()
        fcid = FetchCid(fet)
        self.assertEqual(fcid.extractcid(
                         '__INITIAL_STATE__ "cid":12345,"abc'), '12345')
        self.assertEqual(fcid.extractcid(), -1)
        self.assertEqual(fcid.extractcid('hello'), -1)
        self.assertEqual(fcid.extractcid('"cid":123,'), -1)

    def test_fetchcid(self):
        fet = Fetch()
        fcid = FetchCid(fet)
        self.assertRaises(Exception, fcid.fetchcid)


if __name__ == "__main__":
    unittest.main()
