import numpy as np
import matplotlib.pyplot as plt

class RK4():
    '''
    Implementação do RK4 clássico, recebendo um step, uma função e os valores iniciais

    **Entradas (para o init)**:
    func: função vetorial 'f'
    step: valor do passo
    x0: valor inicial do x
    y0: vetor inicial do y
    '''
    def __init__(self: object, func: np.array, step: float, x0: float, y0: np.array):
        #propriedades relevantes
        self.func = func #funcao de x e y
        self.step = step #assume step fixo
        self.x0 = x0 #valor da variavel independente
        self.y0 = y0 #vetor da variavel dependente


    def _compute_step(self, x, y):
        #calcula 1 step do método do RK4

        #calcula constantes seguindo RK4 classico
        k1 = self.func(x, y)

        k2 = self.func(x + self.step/2, y + self.step/2 * k1)

        k3 = self.func(x + self.step/2, y + self.step/2 * k2)

        k4 = self.func(x + self.step, y + self.step * k3)

        return y + self.step/6 * (k1 + 2 * k2 + 2 * k3 + k4)

    def solve(self, n_steps):
        #calcula um número 'n_steps' de iterações

        #formato do vetor: vec_y[instante, variavel]
        vec_y = np.zeros(shape=(n_steps, self.y0.shape[0]))
        vec_y[0, :] = self.y0

        vec_x = np.zeros(shape=(n_steps,))
        vec_x[0] = self.x0

        for i in range(0, n_steps-1, 1):

            vec_y[i + 1, :] = self._compute_step(vec_x[i], vec_y[i, :])
            vec_x[i + 1] = vec_x[i] + self.step

        return vec_x, vec_y



if __name__ == '__main__':

    def f(x, y):
        return np.array([
            -0.5*y[0],
            4 - 0.3*y[1] - 0.1*y[0]
        ])

    x0 = 0
    y0 = np.array([4, 6])
    h = 0.5

    runge = RK4(f, h, x0, y0)
    x, y = runge.solve(3)

    plt.plot(x, y[:, 0])
    plt.plot(x, y[:, 1])
    plt.show()




