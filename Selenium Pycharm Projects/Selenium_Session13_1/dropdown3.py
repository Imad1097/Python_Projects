import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.wikipedia.org/")

#https://www.selenium.dev/documentation/webdriver/support_features/select_lists/
#https://www.selenium.dev/selenium/docs/api//py/webdriver_support/selenium.webdriver.support.select.html

dropdown = driver.find_element(By.ID,"searchLanguage")
time.sleep(2)
select = Select(dropdown) #object #parametertize constructor
#multiple ways to select dropdowns
#select.select_by_index(1)
#select.select_by_value("et")
select.select_by_visible_text("Español")

#getting the number of length of all option in select tag
options = driver.find_elements(By.TAG_NAME,"option")
a = len(options)
print(a)

time.sleep(5)

driver.close()