import numpy as np


class Particle:

    def __init__(self, mass, x, y, z):
        self.mass = mass
        self.position = np.array(x, y, z)

    def draw(self):
        print("draw something dudeee")
