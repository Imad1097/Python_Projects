import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.wikipedia.org/")

links = driver.find_elements(By.TAG_NAME,"a")
print(type(links))
count = len(links)
print(count)

for link in links:
    All_link = link.get_attribute("href")
    print(All_link)

