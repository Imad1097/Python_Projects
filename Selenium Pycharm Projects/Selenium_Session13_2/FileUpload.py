import time

import driver
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(5)

#giving the path of the file name through send.keys bcoz if we use .click on the "choose file"
#it will open system window & it cannot be locate by webdriver bcoz its outside the browser.
file_input = driver.find_element(By.ID,"file-upload")
file_input.send_keys("C:\\Users\\Abc\\Pictures\\Screenshots\\Home Of Good _ Nestlé Malaysia_files\\Deals.png")
upload_button = driver.find_element(By.CLASS_NAME,"button")
upload_button.click()

time.sleep(5)
