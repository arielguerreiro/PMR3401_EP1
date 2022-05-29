import numpy as np

#funcoes para a definicao dos coeficientes para cada caso do problema

def compute_inside(sigma, deltaPhi, deltaR, R):
    '''
    Função que gera os coeficientes dos termos V para o caso do interior do material em A e B
    Os pesos serao referentes aos pontos relativos da seguinte maneira:

        [Vij ; Vi-1,j ; Vi+1,j ; Vi,j-1 ; Vi,j+1]

    '''
    coeficients = np.array([
        -2*sigma*(1/(deltaR**2) + 1/(deltaPhi**2)*(R**2)), 
        (sigma/deltaR)*((1/deltaR) - (1/2*R)), 
        (sigma/deltaR)*((1/deltaR) + (1/2*R)),
        (sigma)/((deltaPhi**2)*(R**2)), 
        (sigma)/((deltaPhi**2)*(R**2)) 
    ]) 

    return coeficients


def compute_uper_border(sigma, deltaPhi, deltaR, R):
    '''
    Função que gera os coeficientes dos termos V para o caso da borda do material em A
    Os pesos serao referentes aos pontos relativos da seguinte maneira:

        [Vij ; Vi-1,j ; Vi+1,j ; Vi,j-1]

    '''
    coeficients = np.array([
        -2*sigma*(1/(deltaR**2) + 1/(deltaPhi**2)*(R**2)),
        (sigma/(deltaR**2)), 
        (sigma/(deltaR**2)), 
        (2/(deltaPhi**2)*(sigma/(R**2)))
    ]) 

    return coeficients


def compute_borderAB_byR(sigmaA, sigmaB, deltaPhi, deltaR, R):
    '''
    Função que gera os coeficientes dos termos V na fronteira entre os materiais A e B
    aproximando pela variação no raio (delraR).
    Os pesos serao referentes aos pontos relativos da seguinte maneira:

        [Vij ; Vi-1,j ; Vi+1,j ; Vi,j-1 ; Vi,j+1]

    '''
    coeficients = np.array([
        (2*(sigmaB-sigmaA)/(deltaR**2)) - 2*(sigmaA+sigmaB)/((R**2)*(deltaPhi**2)),
        (2*(sigmaA)/(deltaR**2)) - (sigmaA+sigmaB)/(2*(deltaR)*(R)),
        (-2*(sigmaB)/(deltaR**2)) + (sigmaA+sigmaB)/(2*(deltaR)*(R)),
        (sigmaA+sigmaB)/((deltaPhi**2)*(R**2)),
        (sigmaA+sigmaB)/((deltaPhi**2)*(R**2))
    ]) 

    return coeficients

def compute_borderAB_byPHI(sigmaA, sigmaB, deltaPhi, deltaR, R):
    '''
    Função que gera os coeficientes dos termos V na fronteira entre os materiais A e B
    aproximando pela variação no ângulo (delraPhi).
    Os pesos serao referentes aos pontos relativos da seguinte maneira:

        [Vij ; Vi-1,j ; Vi+1,j ; Vi,j-1 ; Vi,j+1]

    '''
    coeficients = np.array([
        (-2*(sigmaB+sigmaA)/(deltaR**2)) - 2*(sigmaA+sigmaB)/((R**2)*(deltaPhi**2)),
        ((sigmaA+sigmaB)/(deltaR**2)) - (sigmaA+sigmaB)/(2*(deltaR)*(R)),
        ((sigmaA+sigmaB)/(deltaR**2)) + (sigmaA+sigmaB)/(2*(deltaR)*(R)),
        (2*sigmaB)/((deltaPhi**2)*(R**2)),
        (2*sigmaA)/((deltaPhi**2)*(R**2))
    ]) 

    return coeficients

if __name__ == "__main__":
    print(compute_borderAB_byPHI(1,1,1,1,1))