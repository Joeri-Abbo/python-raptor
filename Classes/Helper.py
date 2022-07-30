from urllib.parse import urlparse
import requests
import sys


# Get base url
def get_base_url(url):
    base_url_object = urlparse(url)
    return base_url_object.scheme + "://" + base_url_object.netloc


# Try triggering php errors
def try_trigger_php_error(url):
    response = requests.get(url)
    if response.status_code == 500:
        print('🔥 PHP error triggered!')
        print(url)


# Check if file exists in folder
def file_exists_on_url(url, file):
    url = url + '/' + file
    response = requests.get(url)
    if response.status_code == 200:
        print('🔥 ' + file + ' found! Did the developer make a backdoor for me?')
        print(url)


# Just place a linebreak
def line_breaker():
    print(get_line_breaker())


def get_line_breaker():
    return '============================================================'


# Check if a readme variant exist on the url
def check_readme_files(url):
    readme_files = ['readme.txt', 'readme.md', 'readme.html', 'readme.htm', 'readme.php', 'readme.xml', 'readme.json',
                    'readme.yml', 'phtml']
    check_files_exists(url, readme_files)


# Check if a readme variant exist on the url
def check_docker_files(url):
    docker_files = ['docker-compose.yml', 'docker-compose.yaml', 'docker-compose.json', 'Dockerfile']
    check_files_exists(url, docker_files)


# Check if file exist
def check_files_exists(url, files):
    for file in files:
        response = requests.get(url + '/' + file)
        if response.status_code == 200 and response.url == url + '/' + file:
            print('🔥 ' + file + ' found!')
            print(url + '/' + file)


# yes or no input
def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question + ' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False


# Check if root has composer.json
def try_composer(url):
    file_exists_on_url(url, "composer.json")
    file_exists_on_url(url, "composer.lock")


# Try npm files
def try_npm(url):
    file_exists_on_url(url, "package.json")
    file_exists_on_url(url, "package-lock.json")
    file_exists_on_url(url, "yarn.lock")
    file_exists_on_url(url, "pnpm-lock.yaml")
    file_exists_on_url(url, "webpack.mix.js")
    file_exists_on_url(url, "tailwind.config.js")


def get_url_arg():
    url = False
    if sys.argv:
        for arg in sys.argv:
            if 'u=' in arg:
                url = arg[2:]

    if not url:
        url = input("Url to scan: ")

    return url
