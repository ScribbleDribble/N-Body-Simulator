import numpy as np


class Particle:

    def __init__(self, mass, x, y, z, initial_vx, initial_vy):
        self.mass = mass
        self.position = np.array([x, y, z])
        self.velocity = np.array([initial_vx, initial_vy])

    def draw(self):
        print("draw something dudeee")
