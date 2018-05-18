import numpy as np
np.set_printoptions(precision=3, suppress=True)

n = 6
P = np.zeros((n, n))
P[0, 0] = 1
P[1, 2] = 1/2
P[1, 4] = 1/2
P[2, 0] = 1
P[3, 1] = 1/2
P[3, 4] = 1/2
P[4, 1] = 1/2
P[4, 3] = 1/2
P[5, 2] = 1
J = np.ones((n, n))
alfa = [0, 0.15, 0.5, 1]

print(P)

for a in alfa:
    M = (1-a) * P + a * 1/n * J
    # print(M ** 32)


# Pt = P.copy()
# Pt[1, 2] = 0
# Pt[1, 4] = 1
#
# for a in alfa:
#     M = (1-a) * Pt + a * 1/n * J
#     print(M)
