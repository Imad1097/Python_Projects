import time

import driver
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()
#   ("https://"write username here":"write password here"@the-internet.herokuapp.com/basic_auth"
#   we do this bcoz we cannot inspect and locate that element (BasicAuth i.e username & password)
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(5)