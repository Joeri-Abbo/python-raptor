import requests
from bs4 import BeautifulSoup
from classes import Helper


def get_information(with_login, browser, url, html, scripts, styles, page, cookies):
    print("Drupal detected")
    Helper.get_sitemap(url)


def is_drupal(cookies, url, scripts, styles):
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    for meta in soup.find_all("meta"):
        if meta.get('name') == 'Generator' and 'Drupal' in meta.get('content'):
            return True
    return False
