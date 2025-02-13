import time

import driver
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://cosmocode.io/automation-practice-webtable/")
time.sleep(3)

table = driver.find_element(By.TAG_NAME,"table")
rows = table.find_elements(By.TAG_NAME,"tr")

target_value = 'Pakistan'
found = False

for row in rows:
    allcells = row.find_elements(By.TAG_NAME,"td")
    for cell in allcells:
        if target_value == cell.text:
            print("value found")
            found = True
            break
if found:
    print(target_value)
else:
    print(f"target value {target_value} not found")

driver.close()