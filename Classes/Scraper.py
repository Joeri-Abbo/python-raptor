import os
from urllib.parse import urlparse
import datetime
from Classes import Helper
import requests
from bs4 import BeautifulSoup

visited = []
scrape = []
time = str(datetime.datetime.now().timestamp())


# Vist url and write urls to file
def visit_url(file, domain, url):
    if url in visited:
        return False
    print(url)
    file.write(Helper.get_line_breaker() + "\n")
    file.write(url + "\n")
    file.write(Helper.get_line_breaker() + "\n")

    grab = requests.get(url)
    soup = BeautifulSoup(grab.text, 'html.parser')
    for link in soup.find_all("a"):
        data = link.get('href')
        if data and data.startswith("http"):
            file.write(data + "\n")
            if '//' + domain in data or 'www.' + domain in data:
                scrape.append(data)
    visited.append(url)
    if url in scrape:
        scrape.remove(url)


# Run scraper loop
def run_scrape(file, domain):
    while scrape:
        url = scrape.pop()
        visit_url(file, domain, url)


# Run scraper
def run(url):
    file_path = '_scraper/' + time + '/'
    os.mkdir(file_path)

    domain = urlparse(url).netloc
    file = open(file_path + domain.replace('.', '-') + '.txt', "w")

    scrape.append(url)
    run_scrape(file, domain)
