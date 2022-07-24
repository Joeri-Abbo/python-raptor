#!/usr/bin/env python3
import Classes.WordPress as WordPress
import Classes.Browser as Browser
import Classes.Laravel as Laravel
import sys

if __name__ == '__main__':
    if 'withLogin' in sys.argv:
        with_login = True
    else:
        with_login = False

    url = False
    if sys.argv:
        for arg in sys.argv:
            if 'u=' in arg:
                url = arg[2:]

    if not url:
        url = input("Url to send the raptors to: ")
        # url = "http://localhost/"

    browser = Browser.setup_browser()

    print("Sending raptors to: " + url)
    page = Browser.get_page(browser, url)
    html = Browser.get_html_of_page(page)
    styles = Browser.get_styles_of_page(page)
    scripts = Browser.get_scripts_of_page(page)
    cookies = page.get_cookies()

    if styles:
        print('found styles:')
        # for style in styles:
        #     print(style)

    if scripts:
        print('found scripts:')
        # for script in scripts:
        #     print(script)

    Browser.get_server_settings(url)

    if WordPress.is_wordpress(cookies, url, scripts, styles):
        print("This site is a wordpress site")
        WordPress.get_information(with_login, browser, url, html, scripts, styles, page, cookies)
    elif Laravel.is_laravel(cookies, url, scripts, styles):
        print("This site is a laravel site")
        Laravel.get_information(with_login, browser, url, html, scripts, styles, page, cookies)
    else:
        print('Wow, this is not a wordpress or laravel site lets try something else')

    print('Done')
    # close web browser
    browser.close()
