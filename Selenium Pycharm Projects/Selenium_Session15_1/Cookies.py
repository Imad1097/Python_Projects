import time

import driver
from cffi.cffi_opcode import PRIM_SCHAR
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
cookies = driver.get_cookies()

for cookie in cookies:
    print(cookie)
NID = driver.get_cookie("NID")
print("-----------------------------------")
print(NID)