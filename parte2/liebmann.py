import numpy as np

def calcula_erro(M_novo, M_atual):
    '''
    Função que calcula o erro relativo entre a iteração atual e a iteração
    anterior, devolvendo uma matriz com o valor do erro em cada entrada
    da matriz M

    **Entradas**:
    M_novo: matriz da nova iteração
    M_atual: matriz da iteração anterior

    **Saídas**:
    erro: matriz com o erro relativo de cada um dos valores da variável
    
    '''
    erro = np.zeros(M_atual.shape)

    for i in range(M_atual.shape[0]):
        for j in range(M_atual.shape[1]):
            if(M_novo[i, j] == 0 and M_atual[i, j] == 0):
                #evita a divisão por zero
                erro[i, j] = 0
            elif(M_novo[i, j] == 0 and M_atual[i, j] != 0):
                 #não deve ocorrer, caso ocorra o código para imediatamente
                import pdb; pdb.set_trace()
            else:
                erro[i, j] = np.abs((M_novo[i, j] - M_atual[i, j])/M_novo[i, j])
    return erro

def calcula_iteracao(M_atual, func, lamb, dr, dtheta, q_dots):
    '''
    Função que calcula uma iteração do método de liebmann, já aplicando a 
    sobrerelaxação a cada item calculado

    **Entradas**:
    M_atual: numpy array com os valores iniciais da iteração, permanece inalterada
    func: função que calcula novo valor da variável
    lamb: fator de sobrerelaxação
    dr: variação "delta r"
    dtheta: variação "delta theta"
    q_dots: valor de q_ponto, usado no caso térmico

    **Saídas**
    M_step: numpy array com os novos valores após o cálculo da iteração
    
    '''
    M_step = np.copy(M_atual)

    for i in range(M_atual.shape[0]):
        for j in range(M_atual.shape[1]):
            M_step[i, j] = func(M_step, i, j, dr, dtheta, q_dots)
            M_step[i, j] = lamb*M_step[i, j] + (1 - lamb)*M_atual[i, j]

    return M_step

def liebmann(M, func, lamb, erro_des, dr, dtheta, max_steps=1e5,q_dots=None):
    '''
    Implementação do método de Liebmann com sobrerelexação

    **Entradas**:
    M: numpy array que armazenará os valores da varíavel calculada
    func: função que calcula novo valor da variável
    lamb: fator de sobrerelaxação
    erro_des: erro relativo desejado
    dr: variação "delta r"
    dtheta: variação "delta theta"
    max_steps: número máximo de iterações, interrompe execução caso
    a convergência não tenha ocorrido
    q_dots: valor de q_ponto, usado no caso térmico

    **Saídas**
    M_atual: Matriz com os valores da variável calculada após a convergência
    '''
    
    M_atual = np.copy(M)
    erro = [10*erro_des]
    i = 1

    while(np.max(erro) > erro_des):
        M_novo = calcula_iteracao(M_atual, func, lamb, dr, dtheta,q_dots)
        erro = calcula_erro(M_novo, M_atual)
        M_atual = np.copy(M_novo)
        i += 1

        print(f"Iteração {i}: erro {np.max(erro):.5f}", end='\r')

        if(i > max_steps):
            break

    print(f"Erro {np.max(erro):.4f} atingido com {i} steps")
    return M_atual