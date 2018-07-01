#!/usr/bin/env python3

from datetime import datetime

import enforce

DATE_TIME_FORMAT = '%a %d %b %Y %H:%M:%S %z'


@enforce.runtime_validation
def main() -> None:
    for _ in range(int(input())):
        print('{:.0f}'.format(
            abs(datetime.strptime(input().strip(), DATE_TIME_FORMAT)
                - datetime.strptime(input().strip(), DATE_TIME_FORMAT)
                ).total_seconds()))


if __name__ == '__main__':
    main()
