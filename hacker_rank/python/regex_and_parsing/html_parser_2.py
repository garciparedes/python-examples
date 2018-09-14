#!/usr/bin/env python3


from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, comment):
        out = str()
        if '\n' in comment:
            out += '>>> Multi-line Comment\n'
            for comment_line in comment.split('\n'):
                out += '{}\n'.format(comment_line)
        else:
            out += '>>> Single-line Comment\n'
            out += '{}\n'.format(comment)
        print(out, end='')

    def handle_data(self, data):
        if data is not '\n':
            out = str()
            out += '>>> Data\n'
            out += '{}\n'.format(data)
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
        text += '\n'
    show_html_stats(text)


if __name__ == '__main__':
    main()
