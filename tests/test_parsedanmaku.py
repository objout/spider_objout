import unittest

from src.spider_objout.spider.parsedanmaku import ParseDanmaku


class TestParseDanmaku(unittest.TestCase):
    def test_parse(self):
        fpd = ParseDanmaku()
        self.assertRaises(Exception, fpd.parse)
        self.assertRaises(Exception, fpd.parse, 'hello')


if __name__ == "__main__":
    unittest.main()
