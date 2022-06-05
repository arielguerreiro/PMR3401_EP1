import numpy as np
from liebmann import *
from funcoes_potencial import *

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
            return 1 #borda esquerda do material B (antes 2)
        elif(raio == 0.08):
            return 1 #borda direita do material B (antes 3)
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


def calcula_tensao(M, i, j, dr, dtheta,q_dots):
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

    if q_dots is None: 
        qdot = 0 
    else:
        qdot = q_dots[i,j]
    
    condicao = define_condicao(i, j, dr, dtheta)

    if(condicao == 0):
        temp = sup_A(M, i, j, dr, dtheta, qdot)
    elif(condicao == 1):
        temp = inf_B(M, i, j, dr, dtheta, qdot)
    elif(condicao == 2):
        temp = esq_B(M, i, j, dr, dtheta, qdot)
    elif(condicao == 3):
        temp = dir_B(M, i, j, dr, dtheta, qdot)
    elif(condicao == 4):
        temp = esq_A(M, i, j, dr, dtheta, qdot)
    elif(condicao == 5):
        temp = dir_A(M, i, j, dr, dtheta, qdot)
    elif(condicao == 6):
        temp = inf_A(M, i, j, dr, dtheta, qdot)
    elif(condicao == 7):
        temp = sup_B(M, i, j, dr, dtheta, qdot)
    elif(condicao == 8):
        temp = inter_A(M, i, j, dr, dtheta, qdot)
    elif(condicao == 9):
        temp = inter_B(M, i, j, dr, dtheta, qdot)
    
    return temp

def resolve_potencial(dr=0.001, dtheta=np.deg2rad(2), lamb=1.75, erro_des=1e-4,q_dots=None):

    #cria matriz inicialmente zerada
    M = cria_malha(dr, dtheta)

    print(f"Matriz: {M.shape}")

    M_ans = liebmann(M,
                    func=calcula_tensao, 
                    lamb=lamb, 
                    erro_des=erro_des, 
                    dr=dr, 
                    dtheta=dtheta,
                    q_dots=q_dots,
                    max_steps=1.e4
                    )

    #cria_plot(M_ans, dr, dtheta)
    return M_ans

def calcula_Qr(V, i, j, dr, dtheta, termico=False):
    condicao = define_condicao(i, j, dr, dtheta)

    if termico:
        multA = props_elet['k_A']
        multB = props_elet['k_B']
    else: 
        multA = props_elet['sigma_A']
        multB = props_elet['sigma_B']
    
    if(condicao == 4): #borda esquerda de A
        #progressiva
        qr = multA * (-V[i+2, j] + 4*V[i+1, j] - 3*V[i, j])/(2*dr)    
    elif(condicao == 5): #borda direita de A
        #regressiva
        qr = multA * (V[i-2, j] - 4*V[i-1, j] + 3*V[i, j])/(2*dr)
    elif(condicao in [0, 8, 6]): #interior de A
        qr = multA * (V[i+1, j] - V[i-1,j])/(2*dr)
    else: #interior de B 
        qr = multB * (V[i+1, j] - V[i-1,j])/(2*dr)

    return qr

def calcula_Qtheta(V, i, j, dr, dtheta, termico=False):
    condicao = define_condicao(i, j, dr, dtheta)

    if termico:
        multA = props_elet['k_A']
        multB = props_elet['k_B']
    else: 
        multA = props_elet['sigma_A']
        multB = props_elet['sigma_B']
        

    if(condicao == 0): #regressiva
        qtheta = multA * (V[i, j-2] - 4*V[i, j-1] + 3*V[i, j])/(2*dtheta)
    elif(condicao in [6, 1]): #central simetrica A
        qtheta = 0
    elif(condicao in [4, 5, 8]): #central A
        try:
            qtheta = multA* (V[i, j+1] - V[i,j-1])/(2*dtheta)
        except:
            qtheta = 0 #despreza pontos extremos de A
    else: #central B
        qtheta = multB* (V[i, j+1] - V[i,j-1])/(2*dtheta)

    return qtheta

def calcula_J(V_ans, dr, dtheta, termico=False):
    J = np.zeros((V_ans.shape[0], V_ans.shape[1], 2)) #guarda os vetores
    for i in range(J.shape[0]):
        for j in range(J.shape[1]):
            J[i, j, 0] = -calcula_Qr(V_ans, i, j, dr, dtheta, termico)
            J[i, j, 1] = -calcula_Qtheta(V_ans, i, j, dr, dtheta, termico)

    return J

def calcula_qponto(J_ans, dr, dtheta):
    qdot = np.zeros((J_ans.shape[0], J_ans.shape[1]))

    for i in range(qdot.shape[0]):
        for j in range(qdot.shape[1]):
            condicao = define_condicao(i, j, dr, dtheta)
            
            if(condicao in [0, 4, 5, 6, 8]):
                sigma = props_elet['sigma_A']
            else:
                sigma = props_elet['sigma_B']
            
            qdot[i, j] = -(np.linalg.norm(J_ans[i, j, :]))**2/sigma

    return qdot

def calcula_corrente(J_ans, dr, dtheta):
    #aproxima integral para soma
    soma = 0

    for i in range(J_ans.shape[0]): #caminha em r
        for j in range(J_ans.shape[1]):
            #somente a componente de r do vetor seria seria relevante
            soma += J_ans[i, j, 0]*dr  

    return soma

if __name__ == "__main__":
    resolve_potencial()

