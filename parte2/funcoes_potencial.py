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
    pass

#5: borda direita de A
def dir_A(M, i, j, dr, dtheta):
    pass

#6: borda inferior de A (regiao de simetria)
def inf_B(M, i, j, dr, dtheta):
    pass

#7: borda superior de B
def sup_B(M, i, j, dr, dtheta):
    pass

#8: interior de A
def inter_A(M, i, j, dr, dtheta):
    pass

#9: interior de B
def inter_B(M, i, j, dr, dtheta):
    pass