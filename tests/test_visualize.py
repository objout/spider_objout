import unittest

from src.spider_objout.visualizing.visualize import Visualize


class TestVisualize(unittest.TestCase):
    def test_run(self):
        v = Visualize('no.xlsx')
        self.assertRaises(Exception, v.run)


if __name__ == "__main__":
    unittest.main()
