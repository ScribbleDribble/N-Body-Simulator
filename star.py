from particle import Particle


class Star(Particle):

    def __init__(self, mass, x, y, z, name, universe):
        super().__init__(mass, x, y, z)
        self.name = name
        self.universe = universe

    def get_mass(self):
        return self.mass

    def get_position(self):
        return self.position
