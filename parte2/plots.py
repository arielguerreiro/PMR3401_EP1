import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns
import plotly.express as ex

def cria_plot(M, dr, dtheta):

    sns.color_palette("tab10")

    X = []
    Y = []
    Valores = []

    for i in range(M.shape[0]): #raio
        for j in range(M.shape[1]): #angulo
            raio = 0.03 + i*dr
            angulo = j*dtheta

            x = raio*np.cos(angulo)
            y = raio*np.sin(angulo)
            #print(f"\nPara j={j}: ang = {np.rad2deg(angulo):.3f}, x = {x:.4f}, y = {y:.4f}")

            valor = M[i,j]

            X.append(x)
            Y.append(y)
            Valores.append(valor)

    fig = ex.scatter(x=X, y=Y, color=Valores)
    fig.show()

if __name__ == '__main__':
    from cria_malha import cria_malha
    from resolve_potencial import define_condicao

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