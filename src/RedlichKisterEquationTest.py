from RedlichKisterEquation import RedlichKisterEquation
import unittest

class RedlichKisterEquationTest(unittest.TestCase):

    def test_method(self):
        order1 = RedlichKisterEquation.calculate([1, 2, 3], 0.1, 0.9, True)
        order2 = RedlichKisterEquation.calculate([1, 2, 3], 0.9, 0.1, True)
        
        assert(order1 != order2)
        
        # TODO: add more tests

if __name__ == '__main__':
    unittest.main()
