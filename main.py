from particle import Particle
from solar_system import SolarSystem
import vpython as vpy


def main():
    # t = 1.2096e+6

    t = 0
    dt = 1
    s = SolarSystem(2.50e+11, "Solar System", dt, 3)

    # intial conditions obtained from date: A.D. 2020 - Jul - 18
    # vpy.scene.camera.pos = vpy.vector(5.72559063e+11, -3.90307823e+11, -2.22245751e+11)

    s.add_body(Particle(1.9890e+30, -8.115575219749061E+05, 1.023358542970559E+06, 1.030475383803935E+04,
                        -1.367124428632311E+01, -7.255536346983386E0, 3.953653246527174E-01,  7.000E7, "Sun"))

    s.add_body(Particle(6.4190e+23, 1.700911233235551E+08, -1.154793014669231E+08, -6.623490315706909E+06,
                        1.455681174959298E+04, 2.208572786142721E+04, 1.059053211570298E+03, 4e6, "Mars"))
    #
    # s.add_body(Particle(6.4190e+23, 1.136988932580810E+00, -7.719314514743499E-01, -4.427529806884417E-02,
    #                     8.407262277729954E-03, 1.275557518498364E-02, 6.116544109318913E-05, 2e+10, "Mars"))

    # s.add_body(Particle(1.9890e+30, 0, 0, 6.96340e+5, 0, 0, 0, 2e+10, "Sun"))
    # s.add_body(Particle(5.9740e+24, 1.4960e+11, 0, 0, 0, 2.9800e+04, 0, 4e3, "Earth"))
    s.add_body(Particle(5.9740e+24, 6.478846194962674E+07, -1.361379609312382E+08, 1.655851550595462E+04,
                        2.638665577941761E+01, 1.273331100378729E+01, -1.385515264764159E-03, 4e6, "Earth"))

    while t < 2e7:

        vpy.rate(200)
        s.net_forces()
        s.acceleration()
        s.velocity()
        t += dt


if __name__ == "__main__":
    main()
