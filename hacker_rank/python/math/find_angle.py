#!/usr/bin/env python3

import enforce

import math


@enforce.runtime_validation
def main() -> None:
    ab = int(input().strip())
    bc = int(input().strip())
    cm = math.hypot(ab, bc) / 2
    xm = math.sin(math.atan(ab / bc)) * cm
    xc = math.sqrt(math.pow(cm, 2) - math.pow(xm, 2))
    theta = math.atan(xm / xc)

    print('{:d}°'.format(round(math.degrees(theta))))


if __name__ == '__main__':
    main()