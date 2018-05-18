import numpy as np

n = 5
P = np.zeros((n, n))
ones = [(0, 1), (0, 2), (1, 3), (2, 1), (2, 3), (2, 4), (3, 0)]
I = np.ones((n, n))
for i, j in ones:
    P[i, j] = 1

P[n-1] = 1

pi = np.array([1/n] * n)
P = P * pi

alfa = [0, 0.25, 0.5, 0.75, 0.85, 1]


for a in alfa:
    M = (1-a) * P + a * I
    print((M ** 10)[2, :])



