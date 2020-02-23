# qc_lowest_eigenvalue
Calculates lowest eigenvalue of a given matrix using self composed VQE (actually VQE-esque) routine. 

# Dependencies:
* Numpy
* [Pyquil](https://github.com/rigetti/pyquil)
* Grove

# Content description:

* pauli_decomposition.py: Decomposes any 4x4 matrix into individual Pauli terms
* calculator.py: Calculates the lowest eigenvalue given a PauliTerm expression for the Hamiltonian / matrix
* solution.ipynb: Notebook to demonstrate the flow
