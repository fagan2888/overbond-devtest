# Bond Yield Spread Calculator

Reads input from a .csv file to calculate the yield spreads of one or more corporate bonds to either a government bond benchmark or to the government bond curve.

## How to use?

Run file 'main.py'. Follow the prompts on the screen: you will first be asked to enter the file to import bond data from, then to choose whether to calculate the yield spread using a benchmark or curve.

### Input format (for CSV file)

| bond   | type       | term        | yield |
|--------|------------|-------------|-------|
| C1     | corporate  | 10.3 years  | 5.30% |
| G1     | government | 9.4 years   | 3.70% |
| G2     | government | 12 years    | 4.80% |

## Technical Choices

Technologies/frameworks used: Python 3.6.5, unittest framework, csv library.

Being a simple application with no GUI, I chose to write a series of simple python scripts. Seperate files were used for operations specific to Challenge #1 and Challenge #2. The definition of the Bond object was also its own file. This was done for clarity and modularity purposes.

The Bond object stored the name, type (government or corporate), term, and yield. If the type given to the Bond was not government or corporate, a custom exception was raised.

After extracting the bond data from the input file using csv.reader, I used a modified hash table data structure  (Python dictionary) to store said data, the bond name field ("C1", "G1", etc.) as the key and the whole Bond object as the value. 

To find benchmarks--whether a single one or multiple points on the government bond curve (to be used in linear interpolation calculation)--I used a greedy algorithm. 

For each corporate bond, the difference between its term and each government bond was calculated. 

If this was less than the current minimum difference (or, when calculating for the curve in Challenge #2: the minimum difference for a longer or shorter term specifically), it became the new minimum difference, and the government bond became the new benchmark. 

Runtime of this algorithm is O(n^2). This is more efficiently than storing all the differences and having to sort it, which would make the algorithm at least O(n^2*logn).
