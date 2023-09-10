import unittest

from spider_objout.spider.utils.getheaders import getheaders, getcookie, \
    parsecookie


class TestGetheaders(unittest.TestCase):
    def test_getheaders(self):
        self.assertIsInstance(getheaders(), dict)
        self.assertIsInstance(getheaders('hello'), dict)

    def test_getcookie(self):
        self.assertIsInstance(getcookie(), str)
        self.assertIsInstance(getcookie(), str)

    def test_parsecookie(self):
        self.assertRaises(Exception, parsecookie)
        self.assertRaises(Exception, parsecookie, 'not exsits')


if __name__ == "__main__":
    unittest.main()
