from scipy.integrate import odeint
import numpy as np

def f(x, y):
    return np.array([
        -0.5 * y[0],
        4 - 0.3 * y[1] - 0.1 * y[0]
    ])


x0 = 0
y0 = np.array([4, 6])
h = 0.001

t = np.linspace(0, 1, int(1/h))

y = odeint(f, y0, t)

import pdb; pdb.set_trace()
