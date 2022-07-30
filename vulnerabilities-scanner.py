#!/usr/bin/env python3
import sys
from Classes import Snyk

if __name__ == '__main__':
    items = []
    for url in sys.argv:
        if url.startswith(".") or url.startswith('vulnerabilities-s'):
            continue
        items.append(url)
    Snyk.scan(items)
