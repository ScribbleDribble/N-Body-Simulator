from particle import Particle
from solar_system import SolarSystem
import vpython as vpy


def main():

    t = 0
    dt = 1
    s = SolarSystem(2.50e+11, "Solar System", dt, 3)

    # Data info
    # initial conditions obtained from date: A.D. 2020 - Jul - 18
    # vector ephemeris data is obtained from: https://ssd.jpl.nasa.gov/horizons.cgi#top
    # km/s converted to m/s

    s.add_body(Particle(1.9890e+30, -8.115575219749061E+05, 1.023358542970559E+06, 1.030475383803935E+04,
                        -1.367124428632311E+01, -7.255536346983386E0, 3.953653246527174E-01,  7.000E+06, "Sun"))
    # #
    s.add_body(Particle(6.4190e+23, 1.700911233235551E+08, -1.154793014669231E+08, -6.623490315706909E+06,
                        1.455681174959298E+04, 2.208572786142721E+04, 1.059053211570298E+03, 4.000E+05, "Mars"))
    #
    #
    # s.add_body(Particle(5.9740e+24, 6.478846194962674E+07, -1.361379609312382E+08, 1.655851550595462E+04,
    #                     2.638665577941761E+04, 1.273331100378729E+04, -1.385515264764159E00, 5.000E+06, "Earth"))

    # s.add_body(Particle(1.8982E+27, 2.925974889403378E+08, -7.120923141565894E+08, -3.592415407148212E+06,
    #                     1.192504812263601E+04, 5.588195368858322E+03, -2.898746577296276E+02, 8.000E+06, "Jupiter"))

    # s.add_body(Particle(7.34767309E+22, 6.484283712254966E+07, -1.357523313359251E+08, 1.235756001138687E+04,
    #                     2.538303859564986E+04, 1.282111106220561E+04, 9.061949758449295E+01, 5.000E+04, "Moon (Earth)"))

    while t < 25000:

        vpy.rate(100)
        s.net_forces()
        s.acceleration()
        s.velocity()
        t += dt

    s.plot()

if __name__ == "__main__":
    main()
