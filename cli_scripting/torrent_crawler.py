#!/bin/python3

import urllib.request as req
import re
import os
from pathlib import Path


def main():
    url = input().strip()
    path = Path(input().strip())
    opener = req.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    req.install_opener(opener)
    page = req.urlopen(url).read().decode('utf-8')
    links = re.findall(r'"([^"]+\.torrent)"', page)
    for i, url in enumerate(links):
        file_name = "torrent_" + str(i) + ".torrent"
        req.urlretrieve(url, path / file_name)
        print(url)

if __name__ == '__main__':
    main()
