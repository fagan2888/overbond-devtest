import unittest
from main import *

class TestBenchmarkMethods(unittest.TestCase):

    global bonds
    bonds = bond_dict_maker("data/sample_input.csv")

    def test_benchmark_finder(self):
        c1_bench = benchmark_finder(bonds["C1"], bonds)
        self.assertEqual(c1_bench.get_name(), "G1")

        c2_bench = benchmark_finder(bonds["C2"], bonds)
        self.assertEqual(c2_bench.get_name(), "G2")

        c3_bench = benchmark_finder(bonds["C3"], bonds)
        self.assertEqual(c3_bench.get_name(), "G3")

        c4_bench = benchmark_finder(bonds["C4"], bonds)
        self.assertEqual(c4_bench.get_name(), "G3")

        c5_bench = benchmark_finder(bonds["C5"], bonds)
        self.assertEqual(c5_bench.get_name(), "G4")

        c6_bench = benchmark_finder(bonds["C6"], bonds)
        self.assertEqual(c6_bench.get_name(), "G5")

        c7_bench = benchmark_finder(bonds["C7"], bonds)
        self.assertEqual(c7_bench.get_name(), "G6")

        
if __name__ == '__main__':
    unittest.main()
