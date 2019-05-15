#!/usr/bin/env python3

from collections import OrderedDict


def main() -> None:
    n = int(input().strip())

    dict_products = OrderedDict()
    for i in range(n):
        raw = input().strip().split(' ')
        price = int(raw[-1])
        name = ' '.join(raw[:-1])
        if name in dict_products:
            dict_products[name] += int(price)
        else:
            dict_products[name] = int(price)

    for name, price in dict_products.items():
        print(name, price, sep=' ')


if __name__ == '__main__':
    main()
