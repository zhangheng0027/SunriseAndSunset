import numpy as np
from numpy import cos, sin, pi


def rotateX(s):
    return np.array([[1, 0, 0],
                     [0, cos(s), -sin(s)],
                     [0, sin(s), cos(s)]])


def rotateY(s):
    return np.array([[cos(s), 0, -sin(s)],
                     [0, 1, 0],
                     [sin(s), 0, cos(s)]])


def rotateZ(s):
    return np.array([[cos(s), -sin(s), 0],
                     [sin(s), cos(s), 0],
                     [0, 0, 1]])


def getZ(w, r):
    return r * sin(w * pi / 180)


def rotateTime(t, point):
    # 经过 t 分钟后 point 对应的坐标
    return rotateZ(-t * 2 * pi / 525948).dot(rotateX(-23.5 * pi / 180).dot(rotateZ(t * 2 * pi / 1440).dot(point.T))).T


if __name__ == "__main__":
    np.set_printoptions(suppress=True, precision=6)
    t = 723
    p = np.array([[0, -cos(39.90960456049752 * pi / 180), sin(39.90960456049752 * pi / 180)]])
    print(rotateTime(t, p))
