class BondTypeError(Exception):
    """Raised when the bond is not government or corporate type."""
    pass

class InvalidTermError(Exception):
    """Raised when a bond is created with a term of
    negative number of years."""
    pass

class InvalidYieldError(Exception):
    """Raised when a bond is created with a negative yield."""
    pass

class Bond:
    def __init__(self, name, typ, term, yld):
        """
        Creates a bond with an identifier, type (corporate or government),
        term (number of years), and yield.

        @type self: Bond
        @type name: str
            The identifier for the bond.
        @type typ: str
            Type of bond: must be either "corporate" or "government".
        @type term: float
            Term of the bond, in years.
        @type yld: float
            Yield of the bond. Expressed as a percentage, without the sign.
        @rtype: None
        """

        # Error checking... make sure input is correct type:
        if typ != "corporate" and typ != "government":
            raise BondTypeError("Bonds must be of type corporate or government.")
        if term <= 0:
            raise InvalidTermError("Please enter a non-negative number of years")
        if yld <= 0:
            raise InvalidYieldError("Please enter a non-negative yield value")

        # Initialize Bond data structure
        self.name = name
        self.typ = typ
        self.term = term
        self.yld = yld

    def get_type(self):
        """Returns type of bond."""
        return self.typ

    def get_name(self):
        """Returns name of bond."""
        return self.name

    def get_term(self):
        """Returns term of bond."""
        return self.term

    def get_yield(self):
        """Returns yield of bond."""
        return self.yld

    def term_difference(self, other):
        """
        Returns the difference in years of the terms of Bond self
        and Bond other.
        """
        return abs(other.term - self.term)
    
    def yield_spread(self, other):
        """
        Returns the yield spread of Bond self and Bond other.
        """
        return abs(other.yld - self.yld)

        
