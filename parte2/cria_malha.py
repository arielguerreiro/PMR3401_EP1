import numpy as np

#variaveis globais
#definicao de somente metade do forno

props_geo = {
    "R_A" : [0.03, 0.08 + 0.03],
    "R_B" : [0.03 + 0.02, 0.03 + 0.05],
    "Theta_A" : [0, np.deg2rad(40)],
    "Theta_B" : [0, np.deg2rad(18)],
}

def cria_malha(dr, dtheta):
    
    #cria matriz inicial
    n_r = (max(props_geo['R_A']) - min(props_geo['R_A']))/dr
    n_theta = (max(props_geo["Theta_A"]) - min(props_geo["Theta_A"]))/dtheta 
    
    ##print(n_r, n_theta)

    M = np.zeros((int(n_r+1), int(n_theta+1)))

    return M

def verifica_condicao(M, i, j, dr, dtheta):
    #verifica em qual condicao esta o ponto i, j da malha
    raio = i*dr + min(props_geo['R_A'])
    theta = np.rad2deg(j*dtheta + min(props_geo['Theta_A']))

    print(f"Raio = {raio}, Theta = {theta}")

    if(theta == 40):
        print("Borda superior do material A")
    
    elif(theta == 0):
        if(0.05 < raio < 0.08):
            print("borda inferior do material B")
        elif(raio == 0.05):
            print("borda esquerda do material B")
        elif(raio == 0.08):
            print("borda direita do material B")
        elif(raio == 0.03):
            print("borda esquerda do material A")
        elif(raio == 0.11):
            print("borda direita do material A")
        else:
            print("borda inferior do material A")
    
    elif(theta == 18):
        if(0.05 < raio < 0.08):
            print("borda superior do material B")
        else:
            print("interior do material A")

    else:
        if(0.05 < raio < 0.08):
            print("interior do material B")
        elif(raio == 0.05):
            print("borda esquerda do material B")
        elif(raio == 0.08):
            print("borda direita do material B")
        elif(raio == 0.03):
            print("borda esquerda do material A")
        elif(raio == 0.11):
            print("borda direita do material A")
        else:
            print("interior do material A")
    

if __name__ == '__main__':
    dr = 0.01
    dtheta = np.deg2rad(1)

    Mat = cria_malha(dr, dtheta)
    print(Mat)

    i = 0
    j = 0

    verifica_condicao(Mat, i, j, dr, dtheta)

    i = 2
    j = 0

    verifica_condicao(Mat, i, j, dr, dtheta)

    i = 2
    j = 1

    verifica_condicao(Mat, i, j, dr, dtheta)

    i = 3
    j = 3

    verifica_condicao(Mat, i, j, dr, dtheta)