#!/usr/bin/env python3


from xml.etree import ElementTree


def read_str() -> str:
    return input().strip()


def read_int() -> int:
    return int(read_str())


def xml_score(root: ElementTree) -> int:
    score = len(root.attrib)
    for child in root:
        score += xml_score(child)
    return score


def main() -> None:
    xml_str = str()
    for _ in range(read_int()):
        xml_str += read_str()
    root = ElementTree.fromstring(xml_str)
    score = xml_score(root)
    print(score)


if __name__ == '__main__':
    main()
