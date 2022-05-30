import numpy as np 
from coeficients import *
from liebmann import *
from cria_malha import *


def function(M, i, j):
    '''
    função que retorna o resultado para V{i,j} com base em seus termos adjacentes.
    '''
    coef = compute_inside(sigma=3, deltaPhi=1, deltaR=2, R=1)
    adjacentes = np.array([M[i-1,j], M[i+1,j], M[i,j-1], M[i,j+1]]).reshape(4,1)

    print(f"COEF: {coef}")
    print(f"ADJ: {adjacentes}")

    return coef @ adjacentes