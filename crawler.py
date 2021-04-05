from selenium import webdriver
import time
import pandas as pd
import string
import random
import sys
class Crawler:


    def __init__(self, driver):
        super(Crawler,self)
        self.alphabet = list(string.ascii_lowercase)
        self.browser= webdriver.Chrome(driver)
        self.name_agent = []
        self.version_agent = []
        self.locale = []
        self.platform = []
        self.timer = []

    def finish(self):
        self.browser.quit()


    def spyder(self,url):

        maxpage = 50
        number_visited = 0
        num = 0
        _response = True
        while _response == True and number_visited < maxpage:
            letter = random.choice(self.alphabet)
            number_visited+=1
            path = url + letter + "&start=" + str(num) 
            print(number_visited, "Accessing", path)
            self.browser.get(path)
            time.sleep(5)
            self.getInfo()
            print("Success")
            num = num + 20
        df = pd.DataFrame({"Name": self.name_agent, "Version": self.version_agent, "Location:": self.locale, "Platform": self.platform, "Time": self.timer})
        df.to_csv("agent_info.csv", sep=";")
    def getInfo(self):
        self.name_agent.append(self.browser.execute_script("return navigator.appName;"))
        self.version_agent.append(self.browser.execute_script("return navigator.appVersion;"))
        self.locale.append(self.browser.execute_script("return Intl.DateTimeFormat().resolvedOptions().timeZone"))
        self.platform.append(self.browser.execute_script("return navigator.platform"))
        self.timer.append(self.browser.execute_script("return new Date()"))




def main():
    input = sys.argv[1]
    obj = Crawler(input)
    obj.spyder("http://www.portaldalinguaportuguesa.org/index.php?action=fonetica&region=spx&act=list&letter=")
    obj.finish()

if __name__ == "__main__":
    main()




