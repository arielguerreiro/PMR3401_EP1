import numpy as np

#funcoes para a definicao dos coeficientes para cada caso do problema

def compute_inside(sigma, dtheta, dr, R):
    '''
    Função que gera os coeficientes dos termos V para o caso do interior do 
    material em A e B.
    
    Os pesos serao referentes aos pontos relativos a V[i,j] da seguinte maneira:

        [Vi-1,j ; Vi+1,j ; Vi,j-1 ; Vi,j+1]

    '''
    coeficients = np.array([
        -2*sigma*(1/(dr**2) + 1/(dtheta**2)*(R**2)), 
        (sigma/dr)*((1/dr) - (1/2*R)), 
        (sigma/dr)*((1/dr) + (1/2*R)),
        (sigma)/((dtheta**2)*(R**2)), 
        (sigma)/((dtheta**2)*(R**2)) 
    ]) 

    return -coeficients[1:]/coeficients[0]


def compute_uper_border(sigma, dtheta, dr, R):
    '''
    Função que gera os coeficientes dos termos V para o caso da borda do material em A
    Os pesos serao referentes aos pontos relativos a V[i,j] da seguinte maneira:

        [Vi-1,j ; Vi+1,j ; Vi,j-1]

    '''
    coeficients = np.array([
        -2*sigma*(1/(dr**2) + 1/(dtheta**2)*(R**2)),
        (sigma/(dr**2)), 
        (sigma/(dr**2)), 
        (2/(dtheta**2)*(sigma/(R**2)))
    ]) 

    return -coeficients[1:]/coeficients[0]


def compute_borderAB_byR_left(sigmaA, sigmaB, dtheta, dr, R):
    '''
    Função que gera os coeficientes dos termos V na fronteira entre os materiais A e B
    aproximando pela variação no raio (delraR) do lado esquerdo.
    Os pesos serao referentes aos pontos relativos a V[i,j] da seguinte maneira:

        [Vi-1,j ; Vi+1,j ; Vi,j-1 ; Vi,j+1]

    '''
    coeficients = np.array([
        (2*(sigmaB-sigmaA)/(dr**2)) - 2*(sigmaA+sigmaB)/((R**2)*(dtheta**2)),
        (2*(sigmaA)/(dr**2)) - (sigmaA+sigmaB)/(2*(dr)*(R)),
        (-2*(sigmaB)/(dr**2)) + (sigmaA+sigmaB)/(2*(dr)*(R)),
        (sigmaA+sigmaB)/((dtheta**2)*(R**2)),
        (sigmaA+sigmaB)/((dtheta**2)*(R**2))
    ]) 

    return -coeficients[1:]/coeficients[0]

def compute_borderAB_byR_right(sigmaA, sigmaB, dtheta, dr, R):
    '''
    Função que gera os coeficientes dos termos V na fronteira entre os materiais A e B
    aproximando pela variação no raio (delraR) do lado direito.
    Os pesos serao referentes aos pontos relativos a V[i,j] da seguinte maneira:

        [Vi-1,j ; Vi+1,j ; Vi,j-1 ; Vi,j+1]

    '''
    coeficients = np.array([
        (2*(sigmaA-sigmaB)/(dr**2)) - 2*(sigmaA+sigmaB)/((R**2)*(dtheta**2)),
        (2*(sigmaB)/(dr**2)) - (sigmaA+sigmaB)/(2*(dr)*(R)),
        (-2*(sigmaA)/(dr**2)) + (sigmaA+sigmaB)/(2*(dr)*(R)),
        (sigmaA+sigmaB)/((dtheta**2)*(R**2)),
        (sigmaA+sigmaB)/((dtheta**2)*(R**2))
    ]) 

    return -coeficients[1:]/coeficients[0]

def compute_borderAB_byPHI(sigmaA, sigmaB, dtheta, dr, R):
    '''
    Função que gera os coeficientes dos termos V na fronteira entre os materiais A e B
    aproximando pela variação no angulo (delraPhi) do lado superior.
    Os pesos serao referentes aos pontos relativos a V[i,j] da seguinte maneira:

        [Vi-1,j ; Vi+1,j ; Vi,j-1 ; Vi,j+1]

    '''
    coeficients = np.array([
        (-2*(sigmaB+sigmaA)/(dr**2)) - 2*(sigmaA+sigmaB)/((R**2)*(dtheta**2)),
        ((sigmaA+sigmaB)/(dr**2)) - (sigmaA+sigmaB)/(2*(dr)*(R)),
        ((sigmaA+sigmaB)/(dr**2)) + (sigmaA+sigmaB)/(2*(dr)*(R)),
        (2*sigmaB)/((dtheta**2)*(R**2)),
        (2*sigmaA)/((dtheta**2)*(R**2))
    ]) 

    return -coeficients[1:]/coeficients[0]


if __name__ == "__main__":
    print(compute_borderAB_byR_right(1,1,1,1,1))