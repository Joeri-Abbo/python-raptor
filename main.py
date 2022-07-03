#!/usr/bin/env python3
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import time


def setup_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1200")
    # start web browser
    browser = webdriver.Firefox(
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

    items = page.find_elements_by_xpath("//script[@src]")

    if items:
        for item in items:
            urls.append(item.get_attribute("src"))
            if ".js" not in url:
                continue
            urls.append(url)
    return urls


def get_styles_of_page(page):
    urls = []

    # Remove urls without http because not interested
    #     Remove link part of

    items = page.find_elements_by_xpath("//link[@href]")

    if items:
        for item in items:
            urls.append(item.get_attribute("href"))
            if ".css" not in url:
                continue
            urls.append(url)
    return urls


if __name__ == '__main__':
    browser = setup_browser()

    url = input("Url to send the raptors to: ")

    page = get_page(browser, url)

    html = get_html_of_page(page)
    print(html)

    if get_styles_of_page(page):
        print('found styles:')
        for item in get_styles_of_page(page):
            print(item)

    if get_scripts_of_page(page):
        print('found scripts:')
        for item in get_scripts_of_page(page):
            print(item)
    # close web browser
    browser.close()
