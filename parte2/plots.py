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

    raios = [0.03 + i*dr for i in range(J.shape[0])]
    angulos = [j*dtheta for j in range(J.shape[1])]

    ang_mesh, raio_mesh = np.meshgrid(angulos, raios)

    x_mesh = raio_mesh*np.cos(ang_mesh)
    y_mesh = raio_mesh*np.sin(ang_mesh)

    x_vec = np.zeros((J.shape[0], J.shape[1]))
    y_vec = np.zeros((J.shape[0], J.shape[1]))

    for i in range(J.shape[0]):
        for j in range(J.shape[1]):
            raio = 0.03 + i*dr
            angulo = j*dtheta
            #projeta
            qr = J[i, j, 0]
            qtheta = J[i, j, 1]
            x_vec[i, j] = (qr - qtheta)*np.cos(angulo)
            y_vec[i, j] = (qr + qtheta)*np.sin(angulo)

    fig1 = ff.create_quiver(x_mesh, y_mesh, x_vec, y_vec)
    fig2 = ff.create_quiver(x_mesh, -y_mesh, x_vec, -y_vec)

    fig1.add_traces(data = fig2.data)
    fig1.update_traces(marker=dict(color='blue'))

    fig1.show()


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