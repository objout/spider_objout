import unittest

from src.spider_objout.persistent.persistent import Persistent


class TestPersis(unittest.TestCase):
    def test_read(self):
        p = Persistent('1.xlsx')
        self.assertRaises(Exception, p.read)

        p = Persistent()
        self.assertRaises(Exception, p.read)


if __name__ == "__main__":
    unittest.main()
