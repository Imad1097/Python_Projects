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
value_check = 'Deutsch'
value_exist = False

for option in select.options:
    if option.text == value_check:
        value_exist = True
        break
if value_exist:
    print(value_check)
else:
    print('value not found')

time.sleep(5)

driver.close()