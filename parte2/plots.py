import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns
import plotly.express as ex
import plotly.graph_objects as go
import plotly.figure_factory as ff

def heatmap_2d(M, dr, dtheta, tipo='C'):

    X = []
    Y = []
    Valores = []

    for i in range(M.shape[0]): #raio
        for j in range(M.shape[1]): #angulo
            raio = 0.03 + i*dr
            angulo = j*dtheta

            x = raio*np.cos(angulo)
            y = raio*np.sin(angulo)
            
            valor = M[i,j]

            X.append(x)
            Y.append(y)
            Valores.append(valor)
            
            #reflexao no eixo X
            X.append(x)
            Y.append(-y)
            Valores.append(valor)

    X, Y = np.array(X), np.array(Y)
    if tipo == 'D':
        Valores = [str(i) for i in Valores]
    fig = ex.scatter(x=X, y=Y, color=Valores)
    fig.show()

def surf_3d(M, dr, dtheta):

    raios = [0.03 + i*dr for i in range(M.shape[0])]
    angulos = [j*dtheta for j in range(M.shape[1])]

    ang_mesh, raio_mesh = np.meshgrid(angulos, raios)

    x_mesh = raio_mesh*np.cos(ang_mesh)
    y_mesh = raio_mesh*np.sin(ang_mesh)

    fig = go.Figure(data=[go.Surface(z=M, x=x_mesh, y=y_mesh), go.Surface(z=M, x=x_mesh, y=-y_mesh)])
    fig.show()

def quiver(J, dr, dtheta):

    import pdb; pdb.set_trace()

    raios = [0.03 + i*dr for i in range(M.shape[0])]
    angulos = [j*dtheta for j in range(M.shape[1])]

    ang_mesh, raio_mesh = np.meshgrid(angulos, raios)

    x_mesh = raio_mesh*np.cos(ang_mesh)
    y_mesh = raio_mesh*np.sin(ang_mesh)

    origin = J[:, :, 0]
    
    plt.quiver(x_mesh, y_mesh, J[:, :, 0], J[:, :, 1])
    plt.show()


if __name__ == '__main__':
    from resolve_potencial import define_condicao, cria_malha

    dr = 0.0005
    dtheta = np.deg2rad(0.5)
    M = cria_malha(dr, dtheta)
    print(M.shape)

    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            M[i, j] = define_condicao(i,j, dr, dtheta)

    import seaborn as sns
    import matplotlib.pyplot as plt
    heatmap_2d(M, dr, dtheta, 'C')