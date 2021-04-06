import sys
from multiprocessing.pool import ThreadPool, Pool
from selenium import webdriver
import time
import pandas as pd
import string
import random
import sys

import threading

threadLocal = threading.local()


name_agent = []
version_agent = []
locale = []
platform = []
timer = []

def get_driver():
  driver = getattr(threadLocal, 'driver', None)
  if driver is None:
    driver = webdriver.Chrome(sys.argv[1])
    setattr(threadLocal, 'driver', driver)
  return driver


def generate_links(url):
    links = []    
    maxpage = 10
    number_visited = 0
    num = 0


    while number_visited < maxpage:
        letter = random.choice(list(string.ascii_lowercase))
        number_visited= number_visited + 1 
        path = url + letter + "&start=" + str(num)
        num = num + 20
        links.append(path)
    return links


def get_info(url):
    driver = get_driver()
    driver.get(url)
    time.sleep(5)
    _version_agent = driver.execute_script("return navigator.appVersion;")
    _name_agent = driver.execute_script("return navigator.appName;")
    _version_agent = driver.execute_script("return navigator.appVersion;")
    _locale = driver.execute_script("return Intl.DateTimeFormat().resolvedOptions().timeZone")
    _platform = driver.execute_script("return navigator.platform")
    _timer = driver.execute_script("return new Date()")
    print(_name_agent)
    print(_version_agent)
    print(_locale)
    print(_platform)
    print(_timer)
 
    
if __name__ == '__main__':
    url = "http://www.portaldalinguaportuguesa.org/index.php?action=fonetica&region=spx&act=list&letter="
    Pool(5).map(get_info,generate_links(url))