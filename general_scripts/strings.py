import unittest

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_compsci(self):
        self.assertEqual(remove_vowels("compsci"),"cmpsc")

    def test_aAB(self):
        self.assertEqual(remove_vowels("aAbEefIijOopUus"),"bfjps")

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    without = ""
    for i in s:
        if i not in vowels:
            without += i
    return without

if __name__ == '__main__':
#   unittest.main()
    s1 = "His name is {0}!".format("Arthur")
    print(s1)
