import unittest

from src.spider_objout.spider.utils.fetch import Fetch
from urllib.request import Request


class TestFetch(unittest.TestCase):
    def test_reqwrapper(self):
        fet = Fetch()
        req = fet.reqwrapper('https://baidu.com', {"o": 1})
        self.assertIsInstance(req, Request)
        req = fet.reqwrapper('https://baidu.com', {})
        self.assertIsInstance(req, Request)

        self.assertRaises(Exception, fet.reqwrapper, '', {})

    def test_request(self):
        fet = Fetch()
        self.assertRaises(Exception, fet.request)

        req = fet.reqwrapper('https://baidu.com', {"o": 1})
        ret = fet.request(req)
        self.assertIsNotNone(ret)


if __name__ == "__main__":
    unittest.main()
