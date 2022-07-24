import requests


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
    print('🔬 Get information')
