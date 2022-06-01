from resolve_potencial import *
from plots import *
import numpy as np

#calcula a tensao de cada ponto da malha

dr = 0.001
dtheta = np.deg2rad(1)

V_ans = resolve_potencial(
    dr=dr,
    dtheta=dtheta,
    lamb=1.75,
    erro_des=1e-4
    )

heatmap_2d(V_ans, dr, dtheta)
surf_3d(V_ans, dr, dtheta)

J_ans = calcula_J(V_ans, dr, dtheta)

q_ans = calcula_qponto(J_ans, dr, dtheta)

surf_3d(q_ans, dr, dtheta)

quiver(J_ans, dr, dtheta)