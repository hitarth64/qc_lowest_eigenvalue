import pyquil
from pyquil.quilatom import quil_cos, quil_sin, Parameter
from pyquil.quilbase import DefGate
import numpy as np

theta = Parameter('theta')

t1 = np.kron(pyquil.gate_matrices.I,pyquil.gate_matrices.X)
t2 = np.kron(pyquil.gate_matrices.H,pyquil.gate_matrices.I)

CX_array = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
tmid = np.diag([quil_cos(theta/2) -1j * quil_sin(theta/2), quil_cos(theta/2) -1j * quil_sin(theta/2), quil_cos(theta/2) + 1j * quil_sin(theta/2), quil_cos(theta/2) + 1j * quil_sin(theta/2)])

# our ansatz is of the form: (IX) CX (RZ I) (HI) |00> 
# This is equivalent to: (t1) CX_array (tmid) (t2) |00> 

# inp_bit = [1,0,1,0]

gate_matrix = np.matmul(np.matmul(np.matmul(t1,CX_array),tmid),t2)
gate_definition = DefGate('new_gate', gate_matrix, [theta])

def ansatz(params):
  return Program(gate_definition(params[0],0))

def expectation(params):

  samples = 10000
  prog = ansatz(params)

  # Measure
  ro = prog.declare('ro', 'BIT', 1) # Classical registry storing the results
  prog.measure(0, ro[0])

  # Compile and execute
  prog.wrap_in_numshots_loop(samples)
  prog_exec = qc.compile(prog)
  ret = qc.run(prog_exec)

  # Calculate expectation
  freq_is_0 = [trial[0] for trial in ret].count(0) / samples
  freq_is_1 = [trial[0] for trial in ret].count(1) / samples

  return freq_is_0 - freq_is_1


out = t1.dot(CX_array.dot(tmid.dot(t2.dot([1,0,1,0]))))  
