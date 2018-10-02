import unittest

class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_clockwise_n_e(self):
        self.assertEqual( turn_clockwise("N"),"E")

    def test_clockwise_w_n(self):
        self.assertEqual( turn_clockwise("W"),"N")
    
    def test_clockwise_e_s(self):
        self.assertEqual( turn_clockwise("W"),"N")

    def test_clockwise_invalid_num(self):
        self.assertEqual(turn_clockwise(42), None)
    
    def test_clockwise_invalid_txt(self):
        self.assertEqual(turn_clockwise("rubbish"), None)

def turn_clockwise(initial_dir):
    """ 
    This function given a direction will return the next in the series
    """

    compass = ["N", "E", "S", "W"]
    if initial_dir in compass:
        if initial_dir == "N":
            return "E"
        elif initial_dir == "E":
            return "S"
        elif initial_dir == "S":
            return "W"
        elif initial_dir == "W":
            return "N"
 
if __name__ == '__main__':
    unittest.main()
