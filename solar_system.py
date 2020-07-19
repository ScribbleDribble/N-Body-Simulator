import numpy as np
import numpy.linalg as la
import math
from physics import Physics
from analytics import Analytics

class SolarSystem:

    def __init__(self, radius, name, time_step, n_bodies):
        self._radius = radius
        self._name = name
        self._body_list = []
        self._f_matrix = np.zeros(shape=(3, n_bodies))
        self.a_matrix = np.zeros(shape=(3, n_bodies))
        self.dt = time_step
        self._n_bodies = n_bodies
        self._analytics = Analytics()
        self._acceleration_analytics = Analytics()
        self._velocity_analytics = Analytics()
        self._t = 0

    def add_body(self, body):
        if len(self._body_list) > self._n_bodies:
            print(f"Cannot exceed no. bodies specified in instantiation of solar system ({self._n_bodies})")
            return

        self._body_list.append(body)

    def net_forces(self):
        """ produces a matrix of force components for all bodies """
        self._f_matrix.fill(0)
        count = 0

        for body in self._body_list:
            for body2 in self._body_list:
                if body != body2:
                    net_force = Physics.gravitational_force(body.get_mass(), body2.get_mass(),
                                                            self.euclidean_distance(body.get_position(),
                                                                                    body2.get_position()),
                                                            self.get_dist_change(body.get_position(),
                                                                                 body2.get_position()))

                    self._f_matrix[:, count] += net_force

            count += 1

        self._analytics.add_data(self._t, la.norm(self._f_matrix[:, 1]))

    def acceleration(self):
        """ updates acceleration matrix - ax, ay, az for each body """
        self.a_matrix.fill(0)

        for i, body in enumerate(self._body_list):
            self.a_matrix[:, i] = self._f_matrix[:, i] / body.get_mass()

        self._acceleration_analytics.add_data(self._t, la.norm(self.a_matrix[:, 1]))

    def velocity(self):
        """ updates velocity """
        for i, body in enumerate(self._body_list):
            v = Physics.velocity(body.get_velocity(), self.dt, self.a_matrix[:, i])
            body.set_position(v, self.dt)

            if i == 1:
                self._velocity_analytics.add_data(self._t, la.norm(v))

        self._t += self.dt
        self.render()

    @staticmethod
    def get_dist_change(pos1, pos2):
        """ returns difference in position: x = [dx, dy, dz] """
        return pos1 - pos2

    @staticmethod
    def euclidean_distance(pos1, pos2):
        """ calculates Euclidean distance between two particles """
        return la.norm(pos1 - pos2)

    def render(self):
        """ draws new position of all particles """
        for body in self._body_list:
            body.draw_update()

    def plot(self):
        self._acceleration_analytics.draw("Acceleration of a planet by time", "Acceleration (ms^-2)")
        self._analytics.draw("Force exerted on a planet by time", "Force (N)")
        self._velocity_analytics.draw("Velocity of a planet by time", "Velocity (ms^-1)")