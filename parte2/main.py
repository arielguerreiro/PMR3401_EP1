from resolve_potencial import resolve_potencial
from plots import *
import numpy as np

#calcula a tensao de cada ponto da malha
V_ans = resolve_potencial(
    dr=0.001,
    dtheta=np.deg2rad(1),
    lamb=1.75,
    erro_des=1e-4
    )

heatmap_2d(V_ans, dr, dtheta)
surf_3d(V_ans, dr, dtheta)

