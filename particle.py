import numpy as np
import vpython as vpy
from physics import Physics


class Particle:

    def __init__(self, mass, x, y, z, vx, vy, vz, radius, name):
        self.mass = mass
        self.position = np.array([x, y, z])
        self.velocity = np.array([vx, vy, vz])
        self.name = name
        self.radius = radius
        # draws star into initial position
        self.planet_model = vpy.sphere(pos=vpy.vector(x, y, z), radius=radius,
                                       make_trail=True, trail_type='points', interval=10, retain=500)

    def set_position(self, v, dt):
        s = Physics.displacement(v, dt)
        self.position += s

    def get_mass(self):
        return self.mass

    def get_position(self):
        return self.position

    def get_velocity(self):
        return self.velocity[0], self.velocity[1], self.velocity[2]

    def get_name(self):
        return self.name

    def draw_update(self):
        self.planet_model.pos = vpy.vector(self.position[0], self.position[1], self.position[2])
