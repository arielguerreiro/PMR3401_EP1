import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns
import plotly.express as ex

from cria_malha import *

props_geo = {
    "R_A" : [0.03, 0.08 + 0.03],
    "R_B" : [0.03 + 0.02, 0.03 + 0.05],
    "Theta_A" : [0, np.deg2rad(40)],
    "Theta_B" : [0, np.deg2rad(18)],
}


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
    
    for item in Valores:
        item = str(Valores)
    
    fig = ex.scatter(x=X, y=Y, color=Valores)
    fig.show()