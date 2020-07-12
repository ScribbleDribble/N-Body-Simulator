from particle import Particle


class Star(Particle):

    def __init__(self, mass, initial_x, initial_y, intial_z, initial_vx, initial_vy, name):
        super().__init__(mass, initial_x, initial_y, intial_z, initial_vx, initial_vy)
        self.name = name

    def get_mass(self):
        return self.mass

    def get_position(self):
        return self.position
