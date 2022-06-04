import numpy as np

props_elet = {
    "sigma_A": 5e-6 * 1e5,
    "sigma_B": 1e-5 * 1e5,
    "k_A": 110,
    "k_B": 500
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
def sup_A(M, i, j, dr, dtheta, qdot):
    raio = 0.03 + i*dr
    angulo = j*dtheta #em radianos
    
    coefs = np.array([
        4*(dr**2 + dtheta**2 * raio**2),
        -dr* dtheta**2 * raio + 2 * dtheta**2 * raio**2,
        dr* dtheta**2 * raio + 2 * dtheta**2 * raio**2,
        4 * dr**2,
    ])

    pontos = np.array([M[i-1,j], M[i+1,j], M[i,j-1]]).reshape(3,1)

    return (np.float(coefs[1:] @ pontos)-qdot*2*(dr**2 * dtheta**2 * raio**2))/np.float(coefs[0])

#1: borda inferior de B (regiao de simetria)
def inf_B(M, i, j, dr, dtheta,qdot):
    raio = 0.03 + i*dr
    angulo = j*dtheta #em radianos

    sigma = props_elet['sigma_B']

    coefs = np.array([
        4*(dr**2 + dtheta**2 * raio**2),
        -dr * dtheta**2 * raio + 2 * dtheta**2 * raio**2,
        dr * dtheta**2 * raio + 2 * dtheta**2 * raio**2,
        2*dr**2,
        2*dr**2,
    ])

    pontos = np.array([M[i-1,j], M[i+1,j], M[i,j+1], M[i,j+1]]).reshape(4,1)
   
    return (np.float(coefs[1:] @ pontos)-qdot*4*(dr**2 * dtheta**2 * raio**2))/np.float(coefs[0])

#2: borda esquerda de B
def esq_B(M, i, j, dr, dtheta,qdot):
    raio = 0.03 + i*dr
    angulo = j*dtheta #em radianos

    if qdot==0:
        sigmaA = props_elet['sigma_A']
        sigmaB = props_elet['sigma_B']

        alpha = sigmaA * (-2/dr + 1/raio)
        beta = sigmaB * (2/dr + 1/raio)

    else:
        k_A = props_elet['k_A']
        k_B = props_elet['k_B']

        alpha = k_A * (-2/dr + 1/raio)
        beta = k_B * (2/dr + 1/raio)
        

    coefs = np.array([
        2*(alpha - beta)*(raio**2 * dtheta**2 + dr **2),
        2 * raio**2 * dtheta**2 * alpha,
        -2 * raio**2 * dtheta**2 * beta,
        (alpha - beta)*dr**2,
        (alpha - beta)*dr**2,
    ])

    pontos = np.array([M[i-1,j], M[i+1,j], M[i,j-1], M[i,j+1]]).reshape(4,1)

    return (np.float(coefs[1:] @ pontos)-qdot*4*(dr**2 * dtheta**2 * raio**2))/np.float(coefs[0])

#3: borda direita de B
def dir_B(M, i, j, dr, dtheta,qdot):
    raio = 0.03 + i*dr
    angulo = j*dtheta #em radianos

    if qdot==0:
        sigmaA = props_elet['sigma_A']
        sigmaB = props_elet['sigma_B']

        alpha = sigmaB*(-2/dr + 1/raio)
        beta = sigmaA*(2/dr + 1/raio)

    else:
        k_A = props_elet['k_A']
        k_B = props_elet['k_B']

        alpha = k_A*(-2/dr + 1/raio)
        beta = k_B*(2/dr + 1/raio)


    coefs = np.array([
        2*(alpha - beta)*(raio**2 * dtheta**2 + dr **2),
        2 * raio**2 * dtheta**2 * alpha,
        -2 * raio**2 * dtheta**2 * beta,
        (alpha - beta)*dr**2,
        (alpha - beta)*dr**2,
    ])

    pontos = np.array([M[i-1,j], M[i+1,j], M[i,j-1], M[i,j+1]]).reshape(4,1)

    return (np.float(coefs[1:] @ pontos)-qdot*4*(dr**2 * dtheta**2 * raio**2))/np.float(coefs[0])

#4: borda esquerda de A
def esq_A(M, i, j, dr, dtheta,qdot):
    if qdot==0:
        return 100
    else:
        return 30 + 273


#5: borda direita de A
def dir_A(M, i, j, dr, dtheta,qdot):
    if qdot==0:
        return 0
    else:
        return 25 + 273

#6: borda inferior de A (regiao de simetria)
def inf_A(M, i, j, dr, dtheta,qdot):
    raio = 0.03 + i*dr
    angulo = j*dtheta #em radianos

    coefs = np.array([
        4*(dr**2 + dtheta**2 * raio**2),
        -dr * dtheta**2 * raio + 2 * dtheta**2 * raio**2,
        dr * dtheta**2 * raio + 2 * dtheta**2 * raio**2,
        2*dr**2,
        2*dr**2,
    ])
    pontos = np.array([M[i-1,j], M[i+1,j], M[i,j+1], M[i,j+1]]).reshape(4,1)
 
    return (np.float(coefs[1:] @ pontos)-qdot*2*(dr**2 * dtheta**2 * raio**2))/np.float(coefs[0])

#7: borda superior de B
def sup_B(M, i, j, dr, dtheta,qdot):
    raio = 0.03 + i*dr
    angulo = j*dtheta #em radianos

    if qdot==0:
        A = props_elet['sigma_A']
        B = props_elet['sigma_B']
    else:
        A = props_elet['k_A']
        B = props_elet['k_B']

    coefs = np.array([
        4*(A + B)*(dtheta**2 * raio**2 + dr**2),
        (A + B)*(-dtheta**2 * dr * raio + 2 * dtheta**2 * raio**2),
        (A + B)*(dtheta**2 * dr * raio + 2 * dtheta**2 * raio**2),
        4 * dr**2 * A,
        4 * dr**2 * B, 
    ])

    pontos = np.array([M[i-1,j], M[i+1,j], M[i,j-1], M[i,j+1]]).reshape(4,1)
  
    return (np.float(coefs[1:] @ pontos)-qdot*4*(dr**2 * dtheta**2 * raio**2))/np.float(coefs[0])

#8: interior de A
def inter_A(M, i, j, dr, dtheta,qdot):
    raio = 0.03 + i*dr
    angulo = j*dtheta #em radianos

    coefs = np.array([
        4*(dr**2 + dtheta**2 * raio**2),
        -dr * dtheta**2 * raio + 2 * dtheta**2 * raio**2,
        dr * dtheta**2 * raio + 2 * dtheta**2 * raio**2,
        2*dr**2,
        2*dr**2,
    ])

    pontos = np.array([M[i-1,j], M[i+1,j], M[i,j-1], M[i,j+1]]).reshape(4,1)
 
    return (np.float(coefs[1:] @ pontos)-qdot*2*(dr**2 * dtheta**2 * raio**2))/np.float(coefs[0])


#9: interior de B
def inter_B(M, i, j, dr, dtheta,qdot):
    raio = 0.03 + i*dr
    angulo = j*dtheta #em radianos

    coefs = np.array([
        4*(dr**2 + dtheta**2 * raio**2),
        -dr * dtheta**2 * raio + 2 * dtheta**2 * raio**2,
        dr * dtheta**2 * raio + 2 * dtheta**2 * raio**2,
        2*dr**2,
        2*dr**2,
    ])

    pontos = np.array([M[i-1,j], M[i+1,j], M[i,j-1], M[i,j+1]]).reshape(4,1)

    return (np.float(coefs[1:] @ pontos)-qdot*4*(dr**2 * dtheta**2 * raio**2))/np.float(coefs[0])


if __name__ == '__main__':
    from resolve_potencial import *

    dr = 0.0005
    dtheta = np.deg2rad(0.5)
    lamb = 1.5
    erro_des = 1e-4

    #M = cria_malha(dr, dtheta)