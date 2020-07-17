from star import Star
from solar_system import SolarSystem
import vpython as vpy


def main():
    # time step - two weeks
    t = 1.2096e+6
    s = SolarSystem(2.50e+11, 2, "Solar System", t)
    s.add_star(Star(1.9890e+30, 0, 0, 6.96340e+5, 0, 0, 0, 2e+10, "Sun"))
    s.add_star(Star(5.9740e+24, 1.4960e+11, 0, 0, 0, 2.9800e+04, 0, 2e+9, "Earth"))

    while True:
        vpy.rate(200)
        s.net_forces()
        s.acceleration()
        s.velocity()


if __name__ == "__main__":
    main()
