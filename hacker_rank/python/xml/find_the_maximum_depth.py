#!/usr/bin/env python3


from xml.etree import ElementTree


def read_str() -> str:
    return input().strip()


def read_int() -> int:
    return int(read_str())


maxdepth = 0
def depth(elem: ElementTree, level: int):
    global maxdepth
    # your code goes here


def main() -> None:
    xml_str = str()
    for _ in range(read_int()):
        xml_str += read_str()
    root = ElementTree.fromstring(xml_str)
    depth(root, - 1)
    print(maxdepth)


if __name__ == '__main__':
    main()
