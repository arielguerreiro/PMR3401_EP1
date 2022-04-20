import numpy as np
from runge_kutta import RK4
import matplotlib.pyplot as plt

# variaveis globais
Lb = 0.5
Rb = 20
C = 0.002
La = 0.01
Ra = 200


def e(t):
    return np.cos(t * 600) / La


def f(t, Y):
    '''
    O vetor de variaveis dependentes é dado por:

            | ------ |
            |  q(t)  |
    Y(t) =  | i_1(t) |
            | i_2(t) |
            | ------ |
    '''

    return np.array([
        Y[1] - Y[2],
        1 / La * (e(t) - Ra * (Y[1] - Y[2]) - Y[0] / C),
        1 / Lb * (Ra * (Y[1] - Y[2]) - Rb * Y[2] + Y[0] / C)
    ])


if __name__ == '__main__':
    delta_t = 0.0001
    t0 = 0

    tmax = 0.1

    length = int(tmax / delta_t)

    Y0 = np.array([
        0,
        0,
        0
    ])

    edo = RK4(func=f, step=delta_t, x0=t0, y0=Y0)

    t_int, y_int = edo.solve(length)

    ydot_int = np.array([f(t_int[i], y_int[i, :]) for i in range(len(t_int))])

    plot_scalars = {
        'q': 1e5,
        'i1': 1e2,
        'i2': 1e2,
        'i1dot': 0.1,
        'i2dot': 0.1,
    }

    #plot dos valores

    plt.plot(t_int, y_int[:, 0] * plot_scalars['q'])
    plt.plot(t_int, y_int[:, 1] * plot_scalars['i1'])
    plt.plot(t_int, y_int[:, 2] * plot_scalars['i2'])

    #plot das derivadas
    plt.plot(t_int, ydot_int[:, 1] * plot_scalars['i1dot'])
    plt.plot(t_int, ydot_int[:, 2] * plot_scalars['i2dot'])

    plt.legend([f'{key}*{value:.2E}' for key, value in plot_scalars.items()])

    top_limit = 150
    plt.ylim(top=top_limit, bottom=-top_limit)

    plt.title(f'Passo: {delta_t}, integracao de {t0} a {tmax}')
    plt.grid(True)

    plt.show()
