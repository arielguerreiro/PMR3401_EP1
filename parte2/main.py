from resolve_potencial import *
from plots import *
import numpy as np
import time

print("PMR3401 - EP1 2022")
print("Ariel Guerreiro - 11257838")
print("Felipe Azank - 11258137\n\n")

#calcula a tensao de cada ponto da malha
dr = 0.001
dtheta = np.deg2rad(1)

print(f"Discretização adotada:\ndelta_r = {dr}\ndelta_theta = {dtheta:.5f} rad ({np.rad2deg(dtheta)}°)")

#calculo das tensoes
start_time = time.time()

V_ans = resolve_potencial(
    dr=dr,
    dtheta=dtheta,
    lamb=1.75,
    erro_des=1e-4
    )

#print(f"Tempo de execução: {(time.time() - start_time):.2f} s")

J_ans = calcula_J(V_ans, dr, dtheta)

q_ans = calcula_qponto(J_ans, dr, dtheta)

#calcula metade da corrente - lembrar de dobrar aqui
I_ans = calcula_corrente(J_ans, dr, dtheta)

deltaV = 100

R = deltaV/I_ans

print(f"Corrente: {I_ans} A")
print(f"Resistência equivalente: {R} Ohms")

#plots

#heatmap da tensao eletrica
heatmap_2d(
    V_ans, dr, dtheta,
    title='Tensão elétrica',
    xlabel='Coordenada X (m)',
    ylabel='Coordenada Y (m)',
    legend='Tensão (V)'
)

#surface plot da tensao eletrica
surf_3d(
    V_ans, dr, dtheta,
    title='Tensão elétrica',
    xlabel='Coordenada X (m)',
    ylabel='Coordenada Y (m)',
    zlabel='Tensão (V)'
)

#quiver plot da densidade de corrente
quiver(
    J_ans, dr, dtheta,
    title='Vetor densidade de corrente',
    xlabel='Coordenada X (m)',
    ylabel='Coordenada Y (m)',
)

#surface plot da fonte de calor equivalente
surf_3d(
    q_ans, dr, dtheta,
    title='Fonte de calor equivalente',
    xlabel='Coordenada X (m)',
    ylabel='Coordenada Y (m)',
    zlabel='Fonte de calor (W/m^3)',
)

#calcula temperaturas com as mesmas funcoes do potencial
T_ans = resolve_potencial(
    dr=dr,
    dtheta=dtheta,
    lamb=1.75,
    erro_des=1e-4,
    q_dots = q_ans)

surf_3d(
    T_ans, dr, dtheta,
    title='Temperatura do Sexo',
    xlabel='Coordenada X (m)',
    ylabel='Coordenada Y (m)',
    zlabel='Temperatura (Celsius)'
)