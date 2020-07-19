import numpy as np
import numpy.linalg as la
import math

G = 6.67E-11


class Physics:

    @staticmethod
    def gravitational_force(m1, m2, r, radius_vector):
        """ returns a vector recording the force acting on m1 from m2 """
        return ((G * m1 * m2) / r**3) * radius_vector


    @staticmethod
    def velocity(u, dt, a):
        return u + dt * a

    @staticmethod
    def displacement(v, dt):
        return dt * v


    # @staticmethod
    # def acceleration():

