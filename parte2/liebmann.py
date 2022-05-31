import numpy as np

def calcula_erro(M_novo, M_atual):
    erro = np.zeros(M_atual.shape)

    for i in range(M_atual.shape[0]):
        for j in range(M_atual.shape[1]):
            if(M_novo[i, j] == 0 and M_atual[i, j] == 0):
                erro[i, j] = 0
            elif(M_novo[i, j] == 0 and M_atual[i, j] == 0):
                raise Exception("Divisão inválida: verificar")
            else:
                erro[i, j] = np.abs((M_novo[i, j] - M_atual[i, j])/M_novo[i, j])
    return erro

def calcula_iteracao(M_atual, func, lamb, dr, dtheta):
    M_step = np.copy(M_atual)

    for i in range(M_atual.shape[0]):
        for j in range(M_atual.shape[1]):
            M_step[i, j] = func(M_step, i, j, dr, dtheta)
            M_step[i, j] = lamb*M_step[i, j] + (1 - lamb)*M_atual[i, j]

    return M_step

def liebmann(M, func, lamb, erro_des, dr, dtheta, max_steps=1e3):
    #implementacao do metodo de liebmann
    
    M_atual = np.copy(M)
    erro = [10*erro_des]
    i = 1

    while(np.max(erro) > erro_des):
        M_novo = calcula_iteracao(M_atual, func, lamb, dr, dtheta)
        erro = calcula_erro(M_novo, M_atual)
        M_atual = np.copy(M_novo)
        i += 1

        print(f"Iteração {i}: erro {np.max(erro):.4f}")

        if(i > max_steps):
            break

    print(f"Erro {np.max(erro):.4f} atingido com {i} steps")
    return M_atual

if __name__ == '__main__':

    from plots import cria_plot

    def func(M, i, j, dr, dtheta):
        return i + j

    M = np.zeros((5, 5))

    dr = 1
    dtheta = 0.1

    erro_des = 1e-3
    lamb = 1.5

    M_ans = liebmann(M, func, lamb, erro_des, dr, dtheta)

    print(M_ans)

    cria_plot(M_ans, dr, dtheta)
    

