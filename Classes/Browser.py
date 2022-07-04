import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from urllib.parse import urlparse


def setup_browser():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1200")
    # start web browser
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    return browser


def get_page(browser, url):
    browser.get(url)
    time.sleep(2)
    return browser


def get_html_of_page(page):
    return page.page_source


def get_scripts_of_page(page):
    urls = []

    # Remove urls without http because not interested
    #     Remove link part of

    items = page.find_elements("xpath", "//script[@src]")

    if items:
        for item in items:
            url = item.get_attribute("src")
            if ".js" in url:
                urls.append(url)
    return urls


def get_styles_of_page(page):
    urls = []
    items = page.find_elements("xpath", "//link[@href]")

    if items:
        for item in items:
            url = item.get_attribute("href")
            if ".css" in url:
                urls.append(url)
    return urls


def get_base_url(url):
    base_url_object = urlparse(url)
    return base_url_object.scheme + "://" + base_url_object.netloc
