import vpython as vpy
from star import Star
from solar_system import SolarSystem

#  In the VPython window, hold down the left+right buttons on a two-button mouse (or the Alt key) and move the
# mouse. You should see that you are able to zoom into and out of the scene.
# Now try holding down the right mouse button (or the Ctrl key). You should find that you are able to rotate around
# the sphere (you can tell that you are moving because the lighting changes).



# ball = vpy.sphere(pos=vpy.vector(-5, 0, 0), radius=3, color=vpy.color.blue)



delta_t = 0.5
t = 0

while True:
    vpy.rate(100)

    ball.pos = ball.pos + vpy.vector(4,0,0) * delta_t
    t += delta_t
