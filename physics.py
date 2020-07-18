import numpy as np
import numpy.linalg as la
import math

G = 6.67e-11


class Physics:

    @staticmethod
    def gravitational_force(m1, m2, r, radius_vector):
        """ returns a vector recording the force acting on m1 from m2 """
        f = ((G * m1 * m2) / r**3) * radius_vector
        return f

    @staticmethod
    def velocity(inital_v, dt, a):
        return inital_v + dt * a

    @staticmethod
    def displacement(velocity, time):
        return velocity * time


    # @staticmethod
    # def acceleration():

