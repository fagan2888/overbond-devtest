import unittest
from main import *

class TestCurvesMethods(unittest.TestCase):

    global bonds
    bonds = bond_dict_maker("data/sample_input_challenge2.csv")

    def test_linear_interpolation(self):
        x1 = 9.4
        x2 = 12
        y1 = 3.70
        y2 = 4.80
        x = 10.3
        result = round(linear_interpolation(x, x1, y1, x2, y2), 2)
        self.assertEqual(result, 4.08)

        a1 = 12
        a2 = 16.3
        b1 = 4.80
        b2 = 5.50
        a = 15.2
        result = round(linear_interpolation(a, a1, b1, a2, b2), 2)
        self.assertEqual(result, 5.32)

    def test_curve_finder(self):
        corp_bond1 = bonds["C1"]
        spread = curve_finder(corp_bond1, bonds)
        self.assertEqual(spread, 1.22)

        corp_bond2 = bonds["C2"]
        spread = curve_finder(corp_bond2, bonds)
        self.assertEqual(spread, 2.98)

if __name__ == '__main__':
    unittest.main()
