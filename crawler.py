from selenium import webdriver
import time
import pandas as pd
import string
import random
from bs4 import BeautifulSoup
import sys
class Crawler:


    def __init__(self, driver):
        super(Crawler,self)
        self.browser= webdriver.Chrome(driver)
        self.userAgents = []
        self.pageTrasitionEvents = []
        self.consoles = []
        self.dates = []
        self.locations = []

    def finish(self):
        self.browser.quit()


    def spyder(self,sites):

        maxpage = len(sites)
        number_visited = 0
        num = 0
        _response = True
        while _response == True and number_visited < maxpage:
            date = False
            userAgent = False
            pageTrasitionEvent = False
            console = False
            location = False
            print(number_visited, "Accessing", sites[number_visited])
            try:
                self.browser.get(sites[number_visited])
                print("Success")


                time.sleep(5)
                html_code = self.browser.page_source
                parsed_html = BeautifulSoup(html_code, features="html.parser")
                elements = parsed_html.find_all("script")
                count = 0
                for element in elements:
                    if(element.find("navigator.userAgent") != -1 ):
                        userAgent = True
                    if(element.find(".addeventListener") != -1):
                        pageTrasitionEvent = True
                    if(element.find("window.console") != -1 or element.find("console.log")):
                        console = True
                    if(element.find("window.location") != -1 or element.find("document.location")):
                        location = True
                    if(element.find("Date.now()") != -1 or element.find(".getTime")):
                        date = True
                    if(all(elem == True for elem in [console, userAgent, pageTrasitionEvent, location, date]) == True):
                        self.locations.append(str(location))
                        self.userAgents.append(str(userAgent))
                        self.consoles.append(str(console))
                        self.pageTrasitionEvents.append(str(pageTrasitionEvent))
                        self.dates.append(str(date))
                        break
            except:
                print("Failed")
                self.locations.append(str(-1))
                self.userAgents.append(str(-1))
                self.consoles.append(str(-1))
                self.pageTrasitionEvents.append(str(-1))
                self.dates.append(str(-1))

            number_visited= number_visited + 1
        df = pd.DataFrame({"User Agent": self.userAgents, "Location": self.locations, "console:": self.consoles, "pageTrasitionEvent": self.pageTrasitionEvents, "Time": self.dates})
        df.to_csv("agent_info.csv", sep=";")




def main():
    sites = []

    with open(sys.argv[2], 'r') as filehandle:
        filecontents = filehandle.readlines()

        for line in filecontents:
            current_site = line[:-1]
            sites.append(current_site)

    input = sys.argv[1]
    obj = Crawler(input)
    obj.spyder(sites)
    obj.finish()

if __name__ == "__main__":
    main()




