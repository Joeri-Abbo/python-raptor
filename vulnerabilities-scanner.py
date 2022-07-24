#!/usr/bin/env python3
import sys
import wget
import datetime
import os

if __name__ == '__main__':
    items = []
    for url in sys.argv:
        if url.startswith(".") or url.startswith('vulnerabilities-s'):
            continue
        items.append(url)

    if len(items) < 2:
        exit('No valid args please add at lease 2')

    work_dir = '_work/' + str(datetime.datetime.now().timestamp()) + '/'
    os.mkdir(work_dir)

    print('lets download those files.')
    for item in items:
        wget.download(item, work_dir + item.rsplit('/', 1)[-1])
    os.system("cd " + work_dir + " && snyk test")
