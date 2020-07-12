import numpy as np
from star import Star
import numpy.linalg as la
import math
from physics import Physics


class SolarSystem:

    def __init__(self, radius, n_bodies, name):
        self._radius = radius
        self._n_bodies = n_bodies
        self._name = name
        self._star_list = []
        self._f_matrix = np.zeros(shape=(3, n_bodies))
        self._a_matrix = np.zeros(shape=(3, n_bodies))

    def add_star(self, star):
        self._star_list.append(star)

    def net_forces(self):
        """ produces a matrix of force components for all stars """
        count = 0
        for star in self._star_list:
            for star2 in self._star_list:
                if star != star2:
                    net_force = Physics.gravitational_force(star.get_mass(), star2.get_mass(),
                                                            self.euclidean_distance(star.get_position(),
                                                                                    star2.get_position()))

                    self._f_matrix[:, count] = Physics.force_components(net_force,
                                                                        self.get_angle(
                                                                            self.get_dist_change(star, star2),
                                                                            self.euclidean_distance(star.get_position,
                                                                                                    star2.get_position))
                                                                        )
                    print(self._f_matrix)

                    count += 1

    @staticmethod
    def get_dist_change(star, star2):
        """ returns difference in position """
        return star.get_position() - star2.get_position()

    @staticmethod
    def euclidean_distance(pos1, pos2):
        """ calculates Euclidean distance between two particles """
        return la.norm(pos1 - pos2)

    @staticmethod
    def get_angle(delta_x, distance):
        return math.acos(delta_x / distance)
