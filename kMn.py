import random
from math import log, sqrt, floor
from time import time

import matplotlib.pyplot as plt
import numpy as np


def get_ratio(result_n, result_n_est):
    how_many = len(result_n)
    result_n = np.array(result_n)
    result_n_est = np.array(result_n_est)
    n_est_divided_by_n = result_n_est / result_n
    se_sum = sum(abs(n_est_divided_by_n - 1) <= 0.1)
    ratio = se_sum / how_many
    return ratio, se_sum, how_many, n_est_divided_by_n


def count_not_ones(array):
    return sum([1 for el in array if el != 1])


def hash1(number):
    return random.Random(number).random()


def kMn(set_m, array_len, f, *args):
    m_array = [1] * array_len
    for value in set_m:
        if len(args) > 0:
            hash_value = f(value, args[0])
        else:
            hash_value = f(value)
        if hash_value < m_array[-1] and hash_value not in m_array:
            m_array[-1] = hash_value
            m_array = sorted(m_array)
    if m_array[-1] == 1:
        return count_not_ones(m_array)
    else:
        return (array_len - 1) / m_array[-1]


def test_na_k():
    print('Test na to jak duze musi być k, aby 95% estymacji bylo dokladne z bledem do 10%')
    ratio = 0
    k = 300
    while ratio < 0.95:
        result_n = []
        result_n_est = []
        for n in gen_n(100):
            M = [10 * random.random() for _ in range(n)]
            n_est = kMn(M, k, hash1)
            result_n.append(n)
            result_n_est.append(n_est)
            ratio, se_sum, how_many, _ = get_ratio(result_n, result_n_est)
        k += 5
        print(k, ratio)


def gen_n(interval):
    i = 1
    k = 10 ** 4
    while i < k:
        if i < 10:
            i += interval - 1
        else:
            i += interval
        yield i


def rysuj_blad():
    n_list = [i for i in range(1, 10 ** 4)]  # list(gen_n())
    k_list = [200]
    k_result = []
    for k in k_list:
        s = time()
        result_n = []
        result_n_est = []
        for test in range(1, 2):
            for n in n_list:
                M = [10 ** 4 * random.random() for i in range(n)]

                # M = [n + i for i in range(n)]
                n_est = kMn(M, k, hash1)
                result_n.append(n)
                result_n_est.append(n_est)
                if n % 2000 == 0:
                    print("k={}, test_nr={}, n={}".format(k, test, n))
        e = time()

        ratio, se_sum, how_many, n_est_divided_by_n = get_ratio(result_n, result_n_est)
        print('k={}, |n_est/n-1|<0.1 = {}/{} = {}'.format(k, se_sum, how_many, ratio))
        print(str(se_sum) + '/' + str(how_many) + ' = ' + str(se_sum / how_many))
        k_result.append([result_n, n_est_divided_by_n])
        print(e - s)

    for (ind, lists) in enumerate(k_result):
        result_n = lists[0]
        n_est_divided_by_n = lists[1]
        plt.plot(result_n, n_est_divided_by_n, 'k*')
        plt.plot([min(n_list), max(n_list)], [1, 1], 'b')
        plt.title('k = {}'.format(k_list[ind]))
        plt.show()


def custom_hash(number, bits):
    modulo = 2 << bits
    return random.Random(number).randint(0, modulo) / modulo


def test_hash_function(n, k, how_many_tests):
    how_many_bits = []
    ns = [i * n for i in range(1, 11)]
    for n in ns:
        print(n, end=' ')
        bits = 1
        n_avg = -n
        while abs(n_avg) / n > 0.3:
            n_avg = -n
            for _ in range(how_many_tests):
                M = [random.random() for _ in range(n)]
                n_avg += kMn(M, k, custom_hash, bits) / how_many_tests
            bits += 1
        how_many_bits.append(bits)
    print()
    return ns, how_many_bits


def test_hash_function2(n, k, how_many_tests):
    error_list = []
    bits = 1
    n_avg = -n
    while abs(n_avg) / n > 0.01:
        n_avg = -n
        for _ in range(how_many_tests):
            M = [random.random() for _ in range(n)]
            n_avg += kMn(M, k, custom_hash, bits) / how_many_tests
        bits += 1
        error_list.append(abs(n_avg) / n)
    return error_list


def plot_test_result(n, k, how_many_tests):
    print('Calculating test number 1')
    ns, how_many_bits = test_hash_function(n, k, how_many_tests)
    print('Calculating test number 2')
    error_list = test_hash_function2(10 * n, 10 * k, how_many_tests)
    plt.subplot(121)
    plt.plot(ns, how_many_bits, 'r*')
    plt.title('Ilosc bitow do osiagniecia bledu < 0.1')
    plt.xlabel('n')
    plt.ylabel('Ilosc bitow')
    plt.xticks(ns)
    y = [log(x, 2) for x in ns]
    # 1.17sqrt(x)
    plt.plot(ns, y)
    plt.subplot(122)
    plt.plot(error_list, 'r*')
    plt.title('Blad (n_est-n)/n ze wzgledu na ilosc bitow funkcji haszujacej')
    plt.xlabel('Ilosc bitow')
    plt.ylabel('Blad')
    plt.yticks([0.1 * i for i in range(11)])
    plt.show()


# zad 4
def zad4():
    n = 1000
    k = n
    how_many_tests = 10
    plot_test_result(n, k, how_many_tests)


# zad 5
def plot_x_y(ax, sigma, n_max, col, leg=None):
    x = [0, n_max]
    y1 = [1 - sigma, 1 - sigma]
    y2 = [1 + sigma, 1 + sigma]
    ax.plot(x, y1, col)
    if leg is not None:
        ax.legend([leg])
    ax.plot(x, y2, col)


def zad5():
    n_max = 10000
    k = 400
    # M = [n_max * random.random() for _ in range(n_max)]
    n_list = list(range(1, n_max + 1, 20))
    n_est_by_n = []
    for n in n_list:
        M = [n_max * random.random() for _ in range(n)]
        n_est = kMn(M, k, hash1)
        n_est_by_n.append(n_est / n)

    alpha = [0.05, 0.01, 0.005]
    sigma_czebyszew = [sqrt(1 / ((k - 2) * a)) for a in alpha]
    # eqn= 2-0.005==exp(x)/((1+x)^(1+x))+exp(-x)/((1-x)^(1-x));
    sigma_chern = [0.1467, 0.19, 0.2071]
    est = np.array(n_est_by_n)
    tmp_n = len(est)
    from_data = [sorted(abs(1 - est))[int((1-a) * tmp_n)] for a in alpha]
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey='all')
    for data, s_cz, s_ch in zip(from_data, sigma_czebyszew, sigma_chern):
        plot_x_y(ax1, s_ch, n_max, 'b', 'Chernchoff')
        plot_x_y(ax1, data, n_max, 'y')

        plot_x_y(ax2, s_cz, n_max, 'g', 'Czebyszew')
        plot_x_y(ax2, data, n_max, 'y')

    ax1.plot(n_list, n_est_by_n, 'r*')
    ax2.plot(n_list, n_est_by_n, 'r*')
    plt.show()


def compare_kmn_with_hll():
    from hyperloglog import HyperLogLog
    n_max = 10000
    # 5(2^b) = 32k
    # k = 5 * 2^(b-5)
    bits = 8
    kmn_k = 2**(bits-5)
    n_est_kmn = []
    n_est_hll = []
    n_list = list(range(1, n_max + 1, 50))
    n_est_by_n_kmn = []
    n_est_by_n_hll = []
    for n in n_list:
        M = [n_max * random.random() for _ in range(n)]
        hll = HyperLogLog(M, bits)
        n_est_kmn = kMn(M, kmn_k, hash1)
        n_est_hll = hll.count()
        n_est_by_n_kmn.append(n_est_kmn / n)
        n_est_by_n_hll.append(n_est_hll / n)

    plt.subplot(121)
    plt.plot(n_list, n_est_by_n_kmn, '*')
    plt.title('k = {}'.format(kmn_k))
    plt.subplot(122)
    plt.plot(n_list, n_est_by_n_hll, '*')
    plt.title('bits = {}'.format(bits))
    plt.show()



compare_kmn_with_hll()
