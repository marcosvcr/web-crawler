import unittest

from nose.plugins.attrib import attr
import nose

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
import string
import random
import sys


name_agent = []
version_agent = []
locale = []
platform = []
timer = []



class Tests(unittest.TestCase):

    @attr(batch=("1"))
    def test_1(self):
        driver = sys.argv[1]
        webdriver.Chrome(driver)
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
            webdriver.get(path)
            time.sleep(5)
            name_agent.append(self.browser.execute_script("return navigator.appName;"))
            version_agent.append(self.browser.execute_script("return navigator.appVersion;"))
            locale.append(self.browser.execute_script("return Intl.DateTimeFormat().resolvedOptions().timeZone"))
            platform.append(self.browser.execute_script("return navigator.platform"))
            timer.append(self.browser.execute_script("return new Date()"))
            self.assertTrue(_response == True)

    @attr(batch=("2"))
    def test_2(self):
        driver = sys.argv[1]
        webdriver.Chrome(driver)
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
            webdriver.get(path)
            time.sleep(5)
            name_agent.append(self.browser.execute_script("return navigator.appName;"))
            version_agent.append(self.browser.execute_script("return navigator.appVersion;"))
            locale.append(self.browser.execute_script("return Intl.DateTimeFormat().resolvedOptions().timeZone"))
            platform.append(self.browser.execute_script("return navigator.platform"))
            timer.append(self.browser.execute_script("return new Date()"))
            self.assertTrue(_response == True)

    @attr(batch=("3"))
    def test_3(self):
        driver = sys.argv[1]
        webdriver.Chrome(driver)
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
            webdriver.get(path)
            time.sleep(5)
            name_agent.append(self.browser.execute_script("return navigator.appName;"))
            version_agent.append(self.browser.execute_script("return navigator.appVersion;"))
            locale.append(self.browser.execute_script("return Intl.DateTimeFormat().resolvedOptions().timeZone"))
            platform.append(self.browser.execute_script("return navigator.platform"))
            timer.append(self.browser.execute_script("return new Date()"))
            self.assertTrue(_response == True)

    @attr(batch=("4"))
    def test_4(self):
        driver = sys.argv[1]
        webdriver.Chrome(driver)
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
            webdriver.get(path)
            time.sleep(5)
            name_agent.append(self.browser.execute_script("return navigator.appName;"))
            version_agent.append(self.browser.execute_script("return navigator.appVersion;"))
            locale.append(self.browser.execute_script("return Intl.DateTimeFormat().resolvedOptions().timeZone"))
            platform.append(self.browser.execute_script("return navigator.platform"))
            timer.append(self.browser.execute_script("return new Date()"))
            self.assertTrue(_response == True)
    
    @attr(batch=("5"))
    def test_5(self):
        driver = sys.argv[1]
        webdriver.Chrome(driver)
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
            webdriver.get(path)
            time.sleep(5)
            name_agent.append(self.browser.execute_script("return navigator.appName;"))
            version_agent.append(self.browser.execute_script("return navigator.appVersion;"))
            locale.append(self.browser.execute_script("return Intl.DateTimeFormat().resolvedOptions().timeZone"))
            platform.append(self.browser.execute_script("return navigator.platform"))
            timer.append(self.browser.execute_script("return new Date()"))
            self.assertTrue(_response == True)

def get_cases():
    return [Tests]


def get_suite(cases):
    suite = unittest.TestSuite()
    for case in cases:
        tests = unittest.defaultTestLoader.loadTestsFromTestCase(case)
        suite.addTests(tests)


if __name__ == "__main__":
    nose.main(suite=get_suite(get_cases()))