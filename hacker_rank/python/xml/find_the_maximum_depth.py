#!/usr/bin/env python3


from xml.etree import ElementTree


def read_str() -> str:
    return input().strip()


def read_int() -> int:
    return int(read_str())


def depth(elem: ElementTree, level: int = 0):
    max_depth = level
    for child in elem:
        current_depth = depth(child, level + 1)
        max_depth = max(max_depth, current_depth)
    return max_depth


def main() -> None:
    xml_str = str()
    for _ in range(read_int()):
        xml_str += read_str()
    root = ElementTree.fromstring(xml_str)
    max_depth = depth(root)
    print(max_depth)


if __name__ == '__main__':
    main()
