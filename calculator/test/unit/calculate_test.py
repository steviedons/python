import unittest
from calculator.calculate import Calculate

class TestCalculate(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculate()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))

    def test_add_method_returns_correct_result_fail(self):
        self.assertEqual(4, self.calc.add(2, 4))

    def test_assert_raises(self):
        self.assertRaises(TypeError, self.calc.add, "Hello", "World")

if __name__ == '__main__':
    unittest.main()