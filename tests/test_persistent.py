import unittest

from spider_objout.persistent.persistent import Persistent


class TestPersis(unittest.TestCase):
    def test_persis(self):
        p = Persistent()
        self.assertRaises(Exception, p.read)
        self.assertRaises(Exception, p.write)


if __name__ == "__main__":
    unittest.main()
