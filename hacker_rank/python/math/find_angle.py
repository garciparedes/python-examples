#!/usr/bin/env python3

import math


def find_angle(ab: int, bc: int) -> float:
    cm = math.hypot(ab, bc) / 2
    xm = math.sin(math.atan(ab / bc)) * cm
    xc = math.sqrt(math.pow(cm, 2) - math.pow(xm, 2))
    theta = math.atan(xm / xc)
    return theta


def main() -> None:
    ab = int(input().strip())
    bc = int(input().strip())
    theta = find_angle(ab, bc)

    print('{:d}°'.format(round(math.degrees(theta))))


if __name__ == '__main__':
    main()
