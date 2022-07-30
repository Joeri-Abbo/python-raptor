from Classes import Helper, Browser


def getInformation(url):
    Helper.line_breaker()
    print('🔬 Check for readme\'s')
    Helper.check_readme_files(Helper.get_base_url(url))
    Helper.line_breaker()
    Helper.check_docker_files(Helper.get_base_url(url))
    Browser.get_server_settings(url)
    Helper.line_breaker()
    Helper.try_composer(Helper.get_base_url(url))
    Helper.try_npm(Helper.get_base_url(url))
    Helper.try_robot(Helper.get_base_url(url))
