import numpy as np
from physics import Physics


class Particle:

    def __init__(self, mass, x, y, z, initial_vx, initial_vy, initial_vz):
        self.mass = mass
        self.position = np.array([x, y, z])
        self.velocity = np.array([initial_vx, initial_vy, initial_vz])

    def set_position(self, vx, vy, vz, time):
        self.position = np.array([Physics.displacement(vx, time) + self.position[0], Physics.displacement(vy, time)
                                  + self.position[1], Physics.displacement(vz, time) + self.position[2]])
        print(self.position)

    def get_mass(self):
        return self.mass

    def get_position(self):
        return self.position

    def get_velocity(self):
        return self.velocity[0], self.velocity[1], self.velocity[2]



    # def draw(self):
    #     print("draw something dudeee")
