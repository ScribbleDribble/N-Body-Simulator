from particle import Particle
import vpython as vpy


class Star(Particle):

    def __init__(self, mass, initial_x, initial_y, initial_z, initial_vx, initial_vy, initial_vz, radius, name):
        super().__init__(mass, initial_x, initial_y, initial_z, initial_vx, initial_vy, initial_vz)
        self.name = name
        self.radius = radius
        self.planet_model = vpy.sphere(pos=vpy.vector(initial_x, initial_y, initial_z), radius=radius)


    def get_radius(self):
        return self.radius

    def draw(self):
        self.position = vpy.vector(self.position[0], self.position[1], self.position[2])
