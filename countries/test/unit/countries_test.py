import unittest
from countries.countries import get_country_code

class TestCountryCode(unittest.TestCase):
    """Tests for name_function.py"""

    def test_andorra(self):
        self.assertEqual(get_country_code('Andorra'), 'ad')

    def test_unknown_country(self):
        self.assertEqual(get_country_code('Steve'), None)

if __name__ == '__main__':
    unittest.main()