# K-Means Subspace Clustering

This Python program implements the K-means algorithm for subspace clustering. It reads data from the "test.dat" input file, performs K-means clustering for a range of K values (from Kmin to Kmax), and calculates the Sum of Square Errors (SSE) for each clustering. The results are written to the "test.res" output file.

## Usage

1. Clone or download this repository to your local machine.

2. Make sure you have Python and NumPy installed.

3. Place your input data in the "kmeans_subspace.py" file for the specified variables (n, m, Kmin, Kmax, data) and the random data objects will be assumed by the program in range of 0 to 1 by placing them in 'test.dat' file.

4. Open a terminal in VSCode and navigate to the project directory.

5. Run the following command to execute the code:

   python kmeans_subspace.py

6. The results will be generated in the "test.res" file.

## Input Format

The "test.dat" input file should have the following format:

n m Kmin Kmax
a1d1 ...,a1dm
.
.
.
and1 ...,andm

- n: Total number of objects.
- m: Count of dimensions (attributes).
- Kmin: Minimum value of K to be tested.
- Kmax: Maximum value of K to be tested.
- Data: Data objects with m attributes.

## Output Format

The "test.res" output file contains K and SSE values for each K in the specified range, separated by a space.

## Dependencies

- Python
- NumPy


This `Readme.md` file provides an overview of project, how to use it, the input and output formats, and dependencies.