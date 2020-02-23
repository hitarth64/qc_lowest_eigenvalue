# qc_lowest_eigenvalue
Routine to find lowest eigenvalue of a given matrix using quantum computing techniques (self composed VQE-esque)

Uses [Pyquil](https://github.com/rigetti/pyquil)

* pauli_decomposition.py: Decomposes any 4x4 matrix into individual Pauli terms
* calculator.py: Calculates the lowest eigenvalue given a PauliTerm expression for the Hamiltonian / matrix
* solution.ipynb: Notebook to demonstrate the flow
