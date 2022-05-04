import numpy
from vpython import *
from numpy import sin, cos, pi

numpy.set_printoptions(suppress=True, precision=6)

sphere(pos=vector(0, 0, 0), radius=1)
bj = sphere(radius=0.005, color=color.red,
            pos=vector(0, -cos(39.90960456049752 * pi / 180), sin(39.90960456049752 * pi / 180)))


l = box(pos=vector(0, 0, 0), size=vector(0.005, 0.005, 3))
e = compound([bj, l], origin=bj.pos)
t = 723
# 地球自转
e.rotate(angle=t * 2 * pi / 1440, axis=vec(0, 0, 1), origin=vector(0, 0, 0))
e.rotate(angle=-23.5 * pi / 180, axis=vec(1, 0, 0), origin=vector(0, 0, 0))
# 地球公转
e.rotate(angle=-t * 2 * pi / 525948, axis=vec(0, 0, 1), origin=vector(0, 0, 0))





print(e.pos)

# s = sphere(pos=vector(0, 0, 0), radius=1)
#
# r1 = ring(pos=vector(0, 0, 0), radius=1, thickness=0.005,
#           axis=vector(1, 0, 0))
#
# r2 = ring(pos=vector(0, 0, 0), radius=1, thickness=0.005,
#           axis=vector(0, 0, 1))
#
# l = box(pos=vector(0, 0, 0), size=vector(0.005, 3, 0.005))
#
# e = compound([s, r1, r2, l], origin=vector(0, 0, 0))
# e.texture = {
#     'file': textures.earth
# }
#
# e.rotate(angle=-23.5 * pi / 180, axis=vec(0,0,1), origin=vector(0,0,0))
#
#
#
x = arrow(pos=vector(0, 0, 0), axis=vector(1.4, 0, 0), shaftwidth=0.005)
y = arrow(pos=vector(0, 0, 0), axis=vector(0, 1.4, 0), shaftwidth=0.005)
z = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1.4), shaftwidth=0.005)
tx = text(text='x', pos=vector(1.2, 0, 0), height=0.05)
ty = text(text='y', pos=vector(0, 1.2, 0), height=0.05)
tz = text(text='z', pos=vector(0, 0, 1.2), height=0.05)
#
zbx = compound([x, y, z, tx, ty, tz], origin=vector(0, 0, 0))
#
#
# for i in range(40):
#     rate(20)
#     e.rotate(angle=pi / 100, axis=vec(sin(22.5 * pi / 180), cos(22.5 * pi / 180), 0), origin=vector(0,0,0))
#     zbx.rotate(angle=pi / 500, axis=vec(0, 1,0), origin=vector(0,0,0))
#


# handle = cylinder( size=vector(1,.2,.2),
#                    color=vector(0.72,0.42,0) )
#
# head = box( size=vector(.2,.6,.2), pos=vector(1.1,0,0),
#             color=color.gray(.6) )
#
# hammer = compound([s, l])
# hammer.axis = vector(1,1,0)
# hammer.pos = vector(0, 0, 0)
