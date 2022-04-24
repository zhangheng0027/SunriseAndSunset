from datetime import datetime

import numpy as np
from numpy import sin, cos, pi

np.set_printoptions(suppress=True, precision=6)


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


r = 1


def getPoint(j, w):
    # 北京天安门广场的经纬度 东经：116°23′17〃 冬至 2021年12月21 12:12:28 日中 指向太阳作为X正轴
    st1 = j - (116 + 23 / 60 + 17 / 3600) * pi / 180
    st2 = w
    x = r * cos(st2) * cos(st1)
    y = r * cos(st2) * sin(st1)
    z = r * sin(st2)
    return np.array([[x, y, z]])


beginTime = datetime.strptime("2021-12-21 12:12:28", "%Y-%m-%d %H:%M:%S")


def getMin(time):
    s = (time - beginTime).total_seconds()
    return s / 60


def getPoint1(point, minute):
    a1 = rotateZ(minute * 2 * pi / 1440)  # 自传
    a2 = rotateY(-23.5 * pi / 180)  # 自传与公转的夹角
    a3 = rotateZ(-minute * 2 * pi / 525948)  # 公转
    return a3.dot(a2.dot(a1.dot(point.T))).T


if __name__ == "__main__":
    # 116°23′17〃  39°54′27〃
    point = getPoint((116 + 23 / 60 + 17 / 3600) * pi / 180, (39 + 54 / 60 + 27 / 3600) * pi / 180)
    # endTime = datetime.strptime("2021-12-21 16:52:28", "%Y-%m-%d %H:%M:%S")
    # print(getMin(endTime))
    for i in range(270, 290):
        print(i, getPoint1(point, i))

    # p = np.array([[2, 0, 0]])
    # print(rotateY(pi / 2).dot(p.T))
