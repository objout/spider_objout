import unittest

from src.spider_objout.spider.fetchvid import FetchVideoId
from src.spider_objout.spider.utils.fetch import Fetch


class Test_Fetchvid(unittest.TestCase):
    def test_fetchvid(self):
        fet = Fetch()
        fvid = FetchVideoId(fet)
        self.assertIsInstance(fvid.fetchvid(), list)
        self.assertIsInstance(fvid.fetchvid(kwd='English'), list)
        self.assertIsInstance(fvid.fetchvid(kwd='English', page=1), list)
        self.assertIsInstance(fvid.fetchvid(kwd='English', page=0), list)
        self.assertIsInstance(fvid.fetchvid(page=0), list)
        self.assertIsInstance(fvid.fetchvid(page=-1), list)
        self.assertIsInstance(fvid.fetchvid(page=1), list)

    def test_parse(self):
        fet = Fetch()
        fvid = FetchVideoId(fet)
        self.assertIsInstance(fvid.parse(), list)
        self.assertIsInstance(fvid.parse("hello world"), list)

    def test_getparams(self):
        fet = Fetch()
        fvid = FetchVideoId(fet)
        self.assertIsInstance(fvid.getparams(-1), dict)
        self.assertIsInstance(fvid.getparams(1), dict)
        self.assertIsInstance(fvid.getparams(100), dict)
        self.assertIsInstance(fvid.getparams(), dict)


if __name__ == "__main__":
    unittest.main()
