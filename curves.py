def curve_finder(corporate_bond, bond_dict):
    """
    Finds spread to the government bond curve for a single
    corporate bond.

    @type bond_dict: dictionary
    @rtype: float
    """

    # variables to store two benchmarks:
    # closest government bonds with longer term and shorter term
    min_diff_longer = None
    min_diff_shorter = None
    benchmark_high = None
    benchmark_low = None
    
    for key, value in bond_dict.items():
        if value.get_type() == "government":
            # get difference in term between corporate bond and government bond
            diff = corporate_bond.term_difference(value)

            # if longer term, update benchmark_high if it's the closest so far
            # with a longer term
            if value.get_term() > corporate_bond.get_term():
                if min_diff_longer == None:
                    min_diff_longer = diff
                    benchmark_high = value
                elif min_diff_longer > diff:
                    min_diff_longer = diff
                    benchmark_high = value

            # if shorter term, update benchmark_low if it's the closest so far
            # with a shorter term
            if value.get_term() < corporate_bond.get_term():
                if min_diff_shorter == None:
                    min_diff_shorter = diff
                    benchmark_low = value
                elif min_diff_shorter > diff:
                    min_diff_shorter = diff
                    benchmark_low = value

    # initialize variables for linear interpolation equation                
    y1 = benchmark_low.get_yield()
    y2 = benchmark_high.get_yield()
    x1 = benchmark_low.get_term()
    x2 = benchmark_high.get_term()
    x = corporate_bond.get_term()

    # calculte expected yield and return spread
    curve_yield = linear_interpolation(x, x1, y1, x2, y2)
    spread = abs(round(curve_yield - corporate_bond.get_yield(), 2))
    return spread

def linear_interpolation(x, x1, y1, x2, y2):
    """
    Finds yield of corporate bond on the government bond curve using
    the linear interpolation formula.

    @type x, x1, y1, x2, y2: float
    @rtype: float
    """
    yld = y1 + (x - x1)*((y2-y1)/(x2-x1))
    return yld

def yields_to_curve(bond_dict):
    """
    Finds government bond benchmark for every corporate
    bond in a dictionary of bonds.

    @type bond_dict: dictionary
    @rtype: None
    """
    for key, bond in bond_dict.items():
        if bond.get_type() == "corporate":
            bond_result = str(curve_finder(bond, bond_dict))
            print(bond.get_name() + "," + bond_result + "%")

