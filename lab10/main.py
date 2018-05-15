import numpy as np


n = 4
p = np.array([0, 3, 1, 6, 1, 1, 7, 1, 1, 7, 1, 1, 9, 1, 0, 0]) / 10
P = np.matrix(p.reshape((n, n)))
P32 = P ** 32
P128 = P ** 128

# a
print('Stationary distribution π = ({}, {}, {}, {})'.format(*P128[0].tolist()[0]))
# b
print('Probability of being in state 3 after 32 steps starting from state 0 is: {}'.format(P32[0, 3]))
# c
state_3 = np.sum(1/4 * P128[:, 3])
print('Probability of being in state 3 after 128 steps: {}'.format(state_3))
# d
e = [1/10, 1/100, 1/1000]
result_t = []

for eps in e:
    t = 2
    Pt = P.copy()
    while not((abs(Pt[0, :] - P128[0, :])).max() <= eps):
        Pt = P.copy() ** t
        t += 1
    result_t.append(t)

for el in zip(e, result_t):
    print('For eps = {} we need t = {} steps'.format(*el))

