import time

import driver
from cffi.cffi_opcode import PRIM_SCHAR
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")

search_bar = driver.find_element(By.CSS_SELECTOR,"#APjFqb")
search_bar.send_keys("Selenium with python")

time.sleep(3)
driver.get_screenshot_as_png()
screenshot_path = 'Google_search.png'
driver.save_screenshot(screenshot_path)