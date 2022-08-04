#!/usr/bin/env python3
from classes import Helper, Scraper

if __name__ == '__main__':
    Scraper.run(Helper.get_url_arg())
