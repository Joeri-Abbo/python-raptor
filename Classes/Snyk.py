import wget
import datetime
import os

time = str(datetime.datetime.now().timestamp())


# Get the work_dir to temp store the scan files.
def get_work_dir():
    return '_work/' + time + '/'


# Download the file
def download_file(url, file):
    wget.download(url, file)


# make the work dir
def make_work_dir():
    os.mkdir(get_work_dir())


# run the real snyk test command
def run_snyk():
    os.system("cd " + get_work_dir() + " && snyk test")


# Scan command
def scan(items):
    if len(items) < 2:
        exit('No valid args please add at lease 2')

    make_work_dir()
    print('lets download those files.')
    for item in items:
        download_file(item, get_work_dir() + item.rsplit('/', 1)[-1])
    run_snyk()
