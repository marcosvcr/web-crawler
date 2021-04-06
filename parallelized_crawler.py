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

def get_1():
    driver = webdriver.Chrome(sys.argv[1])
    maxpage = 10
    number_visited = 0
    num = 0
    _response = True
    while _response == True and number_visited < maxpage:
        letter = random.choice(list(string.ascii_lowercase))
        num = num + 20
        number_visited= number_visited + 1
        path = "http://www.portaldalinguaportuguesa.org/index.php?action=fonetica&region=spx&act=list&letter=" + letter + "&start=" + str(num) 
        print(number_visited, "Accessing", path)
        driver.get(path)
        time.sleep(5)
        version_agent.append(driver.execute_script("return navigator.appVersion;"))
        name_agent.append(driver.execute_script("return navigator.appName;"))
        version_agent.append(driver.execute_script("return navigator.appVersion;"))
        locale.append(driver.execute_script("return Intl.DateTimeFormat().resolvedOptions().timeZone"))
        platform.append(driver.execute_script("return navigator.platform"))
        timer.append(driver.execute_script("return new Date()"))


def get_2():
    driver = webdriver.Chrome(sys.argv[1])
    maxpage = 10
    number_visited = 0
    num = 0
    _response = True
    while _response == True and number_visited < maxpage:
        letter = random.choice(list(string.ascii_lowercase))
        num = num + 20
        number_visited= number_visited + 1
        path = "http://www.portaldalinguaportuguesa.org/index.php?action=fonetica&region=spx&act=list&letter=" + letter + "&start=" + str(num) 
        print(number_visited, "Accessing", path)
        driver.get(path)
        time.sleep(5)
        version_agent.append(driver.execute_script("return navigator.appVersion;"))
        name_agent.append(driver.execute_script("return navigator.appName;"))
        version_agent.append(driver.execute_script("return navigator.appVersion;"))
        locale.append(driver.execute_script("return Intl.DateTimeFormat().resolvedOptions().timeZone"))
        platform.append(driver.execute_script("return navigator.platform"))
        timer.append(driver.execute_script("return new Date()"))



def get_3():
    driver = webdriver.Chrome(sys.argv[1])
    maxpage = 10
    number_visited = 0
    num = 0
    _response = True
    while _response == True and number_visited < maxpage:
        letter = random.choice(list(string.ascii_lowercase))
        num = num + 20
        number_visited= number_visited + 1
        path = "http://www.portaldalinguaportuguesa.org/index.php?action=fonetica&region=spx&act=list&letter=" + letter + "&start=" + str(num) 
        print(number_visited, "Accessing", path)
        driver.get(path)
        time.sleep(5)
        version_agent.append(driver.execute_script("return navigator.appVersion;"))
        name_agent.append(driver.execute_script("return navigator.appName;"))
        version_agent.append(driver.execute_script("return navigator.appVersion;"))
        locale.append(driver.execute_script("return Intl.DateTimeFormat().resolvedOptions().timeZone"))
        platform.append(driver.execute_script("return navigator.platform"))
        timer.append(driver.execute_script("return new Date()"))


def get_4():
    driver = webdriver.Chrome(sys.argv[1])
    maxpage = 10
    number_visited = 0
    num = 0
    _response = True
    while _response == True and number_visited < maxpage:
        letter = random.choice(list(string.ascii_lowercase))
        num = num + 20
        number_visited= number_visited + 1
        path = "http://www.portaldalinguaportuguesa.org/index.php?action=fonetica&region=spx&act=list&letter=" + letter + "&start=" + str(num) 
        print(number_visited, "Accessing", path)
        driver.get(path)
        time.sleep(5)
        version_agent.append(driver.execute_script("return navigator.appVersion;"))
        name_agent.append(driver.execute_script("return navigator.appName;"))
        version_agent.append(driver.execute_script("return navigator.appVersion;"))
        locale.append(driver.execute_script("return Intl.DateTimeFormat().resolvedOptions().timeZone"))
        platform.append(driver.execute_script("return navigator.platform"))
        timer.append(driver.execute_script("return new Date()"))


def get_5():
    driver = webdriver.Chrome(sys.argv[1])
    maxpage = 10
    number_visited = 0
    num = 0
    _response = True
    while _response == True and number_visited < maxpage:
        letter = random.choice(list(string.ascii_lowercase))
        num = num + 20
        number_visited= number_visited + 1
        path = "http://www.portaldalinguaportuguesa.org/index.php?action=fonetica&region=spx&act=list&letter=" + letter + "&start=" + str(num) 
        print(number_visited, "Accessing", path)
        driver.get(path)
        time.sleep(5)
        version_agent.append(driver.execute_script("return navigator.appVersion;"))
        name_agent.append(driver.execute_script("return navigator.appName;"))
        version_agent.append(driver.execute_script("return navigator.appVersion;"))
        locale.append(driver.execute_script("return Intl.DateTimeFormat().resolvedOptions().timeZone"))
        platform.append(driver.execute_script("return navigator.platform"))
        timer.append(driver.execute_script("return new Date()"))


if __name__ == '__main__':
    ThreadPool(10).map(get_1(),get_2(),get_3(),get_4(),get_5())