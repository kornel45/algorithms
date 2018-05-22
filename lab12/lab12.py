import decimal
from collections import Counter
from random import random

import matplotlib.pyplot as plt

decimal.getcontext().prec = 1000
import numpy as np


def ruch(current, lam, mu):
    x = random()
    if x < lam:
        return current + 1
    elif x < lam + mu:
        return max(0, current - 1)
    return current


n = 100000
c = Counter()
state_list = []
last_time = {}
time_sum = {}
current = 0
l = 0.35
mu = 1 - l
tmp = []
for i in range(n):
    current = ruch(current, l, mu)
    if current not in last_time.keys():
        last_time[current] = i
        time_sum[current] = i
    else:
        tmp_time = i - last_time[current]
        last_time[current] = i
        time_sum[current] += tmp_time
    tmp.append(current)
    c[current] += 1

how_many_people = []
how_many_times = []
for el in c.keys():
    how_many_people.append(el)
    how_many_times.append(c[el])

pi0 = decimal.Decimal(1 / sum([(l / mu) ** i for i in range(1, max(how_many_people))]))

pi = np.array([pi0] + [decimal.Decimal((l / mu)) ** n for n in range(1, max(how_many_people))])
pi /= sum(pi)

plt.subplot(221)
plt.plot(how_many_people, how_many_times, '*')
plt.plot(range(max(how_many_people)), pi * n)
plt.xlabel('Ile ludzi w kolejce')
plt.ylabel('Ile razy')

mean_time_to_comeback = {}
how_many_people2 = []
mean_time = []
for key in last_time.keys():
    mean_time_to_comeback[key] = time_sum[key] / c[key]
    if c[key] > 1:
        how_many_people2.append(key)
        mean_time.append(mean_time_to_comeback[key])

plt.subplot(222)

# plt.subplot(224)
plt.plot(range(max(how_many_people)), 1 / pi)
plt.plot(how_many_people2, mean_time, '*')
plt.xlabel('Ile ludzi w kolejce')
plt.ylabel('Jaki średni czas do powrotu')

plt.subplot(223)
plt.plot(range(len(tmp)), tmp)
plt.xlabel('Czas')
plt.ylabel('Ilosc ludzi w kolejce')

plt.show()
