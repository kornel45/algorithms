import matplotlib.pyplot as plt
from random import random
from collections import Counter
import numpy as np


def ruch(current, lam, mu):
    x = random()
    if x < lam:
        return current + 1
    elif x < lam + mu:
        return max(0, current - 1)
    return current


n = 50000
c = Counter()
state_list = []
current = 0
l = 0.5
mu = l
for i in range(n):
    current = ruch(current, l, mu)
    c[current] += 1


x = []
y = []
for el in c.keys():
    x.append(el)
    y.append(c[el])


plt.plot(x, y)
plt.xlabel('Ile ludzi w kolejce')
plt.ylabel('Ile razy bylo tyle ludzi w kolejce')
plt.show()

