import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.wikipedia.org/")

#https://www.selenium.dev/documentation/webdriver/support_features/select_lists/
#https://www.selenium.dev/selenium/docs/api//py/webdriver_support/selenium.webdriver.support.select.html

driver.find_element(By.ID,"searchLanguage").send_keys('Eesti') #----> not recommended bcoz cannot find the exact value
time.sleep(5)

driver.close()