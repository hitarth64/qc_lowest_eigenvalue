from pyquil.paulis import PauliSum, PauliTerm

from collections import Counter
from typing import List, Union
import pyquil
import funcsigs
import numpy as np
from pyquil import Program
from pyquil.api import QuantumComputer, WavefunctionSimulator
from pyquil.api._qvm import QVM
from pyquil.gates import RX, RY, MEASURE, STANDARD_GATES
from pyquil.paulis import PauliTerm, PauliSum

H = PauliSum([ PauliTerm.from_list([("X",1),("X",0)],coefficient=0.5), PauliTerm.from_list([("Y",1),("Y",0)],coefficient=0.5), PauliTerm.from_list([("Z",1),("Z",0)],coefficient=0.5), 
            PauliTerm.from_list([("I",1),("I",0)],coefficient=-0.5) ]) 

# Decide n_qubits by size of your hamiltonian matrix
# depth decides the amount of entanglement between qubits
n_qubits = 2; depth = 3

def ansatz(params):
  p = Program()
  for i in range(depth):
    p += pyquil.gates.CNOT(1,0)
    for j in range(n_qubits):
      p += Program(RY(params[j],j))
  return p


def expectation_operator(hamiltonian, ansatz_):
  # ansatz_ should be a pyquil program
  # Hamiltonian is PauliSum object

  operator_progs = []
  operator_coeffs = []
  
  for p_term in hamiltonian.terms:
    op_prog = Program()
    for qindex, op in p_term:
        op_prog.inst(STANDARD_GATES[op](qindex))
    operator_progs.append(op_prog)
    operator_coeffs.append(p_term.coefficient)

  result_overlaps = WavefunctionSimulator().expectation(ansatz_, hamiltonian.terms)
  result_overlaps = list(result_overlaps)
  expectation = sum(list(map(lambda x: x[0] * x[1], zip(result_overlaps, operator_coeffs))))
  return expectation.real

angle_1 = np.linspace(0, 2*np.pi, 40)

liss = [expectation_operator(H,ansatz([i,j])) for i in angle_1 for j in angle_1] 

print(min(liss))
