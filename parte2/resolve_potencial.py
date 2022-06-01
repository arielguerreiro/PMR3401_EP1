import numpy as np
from liebmann import *
from cria_malha import *
from plots import *
from funcoes_potencial import *

def define_condicao(i, j, dr, dtheta):
    #verifica em qual condicao esta o ponto i, j da malha
    raio = i*dr + min(props_geo['R_A'])
    theta = np.rad2deg(j*dtheta + min(props_geo['Theta_A']))
    #angulos sao usados em graus nessa funcao para facilitar a analise

    if(theta >= 40):
        if(raio == 0.03):
            return 4
        if(raio == 0.11):
            return 5
        else:
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


def calcula_tensao(M, i, j, dr, dtheta):
    '''
    Funcao que calcula a tensao para um ponto i, j

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
    '''

    condicao = define_condicao(i, j, dr, dtheta)

    if(condicao == 0):
        temp = sup_A(M, i, j, dr, dtheta)
    elif(condicao == 1):
        temp = inf_B(M, i, j, dr, dtheta)
    elif(condicao == 2):
        temp = esq_B(M, i, j, dr, dtheta)
    elif(condicao == 3):
        temp = dir_B(M, i, j, dr, dtheta)
    elif(condicao == 4):
        temp = esq_A(M, i, j, dr, dtheta)
    elif(condicao == 5):
        temp = dir_A(M, i, j, dr, dtheta)
    elif(condicao == 6):
        temp = inf_A(M, i, j, dr, dtheta)
    elif(condicao == 7):
        temp = sup_B(M, i, j, dr, dtheta)
    elif(condicao == 8):
        temp = inter_A(M, i, j, dr, dtheta)
    elif(condicao == 9):
        temp = inter_B(M, i, j, dr, dtheta)
    
    return np.float(temp)

def main():
    #definicao de propriedades 
    #dr = 0.0005
    #dtheta = np.deg2rad(0.5)
    
    dr = 0.001
    dtheta = np.deg2rad(2)

    lamb = 1.5
    erro_des = 1e-4

    #cria matriz inicialmente zerada
    M = cria_malha(dr, dtheta)

    print(f"Matriz: {M.shape}")

    M_ans = liebmann(M,
                    func=calcula_tensao, 
                    lamb=lamb, 
                    erro_des=erro_des, 
                    dr=dr, 
                    dtheta=dtheta,
                    max_steps=1.e4)

    #cria_plot(M_ans, dr, dtheta)
    heatmap_2d(M_ans, dr, dtheta)
    surf_3d(M_ans, dr, dtheta)


if __name__ == "__main__":
    main()

