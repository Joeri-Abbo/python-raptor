#!/usr/bin/env python3
import sys

import Classes.snyk as snyk

if __name__ == '__main__':
    items = []
    for url in sys.argv:
        if url.startswith(".") or url.startswith('vulnerabilities-s'):
            continue
        items.append(url)
    snyk.scan(items)
