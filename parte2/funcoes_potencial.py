import numpy as np

props_elet = {
    "sigma_A": 5e-6,
    "sigma_B": 1e-5,
}

"""
Todas as funcoes precisam das temperaturas da matriz
de temperatura e da coordenada atual, alem das prop
fisicas e eletricas

10 condicoes necessarias
- 0: borda superior de A
- 1: borda inferior de B (regiao de simetria)
- 2: borda esquerda de B
- 3: borda direita de B
- 4: borda esquerda de A
- 5: borda direita de A
- 6: borda inferior de A (regiao de simetria)
- 7: borda superior de B
- 8: interior de A
- 9: interior de B
"""

#0: borda superior de A
def sup_A(M, i, j, dr, dtheta):
    pass

#1: borda inferior de B (regiao de simetria)
def inf_B(M, i, j, dr, dtheta):
    pass

#2: borda esquerda de B
def esq_B(M, i, j, dr, dtheta):
    pass

#3: borda direita de B
def dir_B(M, i, j, dr, dtheta):
    pass

#4: borda esquerda de A
def esq_A(M, i, j, dr, dtheta):
    return 100

#5: borda direita de A
def dir_A(M, i, j, dr, dtheta):
    return 0

#6: borda inferior de A (regiao de simetria)
def inf_A(M, i, j, dr, dtheta):
    pass

#7: borda superior de B
def sup_B(M, i, j, dr, dtheta):
    pass

#8: interior de A
def inter_A(M, i, j, dr, dtheta):
    raio = 0.03 + i*dr
    angulo = j*dtheta #em radianos

    sigma = props_elet['sigma_A']

    coefs = np.array([
        -2*sigma*(1/(dr**2) + 1/(dtheta**2)*(raio**2)), 
        (sigma/dr)*((1/dr) - (1/2*raio)), 
        (sigma/dr)*((1/dr) + (1/2*raio)),
        (sigma)/((dtheta**2)*(raio**2)), 
        (sigma)/((dtheta**2)*(raio**2)) 
    ])

    pontos = np.array([M[i-1,j], M[i+1,j], M[i,j-1], M[i,j+1]]).reshape(4,1)

    return (coefs[1:] @ pontos)/coefs[0]


#9: interior de B
def inter_B(M, i, j, dr, dtheta):
    raio = 0.03 + i*dr
    angulo = j*dtheta #em radianos

    sigma = props_elet['sigma_B']

    coefs = np.array([
        -2*sigma*(1/(dr**2) + 1/(dtheta**2)*(raio**2)), 
        (sigma/dr)*((1/dr) - (1/2*raio)), 
        (sigma/dr)*((1/dr) + (1/2*raio)),
        (sigma)/((dtheta**2)*(raio**2)), 
        (sigma)/((dtheta**2)*(raio**2)) 
    ])

    pontos = np.array([M[i-1,j], M[i+1,j], M[i,j-1], M[i,j+1]]).reshape(4,1)

    return (coefs[1:] @ pontos)/coefs[0]


if __name__ == '__main__':
    from cria_malha import *

    dr = 0.0005
    dtheta = np.deg2rad(0.5)
    lamb = 1.5
    erro_des = 1e-2

    M = cria_malha(dr, dtheta)
    