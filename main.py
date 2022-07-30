#!/usr/bin/env python3
import Classes.Frameworks.WordPress as WordPress
import Classes.Browser as Browser
import Classes.Frameworks.Laravel as Laravel
import Classes.Frameworks.Drupal as Drupal
import Classes.Frameworks.NoFramework as NoFramework
import Classes.Helper as Helper
import Classes.BaseInformation as BaseInformation
import sys

from Classes import Scraper

if __name__ == '__main__':
    with_login = with_browser = with_scraper = False

    if 'withBrowser' in sys.argv:
        with_browser = True

    if 'withScraper' in sys.argv:
        with_scraper = True

    if 'withLogin' in sys.argv:
        with_login = True

    url = Helper.get_url_arg()

    proxy_server = False
    if sys.argv:
        for arg in sys.argv:
            if 'p=' in arg:
                proxy_server = arg[2:]
    if proxy_server:
        if not proxy_server:
            if Helper.yes_or_no("No proxy server provided. Do you want to use a proxy server?"):
                proxy_server = input("Proxy server: ")
                if not proxy_server:
                    proxy_server = False

    browser = Browser.setup_browser(with_browser, proxy_server)

    print("Sending raptors to: " + url)
    page = Browser.get_page(browser, url)
    html = Browser.get_html_of_page(page)
    styles = Browser.get_styles_of_page(page)
    scripts = Browser.get_scripts_of_page(page)
    cookies = page.get_cookies()

    BaseInformation.getInformation(url)

    if WordPress.is_wordpress(cookies, url, scripts, styles):
        WordPress.get_information(with_login, browser, url, html, scripts, styles, page, cookies)
    elif Drupal.is_drupal(cookies, url, scripts, styles):
        Drupal.get_information(with_login, browser, url, html, scripts, styles, page, cookies)
    elif Laravel.is_laravel(cookies, url, scripts, styles):
        Laravel.get_information(with_login, browser, url, html, scripts, styles, page, cookies)
    else:
        NoFramework.get_information(with_login, browser, url, html, scripts, styles, page, cookies)

    if with_scraper:
        Scraper.run(url)
    print('Done')
    # close web browser
    browser.close()
