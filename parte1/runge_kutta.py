import numpy as np
import matplotlib.pyplot as plt


#implementação do RK4 classico

class RK4():
    def __init__(self, func, step, x0, y0):
        self.func = func #espera funcao de x e y
        self.step = step #assume step fixo
        self.x0 = x0 #vetor da variavel independente
        self.y0 = y0 #vetor da variavel dependente

    def compute_step(self, x, y):

        #calcula constantes seguindo RK4 classico
        k1 = self.func(x, y)

        k2 = self.func(x + self.step/2, y + self.step/2 * k1)

        k3 = self.func(x + self.step/2, y + self.step/2 * k2)

        k4 = self.func(x + self.step, y + self.step*k3)

        return y + self.step/6 * (k1 + 2*k2 + 2*k3 + k4)

    def solve(self, length):

        #formato do vetor: vec_y[instante, variavel]
        vec_y = np.zeros(shape=(length, self.y0.shape[0]))
        vec_y[0, :] = self.y0

        vec_x = np.zeros(shape=(length,))
        vec_x[0] = self.x0

        for i in range(0, length-1, 1):

            vec_y[i + 1, :] = self.compute_step(vec_x[i], vec_y[i, :])
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




