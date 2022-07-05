#!/usr/bin/env python3
import Classes.WordPress as WordPress
import Classes.Browser as Browser

if __name__ == '__main__':
    browser = Browser.setup_browser()
    # url = input("Url to send the raptors to: ")
    url = "http://localhost/"
    print("Sending raptors to: " + url)
    page = Browser.get_page(browser, url)
    html = Browser.get_html_of_page(page)
    styles = Browser.get_styles_of_page(page)
    scripts = Browser.get_scripts_of_page(page)

    if styles:
        print('found styles:')
        # for style in styles:
        #     print(style)

    if scripts:
        print('found scripts:')
        # for script in scripts:
        #     print(script)

    Browser.get_server_settings(url)
    if WordPress.is_wordpress(scripts, styles):
        print("This site is a wordpress site")
        WordPress.get_information(browser, url, html, scripts, styles, page)
    else:
        print('Wow, this is not a wordpress')

    print('Done')
    # close web browser
    browser.close()
