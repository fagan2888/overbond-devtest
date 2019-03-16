import unittest
from main import *
from test_bond import *
from test_benchmarks import *
from test_curves import *

class TestMainMethods(unittest.TestCase):

    global bonds
    bonds = bond_dict_maker("data/sample_input.csv")

    def test_bond_dict_maker(self):
        self.assertEqual(bonds["C1"].get_name(), "C1")
        self.assertEqual(bonds["C1"].get_type(), "corporate")
        self.assertEqual(bonds["C1"].get_term(), 1.3)
        self.assertEqual(bonds["C1"].get_yield(), 3.30)
        
        self.assertEqual(bonds["G1"].get_name(), "G1")
        self.assertEqual(bonds["G1"].get_type(), "government")
        self.assertEqual(bonds["G1"].get_term(), 0.9)
        self.assertEqual(bonds["G1"].get_yield(), 1.70)
        
        self.assertEqual(bonds["C7"].get_name(), "C7")
        self.assertEqual(bonds["C7"].get_type(), "corporate")
        self.assertEqual(bonds["C7"].get_term(), 22.9)
        self.assertEqual(bonds["C7"].get_yield(), 12.30)
        
        self.assertEqual(bonds["G6"].get_name(), "G6")
        self.assertEqual(bonds["G6"].get_type(), "government")
        self.assertEqual(bonds["G6"].get_term(), 24.2)
        self.assertEqual(bonds["G6"].get_yield(), 9.80)

if __name__ == '__main__':
    unittest.main()
