import numpy as np
from star import Star
import numpy.linalg as la

from physics import Physics

class Universe:

    def __init__(self, radius, n_bodies, name):
        self._radius = radius
        self._n_bodies = n_bodies
        self._name = name
        self._star_list = []
        self._f_matrix = np.zeros(3, n_bodies)
        self._a_matrix = np.zeros(3, n_bodies)

    def add_star(self, star):
        self._star_list.append(star)

    def net_forces(self):
        count = 0
        for star in self._star_list:
            for star2 in self._star_list:
                if star != star2:
                    net_force = Physics.pairwise_force(star.get_mass(), star2.get_mass(),
                                                       self.get_distance(star.get_position(), star2.get_position()))
                    self._f_matrix[count]


    @staticmethod
    def get_distance(pos1, pos2):
        """ calculates eclidean distance between two particles """
        return la.norm(pos1 - pos2)

