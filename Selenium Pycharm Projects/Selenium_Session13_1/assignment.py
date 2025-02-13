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
time.sleep(5)
print(type(links))
count = len(links)
print(count)

actual_link = 'https://meta.wikimedia.org/wiki/Special:MyLanguage/List_of_Wikipedias'
link_exist = False

for link in links:
    all_link = link.get_attribute('href')
    #print(all_link)
    if all_link == actual_link:
        link_exist = True
        break
if (link_exist):
    print(actual_link)
else:
    print('value not found')

driver.close()