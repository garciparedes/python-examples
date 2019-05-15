#!/usr/bin/env python3

import math


class Points(object):
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other: 'Points') -> 'Points':
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Points(x, y, z)

    def dot(self, other: 'Points') -> float:
        value = (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
        return value

    def cross(self, other: 'Points') -> 'Points':
        x = (self.y * other.z) - (self.z * other.y)
        y = (self.z * other.x) - (self.x * other.z)
        z = (self.x * other.y) - (self.y * other.x)
        return Points(x, y, z)

    def absolute(self) -> float:
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


def main():
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))


if __name__ == '__main__':
    main()
