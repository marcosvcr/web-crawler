from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
import string
import random
import sys
import asyncio


async def fetch(url, session):
    with session.get(url) as response:
        time.sleep(5)

        name_agent = await response.execute_script("return navigator.appName;")
        WebDriverWait(session, 5).until(name_agent)
        version_agent = await response.execute_script("return navigator.appVersion;")
        WebDriverWait(session, 5).until(version_agent)
        locale_agent = await response.execute_script("return Intl.DateTimeFormat().resolvedOptions().timeZone")
        WebDriverWait(session, 5).until(locale_agent)
        platform_agent = await response.execute_script("return navigator.platform")
        WebDriverWait(session, 5).until(platform_agent)
        timer_agent = await response.execute_script("return new Date()")
        WebDriverWait(session, 5).until(timer_agent)
        return {"name": name_agent, "version": version_agent, "locale": locale_agent, "platform": platform_agent, "timer":timer_agent}

async def middlepoint(sem, url, session):
    async with sem:
        return await fetch(url, session)

async def main():
    driver = sys.argv[1]
    maxpage = 50
    num = 0
    number_visited = 0
    tasks = []
    sem = asyncio.Semaphore(10)
    with webdriver.Chrome(driver) as session:
        session.implicitly_wait(30)
        for i in range(0,maxpage):
            letter = random.choice(list(string.ascii_lowercase))
            number_visited = number_visited + 1
            num = num + 20
            url = "http://www.portaldalinguaportuguesa.org/index.php?action=fonetica&region=spx&act=list&letter=" + letter + "&start=" + str(num)
            print(number_visited, "Accessing", url)
            tasks.append(
                asyncio.create_task(
                    middlepoint(sem,url,session)
                )
            )




results = asyncio.run(main())

for result in results:
    print(result)
