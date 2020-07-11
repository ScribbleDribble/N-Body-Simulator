import numpy as np
import numpy.linalg as la

G = 6.67e-11


class Physics:

    @staticmethod
    def pairwise_force(m1, m2, r):
        f = (G * m1 * m2) / r**2
        return f

    @staticmethod
    def acceleration():

