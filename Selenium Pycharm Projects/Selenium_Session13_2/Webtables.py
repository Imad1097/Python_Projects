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

time.sleep(5)

rows_count = len(rows)
print(rows_count)

for row in rows:
    All_cell = row.find_elements(By.TAG_NAME,"td")
    for each_cell in All_cell:
        print(each_cell.text)


driver.close()