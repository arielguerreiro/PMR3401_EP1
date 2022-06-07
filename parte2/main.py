from resolve_potencial import *
from plots import *
import numpy as np
import time

print("PMR3401 - EP1 2022")
print("Ariel Guerreiro - 11257838")
print("Felipe Azank - 11258137\n\n")

'''
Arquivo principal, responsável por resolver
toda a parte 2 do exercício-programa
'''

#calcula a tensao de cada ponto da malha
dr = 0.001
dtheta = np.deg2rad(1)

print(f"Discretização adotada:\ndelta_r = {dr}\ndelta_theta = {dtheta:.5f} rad ({np.rad2deg(dtheta)}°)")

#calculo das tensoes eletricas
V_ans = resolve_potencial(
    dr=dr,
    dtheta=dtheta,
    lamb=1.75,
    erro_des=1e-4
    )

#calculo do vetor densidade de corrente
J_ans = calcula_J(V_ans, dr, dtheta)

#calculo da energia dissipada por efeito Joule
q_ans = calcula_qponto(J_ans, dr, dtheta)

#calcula corrente eletrica pelo raio maximo.
#Como o problema é resolvido para metade da peça,
#o valor deve ser dobrado
I_ans_rmax = 2*calcula_corrente(J_ans, dtheta, rmax=True)

#ddp
deltaV = 100

#calcula resisência da peça
R_max = deltaV/I_ans_rmax

print(f"Corrente calculada para Rmax = 0.11: {I_ans_rmax} A")
print(f"Resistência equivalente: {R_max} Ohms")
print(f"Potência dissipada MAX: {I_ans_rmax**2 * R_max}")


#calcula corrente eletrica pelo raio minimo.
I_ans = 2*calcula_corrente(J_ans, dtheta, rmax=False)

R_min = deltaV/I_ans

print(f"Corrente calculada para Rmin = 0.03: {I_ans} A")
print(f"Resistência equivalente: {R_min} Ohms")
print(f"Potência dissipada: {I_ans**2 * R_min}")


#calcula temperaturas com as mesmas funcoes do potencial
T_ans = resolve_potencial(
    dr=dr,
    dtheta=dtheta,
    lamb=1.75,
    erro_des=1e-4,
    q_dots = q_ans)

#calculo do fluxo de calor
fluxo_ans = calcula_J(T_ans, dr, dtheta, termico=True)

#calculo da quantidade de calor (unidade W) que flui pela parede de convecção:
qt_calor_ans = 2*calcula_corrente(fluxo_ans, dtheta, rmax=True)

print(f"Quantidade de calor que flui pela parede de convecção: {qt_calor_ans} W")



#plots das condições

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



#surface plot da fonte de calor equivalente
surf_3d(
    q_ans, dr, dtheta,
    title='Fonte de calor equivalente',
    xlabel='Coordenada X (m)',
    ylabel='Coordenada Y (m)',
    zlabel='Fonte de calor (W/m^3)',
)

surf_3d(
    T_ans, dr, dtheta,
    title='Temperatura dos Pontos do Forno',
    xlabel='Coordenada X (m)',
    ylabel='Coordenada Y (m)',
    zlabel='Temperatura (K)'
)

#quiver plot da densidade de corrente
quiver(
    J_ans, dr, dtheta,
    title='Vetor densidade de corrente',
    xlabel='Coordenada X (m)',
    ylabel='Coordenada Y (m)',
    arrow_scale=1e-5,
)

#quiver plot do vetor fluxo de calor
quiver(
    fluxo_ans, dr, dtheta,
    title='Vetor fluxo de calor (W/m^2)',
    xlabel='Coordenada X (m)',
    ylabel='Coordenada Y (m)',
)