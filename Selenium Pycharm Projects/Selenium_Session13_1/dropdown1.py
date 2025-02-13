import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://echoecho.com/htmlforms11.htm")

#https://www.selenium.dev/documentation/webdriver/support_features/select_lists/
#https://www.selenium.dev/selenium/docs/api//py/webdriver_support/selenium.webdriver.support.select.html

#jahan par <select> ka tag use ho rha ho wahan select ki class use kro
driver.find_element(By.NAME,"dropdownmenu").send_keys("Milk")
time.sleep(3)


driver.close()