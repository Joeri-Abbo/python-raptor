def get_information(url, html, scripts, styles, page):
    print('loaded')


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
