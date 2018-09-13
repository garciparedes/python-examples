#!/usr/bin/env python3


from html.parser import HTMLParser


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        out = str()
        out += 'Start : {}\n'.format(tag)
        for attr in attrs:
            out += '-> {} > {}\n'.format(*attr)
        print(out, end='')

    def handle_endtag(self, tag):
        out = str()
        out += 'End   : {}\n'.format(tag)
        print(out, end='')

    def handle_startendtag(self, tag, attrs):
        out = str()
        out += ('Empty : {}\n'.format(tag))
        for attr in attrs:
            out += '-> {} > {}\n'.format(*attr)
        print(out, end='')


def read_str() -> str:
    return input().strip()


def read_int() -> int:
    return int(read_str())


def show_html_stats(html_str: str) -> None:
    parser = MyHTMLParser()
    parser.feed(html_str)


def main() -> None:
    text = str()
    for _ in range(read_int()):
        text += read_str()
    show_html_stats(text)


if __name__ == '__main__':
    main()
