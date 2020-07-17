import numpy as np
import numpy.linalg as la
import math

G = 6.67e-11


class Physics:

    @staticmethod
    def gravitational_force(m1, m2, r):
        f = (G * m1 * m2) / r**2
        return f

    @staticmethod
    def force_components(f, theta):
        return np.array([f * math.cos(theta), f * math.cos(90 - theta), f * math.sin(theta)])

    @staticmethod
    def velocity(inital_v, delta_t, a):
        return inital_v + delta_t * a

    @staticmethod
    def displacement(velocity, time):
        return velocity * time


    # @staticmethod
    # def acceleration():

