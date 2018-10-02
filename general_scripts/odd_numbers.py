import unittest

class TestUM(unittest.TestCase):
    def setUp(self):
        pass
    def test_odds_5(self):
        self.assertEqual( count_odds([1,3,5,7,9]),5)
    def test_odds_10(self):
        self.assertEqual( count_odds([1,3,5,7,9,3,5,7,3,5]),10)
    def test_odds_0(self):
        self.assertEqual( count_odds([2,4,6,8,10,20]),0)


def count_odds(numlist):
    num = 0
    for i in numlist:
        if i % 2 != 0:
            num += 1
    return num

if __name__ == '__main__':
    unittest.main()

