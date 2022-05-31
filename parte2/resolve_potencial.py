import numpy as np 
from coeficients import *
from liebmann import *
from cria_malha import *
from plots import *


def function(M, i, j):
    '''
    função que retorna o resultado para V{i,j} com base em seus termos adjacentes.
    '''
    coef = compute_inside(sigma=3, deltaPhi=1, deltaR=2, R=1)
    adjacentes = np.array([M[i-1,j], M[i+1,j], M[i,j-1], M[i,j+1]]).reshape(4,1)

    print(f"COEF: {coef}")
    print(f"ADJ: {adjacentes}")

    return coef @ adjacentes

def verifica_condicao(i, j, dr, dtheta):
    #verifica em qual condicao esta o ponto i, j da malha
    raio = i*dr + min(props_geo['R_A'])
    theta = np.rad2deg(j*dtheta + min(props_geo['Theta_A']))

    print(f"Raio = {raio}, Theta = {theta}")

    if(theta >= 40): 
        print("Borda superior do material A")

        return 0 
    
    elif(theta == 0):
        if(0.05 < raio < 0.08):
            print("borda inferior do material B")

            return 1 #falta

        elif(raio == 0.05):
            print("borda esquerda do material B")

            return 2 
        elif(raio == 0.08):
            print("borda direita do material B")

            return 3 #falta
        elif(raio == 0.03):
            print("borda esquerda do material A")

            return 4 #ajuste 
        elif(raio == 0.11):
            print("borda direita do material A")

            return 5 #ajuste 
        else:
            print("borda inferior do material A")

            return 6 #falta

    
    elif(theta == 18):
        if(0.05 < raio < 0.08):
            print("borda superior do material B")

            return 7 #AB byPhi
            
        if(raio == 0.11):
            print("borda direita do material A")

            return 5

        elif(raio == 0.03):
            print("borda esquerda do material A")

            return 4
        else:
            print("interior do material A")

            return 8 #interior A

    elif(theta > 18):

        if(raio == 0.11):
            print("borda direita do material A")

            return 5

        elif(raio == 0.03):
            print("borda esquerda do material A")

            return 4

        else:
            print("interior do material A")

            return 8 

    else:
        if(0.05 < raio < 0.08):
            print("interior do material B")

            return 9 #interior B 
        elif(raio == 0.05):
            print("borda esquerda do material B")

            return 2
        elif(raio == 0.08):
            print("borda direita do material B")

            return 3
        elif(raio == 0.03):
            print("borda esquerda do material A")

            return 4 
        elif(raio == 0.11):
            print("borda direita do material A")

            return 5
        else:
            print("interior do material A")

            return 8

if __name__ == "__main__":
    dr = 0.001
    dtheta = np.deg2rad(1)
    M = cria_malha(dr, dtheta)

    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            M[i,j]=verifica_condicao(i,j, dr, dtheta)

    import seaborn as sns
    import matplotlib.pyplot as plt
    sns.color_palette("tab10")
    cria_plot(M, dr, dtheta)

