import time

import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from urllib.parse import urlparse
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


# Setup browser
def setup_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1200")
    # start web browser
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    return browser


# Get page
def get_page(browser, url):
    browser.get(url)
    time.sleep(2)
    return browser


# Get html of page
def get_html_of_page(page):
    return page.page_source


# Get scripts of page
def get_scripts_of_page(page):
    urls = []
    items = page.find_elements("xpath", "//script[@src]")

    if items:
        for item in items:
            url = item.get_attribute("src")
            if ".js" in url:
                urls.append(url)
    return urls


# Get styles of page
def get_styles_of_page(page):
    urls = []
    items = page.find_elements("xpath", "//link[@href]")

    if items:
        for item in items:
            url = item.get_attribute("href")
            if ".css" in url:
                urls.append(url)
    return urls


# Get base url
def get_base_url(url):
    base_url_object = urlparse(url)
    return base_url_object.scheme + "://" + base_url_object.netloc


# Check if id exist in page
def check_exists_by_id(browser, id):
    try:
        browser.find_element(By.ID, id)
    except NoSuchElementException:
        return False
    return True


# Get server settings from headers
def get_server_settings(url):
    print('🔬 Get server settings')
    request = requests.head(url)
    if "Server" in request.headers:
        print("Server : " + request.headers.get('Server'))
    if "X-Powered-By" in request.headers:
        print("Powered by : " + request.headers.get('X-Powered-By'))
