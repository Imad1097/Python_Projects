import time

import driver
from cffi.cffi_opcode import PRIM_SCHAR
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/")

driver.get_screenshot_as_png()
screenshot_path = 'fullpage.png'
driver.save_screenshot(screenshot_path)



