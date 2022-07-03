#!/usr/bin/env python3
import Classes.Wordpress as Wordpress
import Classes.Browser as Browser

if __name__ == '__main__':
    browser = Browser.setup_browser()
    # url = input("Url to send the raptors to: ")
    url = "https://tracefy.com/nl/"
    page = Browser.get_page(browser, url)
    html = Browser.get_html_of_page(page)
    styles = Browser.get_styles_of_page(page)
    scripts = Browser.get_scripts_of_page(page)

    if styles:
        print('found styles:')
        for style in styles:
            print(style)

    if scripts:
        print('found scripts:')
        for script in scripts:
            print(script)

    if Wordpress.is_wordpress(scripts, styles):
        print("This site is a wordpress site")
        Wordpress.get_information(url, html, scripts, styles, page)

    # close web browser
    browser.close()
