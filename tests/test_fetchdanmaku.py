import unittest


from src.spider_objout.spider.fetchdanmaku import FetchDanmaku
from src.spider_objout.spider.utils.fetch import Fetch


class TestFetchdanmaku(unittest.TestCase):
    def test_fetchdanmaku(self):
        fet = Fetch()
        fdan = FetchDanmaku(fet)

        self.assertIsNone(fdan.fetchdanmaku())
        fdan.fetchdanmaku('123')


if __name__ == "__main__":
    unittest.main()
