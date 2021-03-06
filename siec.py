import numpy as np
import matplotlib.pyplot as plt


def main():
    P = np.arange(-2, 2, 0.1)
    T = np.power(P, 2) + 1 * (np.random.choice(P) - 0.5)

    # siec
    S1 = 3
    W1 = np.random.rand(S1, 1) - 0.5
    B1 = np.random.rand(S1, 1) - 0.5
    W2 = np.random.rand(1, S1) - 0.5
    B2 = np.random.rand(1, 1) - 0.5
    lr = 0.01

    for epoka in range(1, 1000):
        # odpowiedz sieci
        s = W1 * P + B1 * np.ones_like(P)
        A1 = np.arctan(s)
        A2 = (W2 @ A1) + B2

        # propagacja wsteczna
        E2 = T - A2
        E1 = np.matrix.transpose(W2) @ E2

        dW2 = (lr * E2) @ np.matrix.transpose(A1)
        dB2 = (lr * E2) @ np.matrix.transpose(np.ones_like(E2))
        dW1 = (lr * (1. / (np.ones_like(s) + s * s)) * E1) @ (np.matrix.transpose(np.array(P)[np.newaxis]))
        dB1 = (lr * (1. / (np.ones_like(s) + s * s)) * E1) @ (
            np.matrix.transpose(np.array(np.ones_like(P))[np.newaxis]))

        W2 = W2 + dW2
        B2 = B2 + dB2
        W1 = W1 + dW1
        B1 = B1 + dB1

        if epoka % 10 == 0:
            plt.clf()
            plt.plot(P, T, 'r*')
            plt.plot(P, np.array(A2).flatten())
            plt.show()


if __name__ == '__main__':
    main()
