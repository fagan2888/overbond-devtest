def benchmark_finder(corporate_bond, bond_dict):
    """
    Finds government bond benchmark (government bond with
    closest term to corporate_bond) for a single
    corporate bond.

    @type bond_dict: dictionary
    @rtype: Bond
    """
    min_diff = None
    benchmark = None
    for key, value in bond_dict.items():
        if value.get_type() == "government":
            diff = corporate_bond.term_difference(value)
            if min_diff == None:
                min_diff = diff
                benchmark = value
            elif min_diff > diff:
                min_diff = diff
                benchmark = value
    return benchmark

def yields_to_benchmark(bond_dict):
    """
    Finds government bond benchmark for every corporate
    bond in a dictionary of bonds.

    @type bond_dict: dictionary
    @rtype: None
    """
    for key, bond in bond_dict.items():
        if bond.get_type() == "corporate":
            benchmark = benchmark_finder(bond, bond_dict)           
            spread = str(round(benchmark.yield_spread(bond), 2))
            print(bond.get_name() + "," + benchmark.get_name() \
                                        + "," + spread + "%")
