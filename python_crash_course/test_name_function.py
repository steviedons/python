import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for name_function.py"""

    def test_first_last_name(self):
        """Do names like Stephen Donovan work?"""
        formatted_name = get_formatted_name('stephen', 'donovan')
        self.assertEqual(formatted_name, 'Stephen Donovan')

    def test_first_middle_last_name(self):
        """Do names like Stephen Nicholas Donovan work?"""
        formatted_name = get_formatted_name('stephen', 'donovan', 'Nicholas')
        self.assertEqual(formatted_name, 'Stephen Nicholas Donovan')


unittest.main()

"""
Some of the Assert Methods Available from the unittest Module
Method Use
assertEqual(a, b) Verify that a == b
assertNotEqual(a, b) Verify that a != b
assertTrue(x) Verify that x is True
assertFalse(x) Verify that x is False
assertIn(item, list) Verify that item is in list
assertNotIn(item, list) Verify that item is not in list
"""
