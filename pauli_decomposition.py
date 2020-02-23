import numpy as np
from numpy import kron

# Using the fact that aij = 1/2 * tr((si \tp sj)H) where sk is one of the Pauli matrices and H is the input matrix; 
# aij corresponds to the coefficient of the term with tensor product of Pauli matrix sigma_i and sigma_j

def HS(M1, M2):
    
    #Hilbert-Schmidt-Product of two matrices M1, M2
    
    return (np.dot(M1.conjugate().transpose(), M2)).trace()
        
def decompose(H):
    
    #Decompose input 4x4 matrix H into Pauli matrices
    
    sx = np.array([[0, 1],  [ 1, 0]], dtype=np.complex128)
    sy = np.array([[0, -1j],[1j, 0]], dtype=np.complex128)
    sz = np.array([[1, 0],  [0, -1]], dtype=np.complex128)
    id = np.array([[1, 0],  [ 0, 1]], dtype=np.complex128)
    S = [id, sx, sy, sz]
    labels = ['I', 'X', 'Y', 'Z']
    for i in range(4):
        for j in range(4):
            label = labels[i] + ' \tp ' + labels[j]
            a_ij = 0.5 * HS(kron(S[i], S[j]), H)
            if a_ij != 0.0:
                print("%s\t*\t( %s )" % (a_ij, label))
