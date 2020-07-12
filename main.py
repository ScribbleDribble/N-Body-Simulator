from star import Star
from solar_system import SolarSystem


def main():
    s = SolarSystem(2.50e+11, 2, "Solar System")
    s.add_star(Star(1.9890e+30, 0, 0, 6.96340e+5, "Sun"))
    s.add_star(Star(5.9740e+24, 1.4960e+11, 0, 0, "Earth"))
    s.net_forces()


if __name__ == "__main__":
    main()
