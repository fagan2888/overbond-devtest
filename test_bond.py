import unittest
from bond import *

class TestBondMethods(unittest.TestCase):
    
    def test_correct_form(self):
        b = Bond("C1", "corporate", 3, 1.3)
        self.assertEqual(b.get_name(), "C1")
        self.assertEqual(b.get_type(), "corporate")
        self.assertEqual(b.get_term(), 3)
        self.assertEqual(b.get_yield(), 1.3)

    def test_invalid_type(self):
        with self.assertRaises(BondTypeError):
            b = Bond("G1", "prison", 3, 1.3)

    def test_invalid_term(self):
        with self.assertRaises(InvalidTermError):
            b = Bond("G1", "government", -3, 1.3)

    def test_invalid_yield(self):
        with self.assertRaises(InvalidYieldError):
            b = Bond("G1", "government", 3, -1.3)

    def test_term_difference(self):
        b1 = Bond("C1", "corporate", 3, 1.3)
        g1 = Bond("G1", "government", 4, 1.8)
        self.assertEqual(b1.term_difference(g1), 1)

    def test_yield_spread(self):
        b1 = Bond("C1", "corporate", 3, 1.3)
        g1 = Bond("G1", "government", 4, 1.8)
        self.assertEqual(b1.yield_spread(g1), 0.5)

        
if __name__ == '__main__':
    unittest.main()
