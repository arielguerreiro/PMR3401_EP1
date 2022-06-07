import numpy as np
from runge_kutta import RK4
import matplotlib.pyplot as plt

# variaveis globais
Lb = 0.5
Rb = 20
C = 0.002
La = 0.01
Ra = 2000


def e(t):
    #funcao da corrente eletrica
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
    #delta_t = 0.01 #grande
    #delta_t = 0.0001 #medio
    delta_t = 1e-6 #pequeno
    t0 = 0

    tmax = 0.03

    n_steps = int(tmax / delta_t) #define numero de steps de integracao

    Y0 = np.array([
        0,
        0,
        0
    ])

    edo = RK4(func=f, step=delta_t, x0=t0, y0=Y0)

    #resolve sistema por RK4 com o numero de steps definido
    t_int, y_int = edo.solve(n_steps)

    #calcula a derivada de [Y] por meio de [F]
    ydot_int = np.array([f(t_int[i], y_int[i, :]) for i in range(len(t_int))])

    #define constantes para multiplicar cada uma das respostas
    plot_scalars = {
        'q': 1e5,
        'i_1': 1e2,
        'i_2': 1e2,
        '\dot{i_1}': 0.1,
        '\dot{i_2}': 0.1,
    }

    #plot dos valores
    plt.plot(t_int, y_int[:, 0] * plot_scalars['q'])
    plt.plot(t_int, y_int[:, 1] * plot_scalars['i_1'])
    plt.plot(t_int, y_int[:, 2] * plot_scalars['i_2'])

    #plot das derivadas
    plt.plot(t_int, ydot_int[:, 1] * plot_scalars['\dot{i_1}'])
    plt.plot(t_int, ydot_int[:, 2] * plot_scalars['\dot{i_1}'])

    plt.legend([f'${key} \cdot {value:.2e}$' for key, value in plot_scalars.items()])

    top_limit = 50
    plt.ylim(top=top_limit, bottom=-top_limit)

    plt.title(f'Integração de {t0} a {tmax} com passo {delta_t:.2e}')
    plt.grid(True)

    plt.show()
