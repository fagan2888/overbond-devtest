from bond import Bond
from benchmarks import *
from curves import *

import csv

def bond_dict_maker(file):
    """
    Creates a dictionary of Bond objects by reading from a .csv file.

    @type file: str
    @rtype: dictionary
    """
    bonds = {}
    
    with open(file, "r") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            name = row[0]
            typ = row[1]

            # cleaning up data... needs to be in numerical form, so:
            # remove the word "years" from term...
            term = float(row[2].strip(" years"))

            # ... and remove '%' sign from yield
            yld = float(row[3].strip('%'))
            new_bond = Bond(name, typ, term, yld)
            bonds[name] = new_bond

    return bonds
            
def main():
    print("=============================")
    print("BOND YIELD SPREAD CALCULATOR")
    print("=============================\n")
    filename = input("Choose file to import bond data: ")

    # create dictionary of bonds to search from
    bond_dict = bond_dict_maker(filename)

    # ask user which calculation they would like to complete
    print("\nENTER 1 to calculate spread to government bond BENCHMARK")
    print("ENTER 2 to calculate spread to government bond CURVE")
    task = input("ENTER CHOICE HERE: ")

    # if invalid input (neither 1 nor 2 is selected), keep prompting
    while task != "1" and task != "2":
        print("\nInvalid choice! Try again.\n")
        print("ENTER 1 to calculate spread to government bond BENCHMARK")
        print("ENTER 2 to calculate spread to government bond CURVE")
        task = input("ENTER CHOICE HERE: ")

    # calculate yield spread to government bond BENCHMARK
    if int(task) == 1:
        print("\n-------")
        print("RESULTS")
        print("-------")
        print("bond,benchmark,spread_to_benchmark")
        yields_to_benchmark(bond_dict)
        
    # calculate yield spread to government bond CURVE
    if int(task) == 2:
        print("\n-------")
        print("RESULTS")
        print("-------")
        print("bond,spread_to_curve")
        yields_to_curve(bond_dict)
        
if __name__ == "__main__":
    main()
