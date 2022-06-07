from matplotlib.axis import XAxis
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns
import plotly.express as ex
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd

def heatmap_2d(M, dr, dtheta, xlabel, ylabel, title, legend, tipo='C', reflexao=True):
    '''
    Função para gerar um heatmap de 2 dimensões, a partir dos valores armazenados
    na matriz M
    
    **Entradas**:
    M: matriz com os valores das variáveis desejadas
    dr: variação "delta r"
    dtheta: variação "delta theta"
    xlabel, ylabel, title: labels para os eixos e título do gráfico
    legend: legenda da variável desejada
    tipo: "C" para dados contínuos, "D" para dados discretos
    reflexao: como calcula-se somente metade da peça, caso este valor seja 'True'
    será feita a reflexão no eixo x para mostrar a peça inteira
    '''

    X = []
    Y = []
    Valores = []

    for i in range(M.shape[0]): #raio
        for j in range(M.shape[1]): #angulo
            raio = 0.03 + i*dr
            angulo = j*dtheta

            #conversao de coord. polar para cartesiana
            x = raio*np.cos(angulo)
            y = raio*np.sin(angulo)
            
            valor = M[i,j]

            X.append(x)
            Y.append(y)
            Valores.append(valor)
            
            #reflexao no eixo X
            if reflexao:
                X.append(x)
                Y.append(-y)
                Valores.append(valor)

    X, Y = np.array(X), np.array(Y)
    if tipo == 'D':
        Valores = [str(i) for i in Valores]

    df = pd.DataFrame({xlabel: X, ylabel: Y, legend: Valores})
    
    fig = ex.scatter(df, x=X, y=Y, color=legend)

    fig.update_layout(
        title = dict(
            text=title,
            x=0.5,
            xanchor='center',
            yanchor='top',
        ),

        xaxis_title = xlabel, 

        yaxis_title = ylabel,

        legend = dict(
            yanchor='top',
            y=1.02,
        ),

        font=dict(
            family="Courier New",
            size=18,
        ),

    )

    fig.show()

def surf_3d(M, dr, dtheta, xlabel, ylabel, zlabel, title):
    '''
    Função para gerar um gráfico tridimensional da variável calculada,
    de tipo 'surf'
    
    **Entradas**:
    M: matriz com os valores das variáveis desejadas
    dr: variação "delta r"
    dtheta: variação "delta theta"
    xlabel, ylabel, zlabel, title: labels para os eixos e título do gráfico
    '''

    raios = [0.03 + i*dr for i in range(M.shape[0])]
    angulos = [j*dtheta for j in range(M.shape[1])]

    ang_mesh, raio_mesh = np.meshgrid(angulos, raios)

    x_mesh = raio_mesh*np.cos(ang_mesh)
    y_mesh = raio_mesh*np.sin(ang_mesh)

    fig = go.Figure(data=[go.Surface(z=M, x=x_mesh, y=y_mesh), go.Surface(z=M, x=x_mesh, y=-y_mesh)])

    fig.update_layout(
       title = dict(
            text=title,
            x=0.5,
            xanchor='center',
        ),

        scene = dict(
            xaxis_title=xlabel,
            yaxis_title=ylabel,
            zaxis_title=zlabel, 
        ),

        font=dict(
            family="Courier New",
            size=18,
        ), 
    )
    
    fig.show()



def quiver(J, dr, dtheta, xlabel, ylabel, title, plot='half', arrow_scale=1, lib='matplotlib'):
    '''
    Função para gerar um gráfico bidimensional de um campo vetorial. Por se tratar de um gráfico
    mais pesado, recomenda-se utilizar o matplotlib ao inves do plotly, mas ambas as opcções estão
    implementadas
    
    **Entradas**:
    J: matriz tridimensional com os valores dos vetores
    dr: variação "delta r"
    dtheta: variação "delta theta"
    xlabel, ylabel, title: labels para os eixos e título do gráfico
    plot: 'half' (metade - recomendado) ou 'full' (peça inteira)
    arrow_scale: escala da seta, utilizada somente na versão do plotly
    lib: 'matplotlib' (recomendada) ou 'plotly'
    '''


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

    if lib == 'matplotlib':
        plt.quiver(x_mesh, y_mesh, x_vec, y_vec)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()


    elif lib == 'plotly':
    
        fig1 = ff.create_quiver(x_mesh, y_mesh, x_vec, y_vec, arrow_scale=arrow_scale)


        if plot == 'full':
            fig2 = ff.create_quiver(x_mesh, -y_mesh, x_vec, -y_vec, arrow_scale=arrow_scale)

            fig1.add_traces(data = fig2.data)
            fig1.update_traces(marker=dict(color='blue'))

        fig1.update_layout(
        title = dict(
                text=title,
                x=0.5,
                xanchor='center',
            ),

            scene = dict(
                xaxis_title=xlabel,
                yaxis_title=ylabel,
            ),

            font=dict(
                family="Courier New",
                size=18,
            ), 
        )

        fig1.show()


if __name__ == '__main__':
    from resolve_potencial import define_condicao, cria_malha

    dr = 0.001
    dtheta = np.deg2rad(1)
    M = cria_malha(dr, dtheta)
    print(M.shape)

    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            M[i, j] = define_condicao(i,j, dr, dtheta)

    heatmap_2d(M, dr, dtheta, title='Condição dos pontos', xlabel='X (m)', ylabel='Y (m)', legend='Condicão', tipo='D', reflexao=False)
    #surf_3d(M, dr, dtheta, title='Condicao dos pontos', xlabel='X (m)', ylabel='Y (m)', zlabel='Tensao (V)')