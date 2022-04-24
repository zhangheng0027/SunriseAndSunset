from datetime import datetime

import numpy as np
from numpy import sin, cos, pi


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

    return np.array([[1, 0, 0]])


beginTime = datetime.strptime("2021-12-21 12:12:28", "%Y-%m-%d %H:%M:%S")


def getMin(time):
    s = (time - beginTime).total_seconds()
    return s / 60


def getPoint1(point, minute):
    a1 = rotateZ(minute * 2 * pi / 1440)  # 自传
    a2 = rotateY(-23.5 * pi / 180)  # 自传与公转的夹角
    a3 = rotateZ(minute * 2 * pi / 525948)  # 公转
    return a3.dot(a2.dot(a1.dot(point.T))).T


if __name__ == "__main__":
    getPoint(0, 0)
