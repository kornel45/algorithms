import random
from hashlib import sha1
from math import log


class HyperLogLog:
    def __init__(self, m, bits):
        self.M = m
        self.bits = bits
        self.m = 1 << bits
        self.alpha = self.get_alpha()

    def get_alpha(self):
        if self.bits == 4:
            return 0.673
        if self.bits == 5:
            return 0.697
        if self.bits == 6:
            return 0.709
        return 0.7213 / (1.0 + 1.079 / self.m)

    @staticmethod
    def bit_length(w):
        return w.bit_length()

    def rho(self, w, max_width):
        rho = max_width - self.bit_length(w) + 1
        return rho

    def count(self):
        m_temp = [0 for _ in range(self.m)]
        for value in self.M:
            x = int(sha1(bytes(str(value), 'utf-8')).hexdigest()[:16], 16)
            j = x & (self.m - 1)
            w = x >> self.bits
            m_temp[j] = max(m_temp[j], self.rho(w, 64 - self.bits))
        n_est = self.alpha * self.m * self.m / sum([2 ** (-m_i) for m_i in m_temp])
        if n_est <= 5/2*self.m:
            v = m_temp.count(0)
            if v > 0:
                n_est = self.m * log(self.m / v)
        upp_limit = 2 ** 32
        if n_est > upp_limit/30:
            n_est = -upp_limit * log(1 - n_est/upp_limit)
        return round(n_est)

    @staticmethod
    def custom_hash(number, bits):
        modulo = 2 << bits
        return random.Random(number).randint(0, modulo) / modulo
