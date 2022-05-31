import numpy as np 
from coeficients import *
from liebmann import *
from cria_malha import *
from plots import *
import seaborn as sns
import matplotlib.pyplot as plt

def define_condicao(i, j, dr, dtheta):
    #verifica em qual condicao esta o ponto i, j da malha
    raio = i*dr + min(props_geo['R_A'])
    theta = np.rad2deg(j*dtheta + min(props_geo['Theta_A']))

    if(theta >= 40): 
        return 0 # borda superior material A
    
    elif(theta == 0):
        if(0.05 < raio < 0.08):
            return 1 #borda inferior do material B - duplicar 

        elif(raio == 0.05):
            return 2 #borda esquerda do material B

        elif(raio == 0.08):
            return 3 #borda direita do material B

        elif(raio == 0.03):
            return 4 #borda esquerda do material A - ajuste de matriz

        elif(raio == 0.11):
            return 5 #borda direita do material A - ajuste de matriz 

        else:
            return 6 #borda inferior do material A - duplicar

    
    elif(theta == 18):
        if(0.05 < raio < 0.08):
            return 7 #borda superior do material B
            
        if(raio == 0.11):
            return 5 #borda direita do material A

        elif(raio == 0.03):
            return 4 #borda esquerda do material A
        else:
            return 8 #interior do material A 

    elif(theta > 18):

        if(raio == 0.11):
            return 5 #borda direita do material A

        elif(raio == 0.03):
            return 4 #borda esquerda do material A

        else:
            return 8 #interior do material A

    else:
        if(0.05 < raio < 0.08):
            return 9 #interior B 

        elif(raio == 0.05):
            return 2 

        elif(raio == 0.08):
            return 3 

        elif(raio == 0.03):
            return 4 

        elif(raio == 0.11):
            return 5

        else:
            return 8

def function(M, i, j, sigmaA, sigmaB, deltaPhi, deltaR, R, dr, dtheta):
    '''
    função que retorna o resultado para V{i,j} com base em seus termos adjacentes.
    '''
    condicao = define_condicao(i, j, dr, dtheta)

    if (condicao==0): 
        coef = compute_uper_border(sigmaA, deltaPhi, deltaR, R)
    elif (condicao==1):
        coef = compute_inside(sigmaB, deltaPhi, deltaR, R) #BORDA INFERIOR-DUPLICAR
    elif (condicao==2):
        coef = compute_borderAB_byR_left(sigmaA, sigmaB, deltaPhi, deltaR, R)
    elif (condicao==3):
        coef = compute_borderAB_byR_right(sigmaA, sigmaB, deltaPhi, deltaR, R)
    elif (condicao==4):
        coef = np.zeros(3) # lidar com essa borda
    elif (condicao==5):
        coef = np.zeros(3) # lidar com essa borda 
    elif (condicao==6):
        coef = compute_inside(sigmaA, deltaPhi, deltaR, R) #BORDA INFERIOR-DUPLICAR
    elif (condicao==7):
        coef = compute_borderAB_byPHI(sigmaA, sigmaB, deltaPhi, deltaR, R)
    elif (condicao==8):
        coef = compute_inside(sigmaA, deltaPhi, deltaR, R)
    elif (condicao==9):
        coef = compute_inside(sigmaB, deltaPhi, deltaR, R)
    else:
        raise Exception("Caso invalido ou não documentado")

    #define os números adjacentes:
    if (condicao==1 or condicao==6):
        #em casos de borda inferior, não há j-1, mas sim seu simétrico j+1 
        adjacentes = np.array([M[i-1,j], M[i+1,j], M[i,j+1], M[i,j+1]]).reshape(4,1)
    else:
        adjacentes = np.array([M[i-1,j], M[i+1,j], M[i,j-1], M[i,j+1]]).reshape(4,1)

    print(f"COEF: {coef}")
    print(f"ADJ: {adjacentes}")

    return coef @ adjacentes


def main():
    #definicao de propriedades 
    dr = 0.0005
    dtheta = np.deg2rad(0.5)
    lamb = 1.5
    erro_des = 1e-2

    #cria matriz inicialmente zerada
    M = cria_malha(dr, dtheta)

    print(f"Matriz: {M.shape}")

    M_ans = liebmann(M, func=function, lamb=lamb, erro_des=erro_des)

    cria_plot(M_ans, dr, dtheta)


if __name__ == "__main__":
    dr = 0.0005
    dtheta = np.deg2rad(0.5)
    M = cria_malha(dr, dtheta)
    print(M.shape)

    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            M[i,j]=define_condicao(i,j, dr, dtheta)

    import seaborn as sns
    import matplotlib.pyplot as plt
    cria_plot(M, dr, dtheta)

